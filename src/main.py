#region VEXcode Generated Robot Configuration
from vex import *
# import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
controller_1 = Controller(PRIMARY)
LeftMotor = Motor(Ports.PORT19, GearSetting.RATIO_18_1, False)
RightMotor = Motor(Ports.PORT12, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)
#endregion VEXcode Generated Robot Configuration
myVariable = 0

def when_started1():
    global myVariable
    pass

def onauton_autonomous_0():
    global myVariable
    pass

def ondriver_drivercontrol_0():
    global myVariable
    while True:
        # Control the drivetrain using the controller
        LeftMotor.set_velocity((controller_1.axis3.position() + controller_1.axis3.position()), PERCENT)
        RightMotor.set_velocity((controller_1.axis1.position() - controller_1.axis1.position()), PERCENT)
        LeftMotor.spin(FORWARD)
        RightMotor.spin(FORWARD)
        wait(5, MSEC)

# create a function for handling the starting and stopping of all autonomous tasks
def vexcode_auton_function():
    # Start the autonomous control tasks
    auton_task_0 = Thread( onauton_autonomous_0 )
    # wait for the driver control period to end
    while( competition.is_autonomous() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the autonomous control tasks
    auton_task_0.stop()

def vexcode_driver_function():
    # Start the driver control tasks
    driver_control_task_0 = Thread( ondriver_drivercontrol_0 )

    # wait for the driver control period to end
    while( competition.is_driver_control() and competition.is_enabled() ):
        # wait 10 milliseconds before checking again
        wait( 10, MSEC )
    # Stop the driver control tasks
    driver_control_task_0.stop()


# register the competition functions
competition = Competition( vexcode_driver_function, vexcode_auton_function )

when_started1()
