import time
import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


PORT = 3
FREQUENCY = 96000000

MAX = 40
MIN = 0

def percent(x: float) -> float:
    return x * (MAX - MIN)


GPIO.setup(PORT, GPIO.OUT)
t1 = GPIO.PWM(PORT, FREQUENCY)


def calibrate():
    print("calibrating")
    t1.start(MIN)
    t1.ChangeDutyCycle(percent(10))
    time.sleep(3)

    t1.ChangeDutyCycle(MAX)
    time.sleep(3)
    t1.ChangeDutyCycle(percent(10))
    t1.ChangeDutyCycle(MIN) 
    time.sleep(3)

    print("Calibration complete.... maybe")


def startup():
    t1.start(0)
    
    t1.ChangeDutyCycle(MAX)
    time.sleep(1)
    t1.ChangeDutyCycle(MIN)
    time.sleep(1)
    
    t1.ChangeDutyCycle(percent(20))

startup()
calibrate()

while True:
    x = input("Enter a number between 0 and MAX or 'q' to quit: ")
    if x == 'q':
        break
    t1.ChangeDutyCycle(int(x))
    time.sleep(1)


t1.stop()
GPIO.cleanup()
