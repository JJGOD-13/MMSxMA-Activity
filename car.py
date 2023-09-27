from MMScar import *
#============================
# Start your code from here
#============================
@decoration
def main():
    
    move_forward(2, 100)
    




if __name__ == "__main__":



    while board.digital_read(buttonPin)[0] == 0:
        time.sleep(0.001)

    main()



