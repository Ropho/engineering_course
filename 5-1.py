import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]

comp = 4

troyka = 17

GPIO.setup (dac, GPIO.OUT)

GPIO.setup (troyka, GPIO.OUT, initial = GPIO.HIGH)

GPIO.setup (comp, GPIO.IN)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]


def adc():
    for i in range(256):
        GPIO.output (dac, dec2bin(i))
        time.sleep(0.001)
        if (GPIO.input(comp) == 0):
            break
    return i

try:
    while (1):
        v = adc ()
        volt = v * 3.3 / 256
        print(dec2bin(v), v, " ", volt)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()