import RPi.GPIO as GPIO
import time
# GPIO2 -- trig
# GPIO3 -- echo


def checkdist():
    GPIO.output(2, GPIO.HIGH)
    time.sleep(0.000010)
    GPIO.output(2, GPIO.LOW)
    while not GPIO.input(3):
        pass
    t1 = time.time()
    while GPIO.input(3):
        pass

    t2 = time.time()
    return (t2-t1)*340/2


if __name__ == '__main__':
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(2, GPIO.OUT, initial=GPIO.LOW)
	GPIO.setup(3, GPIO.IN)

    time.sleep(2)
    try:
        while True:
            print "Distance: %0.2f m" % checkdist()
            time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.cleanup()
