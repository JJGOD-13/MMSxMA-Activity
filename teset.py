from pymata4 import pymata4
import time


# Make board

board = pymata4.Pymata4()


# 6 and 7 are for motor 1
# 8 and 9 are for motor 2
speedPins = [6,7,8,9]

# 10 is for motor 1
# 5 is for motor 2
pwmPins = [10,5]

buttonPin = 3

# Set all the pin modes
# for pin in speedPins:
#     board.set_pin_mode_digital_output(pin)

# for pin in pwmPins:
#     board.set_pin_mode_pwm_output(pin)

# # Quick Test
def motor():
    print("Button pressed")
    board.digital_write(6,1)
    board.digital_write(7,0)
    board.pwm_write(5, 250)


    time.sleep(5)

    board.digital_write(6,0)
    board.digital_write(7,0)
    board.pwm_write(5, 0)

    board.shutdown()


# board.set_pin_mode_digital_input_pullup(buttonPin, callback=motor)



# for pin in speedPins:
#     board.set_pin_mode_digital_output(pin)

# for pin in pwmPins:
#     board.set_pin_mode_pwm_output(pin)


# # Try to move just the right motor

# board.digital_write(8,1)




# board.shutdown()

if __name__ == "__main__":

    for pin in speedPins:
        board.set_pin_mode_digital_output(pin)

    for pin in pwmPins:
        board.set_pin_mode_pwm_output(pin)

    board.set_pin_mode_digital_input(buttonPin)

    val = board.digital_read(buttonPin)
    print(val)
    
    while board.digital_read(buttonPin)[0] == 0:
        time.sleep(0.001)
    motor()

    

   
