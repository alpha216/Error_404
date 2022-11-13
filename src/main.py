#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
intake_motor_group_motor_a = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
intake_motor_group_motor_b = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
intake_motor_group = MotorGroup(intake_motor_group_motor_a, intake_motor_group_motor_b)
controller_1 = Controller(PRIMARY)
left_drive_smart = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT12, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 219.44, 290, 40, MM, 1)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# define variables used for controlling motors based on controller inputs
drivetrain_l_needs_to_be_stopped_controller_1 = False
drivetrain_r_needs_to_be_stopped_controller_1 = False

# define a task that will handle monitoring inputs from controller_1
def rc_auto_loop_function_controller_1():
    global drivetrain_l_needs_to_be_stopped_controller_1, drivetrain_r_needs_to_be_stopped_controller_1, remote_control_code_enabled
    # process the controller input every 20 milliseconds
    # update the motors based on the input values
    while True:
        if remote_control_code_enabled:
            
            # calculate the drivetrain motor velocities from the controller joystick axies
            # left = axis3
            # right = axis2
            drivetrain_left_side_speed = controller_1.axis3.position()
            drivetrain_right_side_speed = controller_1.axis2.position()
            
            # check if the value is inside of the deadband range
            if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                # check if the left motor has already been stopped
                if drivetrain_l_needs_to_be_stopped_controller_1:
                    # stop the left drive motor
                    left_drive_smart.stop()
                    # tell the code that the left motor has been stopped
                    drivetrain_l_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the left motor next
                # time the input is in the deadband range
                drivetrain_l_needs_to_be_stopped_controller_1 = True
            # check if the value is inside of the deadband range
            if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                # check if the right motor has already been stopped
                if drivetrain_r_needs_to_be_stopped_controller_1:
                    # stop the right drive motor
                    right_drive_smart.stop()
                    # tell the code that the right motor has been stopped
                    drivetrain_r_needs_to_be_stopped_controller_1 = False
            else:
                # reset the toggle so that the deadband code knows to stop the right motor next
                # time the input is in the deadband range
                drivetrain_r_needs_to_be_stopped_controller_1 = True
            
            # only tell the left drive motor to spin if the values are not in the deadband range
            if drivetrain_l_needs_to_be_stopped_controller_1:
                left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                left_drive_smart.spin(FORWARD)
            # only tell the right drive motor to spin if the values are not in the deadband range
            if drivetrain_r_needs_to_be_stopped_controller_1:
                right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                right_drive_smart.spin(FORWARD)
        # wait before repeating the process
        wait(20, MSEC)

# define variable for remote controller enable/disable
remote_control_code_enabled = True

rc_auto_loop_thread_controller_1 = Thread(rc_auto_loop_function_controller_1)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------------------------------------------
#
#    Project:        Controlling Disco
#    Description:    This program will show you how to control the
#                    VRC 2022 Herobot Disco's Intake Motor Group with the
#                    "When Controller" events and the drivetrain with the
#                    configured controller.
#                    The R1 button will intake
#                    The R2 button will outtake
#                    The Joystick is configured with Tank controls
#    Configuration:  VRC 2022 Disco (Drivetrain 2-motor, No Gyro)
#                    Intake Motor Group in Ports 10 & 20
#                    Controller
#
# ------------------------------------------------------------------------------


# Begin project code
# Callback function when controller_1 ButtonR1 is pressed
def controller_R1_pressed():
    intake_motor_group.spin(FORWARD)
    while controller_1.buttonR1.pressing():
        # Wait until ButtonR2 is released
        wait(5, MSEC)
    intake_motor_group.stop()


# Callback function when controller_1 ButtonR2 is pressed
def controller_R2_pressed():
    intake_motor_group.spin(REVERSE)
    while controller_1.buttonR2.pressing():
        # Wait until ButtonR2 is released
        wait(5, MSEC)
    intake_motor_group.stop()


# Create Controller callback events
controller_1.buttonR1.pressed(controller_R1_pressed)
controller_1.buttonR2.pressed(controller_R2_pressed)

# 15 msec delay to ensure events get registered
wait(15, MSEC)

intake_motor_group.set_velocity(100, PERCENT)
