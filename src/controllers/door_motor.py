# python imports
from time import sleep

# Gpio imports
import RPi.GPIO as GPIO

# custom imports
from utils.constants import OPEN_VALUE, CLOSE_VALUE

# constants
SERVO_PIN = 17
GHZ = 50

# gpio config
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

def open_door(time = 0.1):
  servo = GPIO.PWM(SERVO_PIN, GHZ)
  servo.start(CLOSE_VALUE)
  sleep(time)
  servo.ChangeDutyCycle(OPEN_VALUE)
  sleep(time)
  servo.stop()

def close_door(time = 0.1):
  servo = GPIO.PWM(SERVO_PIN, GHZ)
  servo.start(OPEN_VALUE)
  sleep(time)
  servo.ChangeDutyCycle(CLOSE_VALUE)
  sleep(time)
  servo.stop()