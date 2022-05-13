
def getXIntercept( x1, x2, y1, y2):
    #  y = mx + c --> for x intercept  x = (0 - c) / m
    m = (y1 - y2) / (x1 - x2)
    c = ((x1*y2) - (y1*x2)) / (x1 - x2)
    x = (-c)/m
    return x

def getAreaUnderGraph(y1, y2, x1, x2):
    v2 = 0.5 * (abs(y1 - y2) * (x2 - x1))
    # state of acceleration
    if((y1 >= 0 and y2 >= 0)):
        v1 = min(y1, y2) * (x2 -x1)
        return v1 + v2
    # state of deceleration
    elif(y1 <= 0 and y2 <= 0):
        v1 = max(y1, y2) * (x2 -x1)
        return v1 - v2
    # initial acceleration followed by deceleration
    elif((y1 < 0 and y2 > 0) or (y1 > 0 and y2 < 0)):
        intercept = getXIntercept(x1, x2, y1, y2)
        return getAreaUnderGraph(y1, 0, x1, intercept) + getAreaUnderGraph(0, y2, intercept, x2)

