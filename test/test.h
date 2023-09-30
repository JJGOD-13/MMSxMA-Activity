/* 
This file contains all of the necessary functions that will be used by the car.ino file such that the 
kids can use the functions in order to run the car.
*/

// Setup all the pins

// Motor A
int ENA = 10;
int IN1 = 9;
int IN2 = 8;

// Motor B
int ENB = 5;
int IN3 = 7;
int IN4 = 6;

void speedconvert(int speed)
{
    // This function will convert the speed from a 0-100 scale to a 0-255 scale
    // This is necessary because the kids will be using a 0-100 scale for the speed
    // but the motor controller uses a 0-255 scale for the speed.
    speed = speed * 2.55;
}

void move_forward(int time, int speed)
{
    // This function will move the car forward for a certain amount of time at a certain speed
    // The speed will be a 0-100 scale and will be converted to a 0-255 scale
    // The time will be in seconds
    speedconvert(speed);
    analogWrite(ENA, speed);
    analogWrite(ENB, speed);
    digitalWrite(IN1, HIGH);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, HIGH);
    digitalWrite(IN4, LOW);
    delay(time * 1000);

    // turn off the motors
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);

   
}

void move_backward(int time, int speed)
{
    // This function will move the car backward for a certain amount of time at a certain speed
    // The speed will be a 0-100 scale and will be converted to a 0-255 scale
    // The time will be in seconds
    speedconvert(speed);
    analogWrite(ENA, speed);
    analogWrite(ENB, speed);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    delay(time * 1000);

    // turn off the motors
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
}

void turn_left(int time, int speed)
{
    // This function will turn the car left for a certain amount of time at a certain speed
    // The speed will be a 0-100 scale and will be converted to a 0-255 scale
    // The time will be in seconds
    speedconvert(speed);
    analogWrite(ENA, speed);
    analogWrite(ENB, speed); // might have to make this a zero in order to make it work.
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, HIGH);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
    delay(time * 1000);

    // turn off the motors
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
}

void turn_right(int time, int speed)
{
    // This function will turn the car right for a certain amount of time at a certain speed
    // The speed will be a 0-100 scale and will be converted to a 0-255 scale
    // The time will be in seconds
    speedconvert(speed);
    analogWrite(ENA, speed);
    analogWrite(ENB, speed); // might have to make this a zero in order to make it work.
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, HIGH);
    delay(time * 1000);

    // turn off the motors
    analogWrite(ENA, 0);
    analogWrite(ENB, 0);
    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);
    digitalWrite(IN3, LOW);
    digitalWrite(IN4, LOW);
}