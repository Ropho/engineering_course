import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
clean_bin = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.setup (dac, GPIO.OUT)

def dec2bin(n):
    return [int(i) for i in bin(n)[2:].zfill(8)]


def prob_out(binary):
    s = 0
    for i in range(7, -1, -1):
        s += binary[i] * 2**(7 - i)
    return s * (3.3/256)

try:
    while (1):
        letter = (input("Введите число для ЦАП: "))
                
        if letter == "q":
            break
        
        try:    
            letter = int(letter)

            if letter < 0:
                print ("отрицательное число")
                break
            if letter > 255:
                print ("слишком большое")
                break

            binary = dec2bin(letter)

        except ValueError:
            print ("неверный тип")

        else:
        
            GPIO.output(dac, binary)
            print(binary)
            print ("НАПРЯГА:", "{:.4}".format(prob_out(binary)))
        
        
        


finally:
    GPIO.output (dac, 0)
    # time.sleep (1000)
    GPIO.cleanup ()