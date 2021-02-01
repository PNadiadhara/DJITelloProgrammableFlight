from djitellopy import tello
import cv2


drone = tello.Tello()

# Connect to tello via wi-fi
drone.connect()
drone.get_battery()


# get video stream from tello
drone.stream_on()

while True:
    img = drone.get_frame_read().frame
    # reduce data space requirements, original tello resolution: 720p and img resolution is 2592 x 1936
    img = cv2.resize(img, (360, 240))

    # create popup window to display img
    cv2.imshow("Image", img)

    cv2.waitKey(1)