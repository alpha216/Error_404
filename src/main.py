#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
Intake = Motor(Ports.PORT18, GearSetting.RATIO_36_1, False)
Shoot_1 = Motor(Ports.PORT20, GearSetting.RATIO_6_1, False)
Shoot_2 = Motor(Ports.PORT19, GearSetting.RATIO_6_1, False)
Shoot = MotorGroup(Shoot_1, Shoot_2)
Left_1 = Motor(Ports.PORT6, GearSetting.RATIO_36_1, False)
Left_2 = Motor(Ports.PORT16, GearSetting.RATIO_36_1, False)
Left = MotorGroup(Left_1, Left_2)
Right_1 = Motor(Ports.PORT5, GearSetting.RATIO_36_1, True)
Right_2 = Motor(Ports.PORT15, GearSetting.RATIO_36_1, True)
Right = MotorGroup(Right_1, Right_2)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
# Callback function when controller_1 ButtonR1 is pressed
def L1():
    Intake.spin(FORWARD)
    while controller_1.buttonL1.pressing():
        wait(5, MSEC)
    Intake.stop()
    
def L2():
    Shoot.spin(FORWARD)
    while controller_1.buttonL2.pressing():
        wait(5, MSEC)
    Shoot.stop()
    
def R1():
    Left.spin(FORWARD)
    Right.spin(FORWARD)
    while controller_1.buttonR1.pressing():
        wait(5, MSEC)
    Left.stop()
    Right.stop()

def R2():
    Left.spin(REVERSE)
    Right.spin(REVERSE)
    while controller_1.buttonR2.pressing():
        wait(5, MSEC)
    Left.stop()
    Right.stop()


# Create Controller callback events
controller_1.buttonL1.pressed(L1)
controller_1.buttonL2.pressed(L2)
controller_1.buttonR1.pressed(R1)
controller_1.buttonR2.pressed(R2)


# 15 msec delay to ensure events get registered
wait(15, MSEC)

Intake.set_velocity(100, RPM)
Shoot_1.set_velocity(3200, RPM)
Shoot_2.set_velocity(3200, RPM)





