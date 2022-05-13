import sensors
import time
from filters import HighPassFilter, LowPassFilter
from capture_lib import getAreaUnderGraph, getXIntercept

start = 0
sensed = 0
ready = 1
velocity = 0
velocityp = 0
distance = 0
distancep = 0
axp = 0
ayp = 0
azp = 0
tp = 0
# accelerometer and gyro on any i2c pin
sensor_pins={ "accel":3,"gyro":3, "button": 7}
sensors.set_pins(sensor_pins)



def senseGesture(ready, level, start, count, sensed, velocity, distance): 
    # we've already sensed the relevant gesture for this button press, but the user hasnt released as yet
    if sensed == 1 and level == 1:
        return velocity, distance, ready, start, sensed
    # print('here', ready, level, start, count, sensed, velocity, distance)
    # continuous sensing from an earlier button press
    if level == 1 and ready == 0:
        velocity = velocityp + getAreaUnderGraph(axp, count, tp, t)
        distance = distancep + getAreaUnderGraph(velocityp, velocity, tp, t)
        # print(distance)
        if(distance > 0.01):
            sensed = 1
            # print("swipe detected")
        if(distance < -0.01):
            sensed = 1
            # print("swipe detected")
        return velocity, distance, ready, start, sensed
    # button finally released, reset and get ready for another press 
    if level == 0 and ready == 0:
        velocity = 0
        distance = 0
        sensed = 0
        ready = 1
        start = 0
        return velocity, distance, ready, start, sensed
    # button press just happened
    if level == 1 and ready == 1:
        start = count
        ready = 0
        return velocity, distance, ready, start, sensed
    # nothing doing
    if level == 0 and ready == 1:
        return velocity, distance, ready, start, sensed

# print('time,ax,ay,az,am,gx,gy,gz,gm,velx,distx,button')
print('true','highpass','lowpass','a_median','a_slidingAverage','high_low','low_high', sep = ',')
HIGH_FILTER_TIME_CONSTANT=.5
LOW_FILTER_TIME_CONSTANT=.5
highFilter=HighPassFilter.make_from_time_constant(HIGH_FILTER_TIME_CONSTANT,0.1)
lowFilter=LowPassFilter.make_from_time_constant(LOW_FILTER_TIME_CONSTANT,0.01)
while True:
    t = time.time()
    # acceleration in x,y,z axes
    ax,ay,az=sensors.accel.get_xyz() 
    # magnitude of acceleration
    am = sensors.accel.get_magnitude() 
    # rotation around x,y,z axes
    gx,gy,gz=sensors.gyro.get_xyz() 
    # magnitude of rotation
    gm = sensors.gyro.get_magnitude()

    # ----------------------- FILTER CODE ---------------------------------------
    axt = ax
    a_high=highFilter.on_value(axt)
    a_low=lowFilter.on_value(axt)
    high_low=lowFilter.on_value(a_high)
    low_high=highFilter.on_value(a_low)
    print(axt,a_low,a_high,high_low,low_high, sep=',')
    # ----------------------- END FILTER CODE ---------------------------------------


    # this check is to simply make sure we only start running after we have some values to use in our calculations
    if(tp != 0):
        velocity, distance, ready, start, sensed = senseGesture(ready, sensors.button.get_level(), start, ax, sensed, velocity, distance)
        # print(time.time(),a_fil,ay,az,am,gx,gy,gz,gm,velocity,distance, sensors.button.get_level(), sep = ',')
    # store these for the next loop so we can calculate the change in velocity
    axp = ax
    ayp = ay
    azp = az
    tp = t
    velocityp = velocity
    distancep = distance
    # time.sleep(.1)