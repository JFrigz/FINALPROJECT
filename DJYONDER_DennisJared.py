#Jared and Dennis

import time
from motor import*
from ultrasonic import*
from infrared import*
from buzzer import*
from led import*
from servo import*


led = Led() 
buzzer = Buzzer() 
infrared = Infrared()   # Create an Infrared object
PWM = Ordinary_Car()    
ultrasonic = Ultrasonic() 
servo = Servo()


def foward():
    PWM.set_motor_model(-500,-500,-500,-500)  # foward
def right():
    PWM.set_motor_model(-900,800,-900,800) #right
    servo.set_servo_pwm('0', 0)
def left():
    PWM.set_motor_model(900,-800,900,-800) #left
    servo.set_servo_pwm('0', 90)
           
def stop():
    PWM.set_motor_model(0,0,0,0) 
    for _ in range(2):
            buzzer.set_state(True)        # Turn on the buzzer
            time.sleep(0.1)               # Wait for 0.1 second
            buzzer.set_state(False)       # Turn off the buzzer
            time.sleep(0.1)
def ledshow():
        print ("colorBlink animation")
        start = time.time()
        while (time.time() - start) < 3:
            led.colorBlink(1)
try:
    while True:
        # read infrared sensor values
        rightsensor_ir = infrared.read_one_infrared(1)
        middlesensor_ir = infrared.read_one_infrared(2)
        leftsensor_ir = infrared.read_one_infrared(3)

        # read ultrasonic distance
        distance = ultrasonic.get_distance()  # Get the distance measurement in centimeters

        # display
        print(f"Ultrasonic distance: {distance}cm")  # Print the distance measurement
        print(f"Right sensor IR value: {rightsensor_ir}")
        print(f"Middle sensor IR value: {middlesensor_ir}")
        print(f"Left sensor IR value: {leftsensor_ir}")

        # if(ultrasonic.get_distance() < 30):
        #  stop()
        #  ledshow()
    

        # check conditions and control motors based on sensor readings.
        if(rightsensor_ir == 0 and middlesensor_ir == 0 and leftsensor_ir == 0):
            foward()    #forward
             
        elif(rightsensor_ir != 0 and middlesensor_ir == 0 and leftsensor_ir == 0):
             right()     #right
          
        elif(rightsensor_ir == 0 and middlesensor_ir == 0 and leftsensor_ir != 0):
            left()      #left
        
        elif(ultrasonic.get_distance() < 30):
             stop()
             ledshow()


        else:

            stop()
            ledshow()
            print("meh")  #stop
                 
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    print ("\nEnd of program")
finally:
    PWM.close()


