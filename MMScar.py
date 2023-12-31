from pymata4 import pymata4
import time


# Create a pymata4 instance
board = pymata4.Pymata4()

# ===================================
# Set up all the pin variables
# ===================================

# 6 and 7 are for motor 1
# 8 and 9 are for motor 2

speedPins = [6,7,8,9]

# 10 is for motor 1
# 5 is for motor 2

pwmPins = [10,5]

# This pin will be set to the digital
buttonPin = 3




# ===================================
# Set up all the pin modes
# ===================================

for pin in speedPins:
    board.set_pin_mode_digital_output(pin)

for pin in pwmPins:
    board.set_pin_mode_pwm_output(pin)

board.set_pin_mode_digital_input(buttonPin)



# ===================================
# Define all the functions
# ===================================

def speedconvert(speed):
    return int(speed*255/100)


def move_forward(Time, speed):
    """
    Moves the car forward.
    time: how long to move forward in seconds
    speed: how fast to move forward, 0-100

    """

    # Validate input
    if Time < 0:
        raise ValueError("Time must be positive")
    if speed < 0 or speed > 100:
        raise ValueError("Speed must be between 0 and 100")
    

    # Set all the pins to forward position

    board.digital_write(6,1)
    board.digital_write(7,0)
    board.digital_write(8,1)
    board.digital_write(9,0)

    # Set the PWM pins to the speed
    board.pwm_write(10, speedconvert(speed))
    board.pwm_write(5, speedconvert(speed))

    # Wait for the time
    time.sleep(Time)

    # Turn off the motors
    board.digital_write(6,0)
    board.digital_write(7,0)
    board.digital_write(8,0)
    board.digital_write(9,0)
    board.pwm_write(10, 0)
    board.pwm_write(5, 0)



def move_backward(Time, speed):

    # Validate input
    if Time < 0:
        raise ValueError("Time must be positive")

    if speed < 0 or speed > 100:
        raise ValueError("Speed must be between 0 and 100")

   # Set all the pins to backwards position

    board.digital_write(6,0)
    board.digital_write(7,1)
    board.digital_write(8,0)
    board.digital_write(9,1)

    # Set the PWM pins to the speed
    board.pwm_write(10, speedconvert(speed))
    board.pwm_write(5, speedconvert(speed))

    # Wait for the time
    time.sleep(Time)

    # Turn off the motors
    board.digital_write(6,0)
    board.digital_write(7,0)
    board.digital_write(8,0)
    board.digital_write(9,0)
    board.pwm_write(10, 0)
    board.pwm_write(5, 0)


def turn_left(Time, speed):

    # Validate input
    if Time < 0:
        raise ValueError("Time must be positive")

    if speed < 0 or speed > 100:
        raise ValueError("Speed must be between 0 and 100")
    
    # Set left wheel to spin backwards and right wheel to spin forwards

    board.digital_write(6,0)
    board.digital_write(7,1)
    board.digital_write(8,1)
    board.digital_write(9,0)

    # Set the PWM pins to the speed
    board.pwm_write(10, speedconvert(speed))
    board.pwm_write(5, speedconvert(speed))

    # Wait for the time
    time.sleep(Time)

    # Turn off the motors
    board.digital_write(6,0)
    board.digital_write(7,0)
    board.digital_write(8,0)
    board.digital_write(9,0)
    board.pwm_write(10, 0)
    board.pwm_write(5, 0)


def turn_right(Time, speed):

    # Validate input
    if Time < 0:
        raise ValueError("Time must be positive")

    if speed < 0 or speed > 100:
        raise ValueError("Speed must be between 0 and 100")
    
    # Set left wheel to spin forwards and right wheel to spin backwards

    board.digital_write(6,1)
    board.digital_write(7,0)
    board.digital_write(8,0)
    board.digital_write(9,1)

    # Set the PWM pins to the speed
    board.pwm_write(10, speedconvert(speed))
    board.pwm_write(5, speedconvert(speed))

    # Wait for the time
    time.sleep(Time)

    # Turn off the motors
    board.digital_write(6,0)
    board.digital_write(7,0)
    board.digital_write(8,0)
    board.digital_write(9,0)
    board.pwm_write(10, 0)
    board.pwm_write(5, 0)


def decoration(func):
    
    def wrapper():
        print("Button pressed")
        func()
        board.shutdown()
    return wrapper