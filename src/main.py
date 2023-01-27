#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
Intake = Motor(Ports.PORT13, GearSetting.RATIO_36_1, True)
Shoot = Motor(Ports.PORT1, GearSetting.RATIO_36_1, True)
Roller = Motor(Ports.PORT15, GearSetting.RATIO_36_1, True)
# Shoot = MotorGroup(Shoot_1, Shoot_2)
Left_1 = Motor(Ports.PORT10, GearSetting.RATIO_6_1, False)
Left_2 = Motor(Ports.PORT16, GearSetting.RATIO_6_1, False)
Left = MotorGroup(Left_1, Left_2)
Right_1 = Motor(Ports.PORT3, GearSetting.RATIO_6_1, True)
Right_2 = Motor(Ports.PORT13, GearSetting.RATIO_6_1, True)
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
    
# def R1():
#     Roller.spin(FORWARD)
#     while controller_1.buttonR1.pressing():
#         wait(5, MSEC)
#     Roller.stop()
    
def R2():
    # Roller.spin(REVERSE)
    Roller.spin_for(FORWARD, -50, DEGREES, wait=True)
    wait(20, MSEC)
    Roller.spin_for(FORWARD, 50, DEGREES, wait=True)

    # Roller.stop()
    
def ax3():
    Left.set_velocity(controller_1.axis3.position(), PERCENT)
    Right.set_velocity(controller_1.axis3.position(), PERCENT)    
    Left.spin(REVERSE)
    Right.spin(REVERSE)

def ax1():
    Left_1.set_velocity(-0.75*controller_1.axis1.position(), PERCENT)
    Left_2.set_velocity(-0.75*controller_1.axis1.position(), PERCENT)
    Right_1.set_velocity(0.75*controller_1.axis1.position(), PERCENT)
    Right_2.set_velocity(0.75*controller_1.axis1.position(), PERCENT)
    Left.spin(FORWARD)
    Right.spin(FORWARD)


# Create Controller callback events
controller_1.buttonL1.pressed(L1)
controller_1.buttonL2.pressed(L2)
# controller_1.buttonR1.pressed(R1)
controller_1.buttonR2.pressed(R2)
controller_1.axis3.changed(ax3)
controller_1.axis1.changed(ax1)


# 15 msec delay to ensure events get registered
wait(15, MSEC)

Intake.set_velocity(70, PERCENT)
Shoot.set_velocity(100, PERCENT)
# Shoot_2.set_velocity(100, PERCENT)


