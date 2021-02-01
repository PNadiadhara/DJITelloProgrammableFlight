from djitellopy import tello
from time import sleep

drone = tello.Tello()

# Connect to tello via wi-fi
drone.connect()

print(drone.get_battery())

#     def send_rc_control(self, left_right_velocity, forward_backward_velocity, up_down_velocity, yaw_velocity):
#         """Send RC control via four channels. Command is sent every self.TIME_BTW_RC_CONTROL_COMMANDS seconds.
#         Arguments:
#             left_right_velocity: -100~100 (left/right)
#             forward_backward_velocity: -100~100 (forward/backward)
#             up_down_velocity: -100~100 (up/down)
#             yaw_velocity: -100~100 (yaw)
#         Returns:
#             bool: True for successful, False for unsuccessful
#         """

drone.takeoff()

drone.send_rc_control(0,0,0,90)
sleep(2)
drone.send_rc_control(0,0,0,0)
drone.land()