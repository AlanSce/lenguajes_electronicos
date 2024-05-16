from machine import Pin
from utime import sleep

from hcsr04 import HCSR04

print("Hello, ESP32!")

ultrasonic = HCSR04(trigger_pin=14, echo_pin=12)
distance = 0; 

while True:
  distance = ultrasonic.distance_cm()
  print(distance)
  sleep(0.5)
