import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

#p = GPIO.PWM(21,1000)
t = GPIO.PWM(22,1000)

try:
    dc = 0
    voltage = 0
    print ("duty cycle")
    while True:
        dc = int(input())
       # p.start(dc)
        t.start(dc)
        voltage = 3.3/100 * dc
        print(voltage)

finally:
    p.stop()
    t.stop()
    GPIO.cleanup()