function getXIntercept(t1, t2, a1, a2) {
    //  y = mx + c --> f|| x intercept  x = (0 - c) / m
    m = (a1 - a2) / (t1 - t2)
    c = ((t1 * a2) - (a1 * t2)) / (t1 - t2)
    x = (-c) / m
    return x
}
function getChangeInVelocity(a1, a2, t1, t2) {
    v2 = 0.5 * (Math.abs(a1 - a2) * (t2 - t1))
    // constant state of acceleration
    if ((a1 >= 0 && a2 >= 0)) {
        v1 = Math.min(a1, a2) * (t2 - t1)
        return v1 + v2
    }
    // constant state of deceleration
    else if (a1 <= 0 && a2 <= 0) {
        v1 = Math.max(a1, a2) * (t2 - t1)
        return v1 - v2
    }
    // initial acceleration followed by deceleration
    else if ((a1 < 0 && a2 > 0) || (a1 > 0 && a2 < 0)) {
        intercept = getXIntercept(t1, t2, a1, a2)
        return getChangeInVelocity(a1, 0, t1, intercept) + getChangeInVelocity(0, a2, intercept, t2)

    }
}

module.exports = {
    getChangeInVelocity
}

console.log(getXIntercept(1648815892.3228457, 1648815892.4310644, 0.4130859375, -0.012451171875));
// console.log(getXIntercept(5,7,1,-1));