#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
Left_motor_a = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)
Left_motor_b = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
Left = MotorGroup(Left_motor_a, Left_motor_b)
Right_motor_a = Motor(Ports.PORT11, GearSetting.RATIO_18_1, False)
Right_motor_b = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)
Right = MotorGroup(Right_motor_a, Right_motor_b)
Shoot = Motor(Ports.PORT4, GearSetting.RATIO_36_1, False)
Intake_motor_a = Motor(Ports.PORT1, GearSetting.RATIO_36_1, False)
Intake_motor_b = Motor(Ports.PORT10, GearSetting.RATIO_36_1, True)
Intake = MotorGroup(Intake_motor_a, Intake_motor_b)
Pole = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
controller_1 = Controller(PRIMARY)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration

# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
# Callback function when controller_1 ButtonR1 is pressed
def controller_R1_pressed():
    Left.spin(FORWARD)
    Right.spin(FORWARD)
    while controller_1.buttonR1.pressing():
        # Wait until ButtonR2 is released
        wait(5, MSEC)
    Left.stop()


# Callback function when controller_1 ButtonR2 is pressed
def controller_R2_pressed():
    Left.spin(REVERSE)
    Right.spin(REVERSE)
    while controller_1.buttonR2.pressing():
        # Wait until ButtonR2 is released
        wait(5, MSEC)
    Left.stop()

def controller_L2_pressed():
    Intake.spin(REVERSE)
    Shoot.spin(REVERSE)
    while controller_1.buttonL2.pressing():
        # Wait until ButtonR2 is released
        wait(5, MSEC)
    Shoot.stop()
    Intake.stop()

# Create Controller callback events
controller_1.buttonR1.pressed(controller_R1_pressed)
controller_1.buttonR2.pressed(controller_R2_pressed)
controller_1.buttonL2.pressed(controller_L2_pressed)


# 15 msec delay to ensure events get registered
wait(15, MSEC)

Left.set_velocity(100, PERCENT)
