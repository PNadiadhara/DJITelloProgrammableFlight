from djitellopy import tello
import keyBoardControlModule as KCM
from time import sleep


KCM.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def getKeyboardInput():
    velocity = 50
    leftRight, forwardBackward, upDown, yawVelocity = 0, 0, 0, 0

    if KCM.getKey("LEFT"):
        leftRight = -velocity
    elif KCM.getKey("RIGHT"):
        leftRight = velocity

    if KCM.getKey("UP"):
        forwardBackward = velocity
    elif KCM.getKey("DOWN"):
        forwardBackward = -velocity

    if KCM.getKey("w"):
        upDown = velocity
    elif KCM.getKey("s"):
        upDown = -velocity

    if KCM.getKey("a"):
        yawVelocity = velocity
    elif KCM.getKey("d"):
        yawVelocity = -velocity

    if KCM.getKey("q"):
        drone.takeoff()
    if KCM.getKey("e"):
        drone.land()

    return [leftRight, forwardBackward, upDown, yawVelocity]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    # buffer time
    sleep(0.05)