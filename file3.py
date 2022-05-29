
import Pi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import pygame, sys
from pygame. locals import *
pygame.init()


SCREEN_SIZE = (500, 500)
screen =pygame.display.set_mode((SCREEN_SIZE))
pygame.display.set_caption('Raspberry Pi Robot Car')

# left wheel
left_wheel_pin1 = 22
left_wheel_pin2 = 23
#right wheel
right_wheel_pin3= 24
right_wheel_pin4= 25

# pin setup
GPIO.setup([left_wheel_pin1, left_wheel_pin2, right_wheel_pin3, right_wheel_pin4].GPIO.OUT)

forward = False
reverse = False
turn_left = False
turn_right = False

while True:
# event checker
    for event in pygame.event.get():
    # window close event
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == KEYDOWN:
            # forward
            if event.key == K_w:
                forward = True
            # reverse
            if event.key == K_s:
                reverse = True
            # turn left
            if event.key == K_a:
                turn_left = True
            # turn right
            if event.key == K_d:
                turn_right = True

    if event. type == KEYUP:
        forward = reverse = turn_left = turn_right = False
        GPIO.output([left_wheel_pin1, left_wheel_pin2, right_wheel_pin3, right_wheel_pin4], GPIO.LOW)


    if forward:
        GPIO.output([left_wheel_pin1, right_wheel_pin4], GPIO.LOW)
        GPIO.output([left_wheel_pin2, right_wheel_pin3], GPIO.HIGH)
        # move reverse
    if reverse:
        GPIO.output([left_wheel_pin1, right_wheel_pin4], GPIO.HIGH)
        GPIO.output([left_wheel_pin2, right_wheel_pin3]. GPIO.LOW)

    if turn_left:
        GPIO.output ([left_wheel_pin1, left_wheel_pin2, right_wheel_pin4], GPIO.LOW)
        GPIO.output (right_wheel_pin3, GPIO.HIGH)
    # turn right
    if turn_right:
        GPIO.output ([left_wheel_pin1, right_wheel_pin4, right_wheel_pin4], GPIO.LOW)
        GPIO.output (left_wheel_pin2, GPIO.HIGH)
    # update screen
    pygame.display.update()