from time import sleep
from RPi import GPIO


GPIO.setmode(GPIO.BOARD)

pin_left_forward = 13
pin_left_reverse = 15
pin_right_forward = 16
pin_right_reverse = 18

GPIO.setup(pin_left_forward, GPIO.OUT)
GPIO.setup(pin_left_reverse, GPIO.OUT)
GPIO.setup(pin_right_forward, GPIO.OUT)
GPIO.setup(pin_right_reverse, GPIO.OUT)

pwm_left_forward = GPIO.PWM(pin_left_forward, 100)
pwm_left_reverse = GPIO.PWM(pin_left_reverse, 100)
pwm_right_forward = GPIO.PWM(pin_right_forward, 100)
pwm_right_reverse = GPIO.PWM(pin_right_reverse, 100)

pwm_left_forward.start(0)
pwm_left_reverse.start(0)
pwm_right_forward.start(0)
pwm_right_reverse.start(0)

while True:
    x = input("::::")
    if x=="w":
        print("forward")
        pwm_left_forward.ChangeDutyCycle(25)
        pwm_left_reverse.ChangeDutyCycle(0)
        pwm_right_forward.ChangeDutyCycle(25)
        pwm_right_reverse.ChangeDutyCycle(0)
    elif x=="s":
        print("reverse")
        pwm_left_forward.ChangeDutyCycle(0)
        pwm_left_reverse.ChangeDutyCycle(25)
        pwm_right_forward.ChangeDutyCycle(0)
        pwm_right_reverse.ChangeDutyCycle(25)
    elif x=="a":
        print("left")
        pwm_left_forward.ChangeDutyCycle(0)
        pwm_left_reverse.ChangeDutyCycle(25)
        pwm_right_forward.ChangeDutyCycle(25)
        pwm_right_reverse.ChangeDutyCycle(0)
    elif x=="d":
        print("right")
        pwm_left_forward.ChangeDutyCycle(25)
        pwm_left_reverse.ChangeDutyCycle(0)
        pwm_right_forward.ChangeDutyCycle(25)
        pwm_right_reverse.ChangeDutyCycle(0)
    elif x=="b":
        pwm_left_forward.ChangeDutyCycle(0)
        pwm_left_reverse.ChangeDutyCycle(0)
        pwm_right_forward.ChangeDutyCycle(0)
        pwm_right_reverse.ChangeDutyCycle(0)
        break
    else:
        pwm_left_forward.ChangeDutyCycle(0)
        pwm_left_reverse.ChangeDutyCycle(0)
        pwm_right_forward.ChangeDutyCycle(0)
        pwm_right_reverse.ChangeDutyCycle(0)
    sleep(1)

pwm_left_forward.stop()
pwm_left_reverse.stop()
pwm_right_forward.stop()
pwm_right_reverse.stop()
GPIO.cleanup()