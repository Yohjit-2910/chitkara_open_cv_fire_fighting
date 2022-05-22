import cv2         # Library for openCV
import threading 
import RPi.GPIO as GPIO          
from time import sleep

fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml') 
vid = cv2.VideoCapture(1) 
runOnce = False 

fire_present = False
x_of_fire = None

while(True):
    Alarm_Status = False
    ret, frame = vid.read() 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # To convert frame into gray color
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5) # to provide frame resolution

    ## to highlight fire with square 
    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # print("Fire alarm initiated")
       

        if runOnce == False:
            # print("We found Fire")
            x_of_fire = x
            fire_present = True
            runOnce = True
        if runOnce == True:
            # print("Fire's still there ")
            fire_present = True
            x_of_fire = x
            runOnce = True

    fire_present = False

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# in1 = 24
# in2 = 23
# en = 25
# temp1=1

left_wheel_pin1 = 22
left_wheel_pin2 = 23
right_wheel_pin3 = 24
right_wheel_pin4 = 25

GPIO.setup([left_wheel_pin1,left_wheel_pin2,right_wheel_pin3,right_wheel_pin4], GPIO.OUT)

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(in1,GPIO.OUT)
# GPIO.setup(in2,GPIO.OUT)
# GPIO.setup(en,GPIO.OUT)
# GPIO.output(in1,GPIO.LOW)
# GPIO.output(in2,GPIO.LOW)
# p=GPIO.PWM(en,1000)
# p.start(50)
# print("\n")
# print("The default speed & direction of motor is LOW & Forward.....")
# print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
# print("\n")    

while(1):

    # x=raw_input()
    
   
    if(x_of_fire > 400 and x_of_fire < 800):
        # GPIO.output(in1,GPIO.HIGH)
        # GPIO.output(in2,GPIO.LOW)
        GPIO.output([left_wheel_pin1, right_wheel_pin4], GPIO.LOW)
        GPIO.output([left_wheel_pin2, right_wheel_pin3], GPIO.HIGH) 
        print("forward")
        # x='z'

    elif fire_present == False:
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        # x='z'

    elif (x_of_fire >= 800):
        print("right")
        GPIO.output([left_wheel_pin1, right_wheel_pin3, right_wheel_pin4], GPIO.LOW)
        GPIO.output(left_wheel_pin2, GPIO.HIGH) 
        # GPIO.output(in1,GPIO.HIGH)
        # GPIO.output(in2,GPIO.LOW)
        # temp1=1
        # x='z'

    elif (x_of_fire <= 400):
        print("left")
        GPIO.output([left_wheel_pin1, left_wheel_pin2, right_wheel_pin4], GPIO.LOW)
        GPIO.output(right_wheel_pin3, GPIO.HIGH) 
        # GPIO.output(in1,GPIO.LOW)
        # GPIO.output(in2,GPIO.HIGH)
        # temp1=0
        # x='z'

    
    
    