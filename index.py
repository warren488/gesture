import string
import sensors
import time

# accelerometer and gyro on any i2c pin
sensor_pins={ "accel":3,
"gyro":3, "button": 2}
sensors.set_pins(sensor_pins)
count = 1
ready = 1

def incrementOnButtonPress(ready, level, count): 
    if level == 1 and ready == 0:
        return ready, count
    if level == 0 and ready == 0:
        return 1, count
    if level == 1 and ready == 1:
        return 0, (count + 1) % 4
    if level == 0 and ready == 1:
        return ready, count

def interactive():
 # acceleration in x,y,z axes
    ax,ay,az=sensors.accel.get_xyz() 
    # magnitude of acceleration
    am = sensors.accel.get_magnitude() 
    # rotation around x,y,z axes
    rx,ry,rz=sensors.gyro.get_xyz() 
    # magnitude of rotation
    rm = sensors.gyro.get_magnitude()
    ready, count = incrementOnButtonPress(ready, sensors.button.get_level(), count)
    print(ready, count)
    if(count == 1): 
        print('accel x:', (ax))
    if(count == 2): 
        print('accel y:', (ay))
    if(count == 3): 
        print('accel z:', (az))
    # if(sensors.button.get_level() == 1): 
    #     print(ax,ay,az,am,rx,ry,rz,rm) 
    
    time.sleep(.1)


print('time,ax,ay,az,am,gx,gy,gz,gm,button')
while True:
    # acceleration in x,y,z axes
    ax,ay,az=sensors.accel.get_xyz() 
    # magnitude of acceleration
    am = sensors.accel.get_magnitude() 
    # rotation around x,y,z axes
    gx,gy,gz=sensors.gyro.get_xyz() 
    # magnitude of rotation
    gm = sensors.gyro.get_magnitude()
    print(time.time(),ax,ay,az,am,gx,gy,gz,gm, sensors.button.get_level())
    
    time.sleep(.1)


