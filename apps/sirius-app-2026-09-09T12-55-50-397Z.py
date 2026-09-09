from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

# Initialize the hub. Assuming a PrimeHub, but you can change this to EV3Brick, MoveHub, etc.
hub = PrimeHub()

# Initialize a motor on Port A.
# You can change this to any port where your motor is connected (e.g., Port.B, Port.C, Port.D, Port.E, Port.F).
motor = Motor(Port.A)

# Run the motor clockwise at a speed of 500 degrees per second.
# The motor will run for 2000 milliseconds (2 seconds).
motor.run_time(500, 2000, wait=True)

# Stop the motor.
motor.stop()

# Wait for a moment before ending the program.
wait(1000)