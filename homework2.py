from gpiozero import LED
from time import sleep

red = LED(17)
green = LED(27)
yellow = LED(22)

while True:
    red.off()
    green.on()
    yellow.on()
    sleep(5)
    red.on()
    green.off()
    yellow.on()
    sleep(5)
    red.on()
    green.on()
    yellow.off()
    sleep(2)