import RPi.GPIO as GPIO
import time

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

TIME_STEP = 0.5


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)


def stop(sleep_time):
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)
    time.sleep(sleep_time)
    GPIO.cleanup()


def ahead(sleep_time):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.cleanup()


def back(sleep_time):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(sleep_time)
    GPIO.cleanup()


def right(sleep_time):
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    time.sleep(sleep_time)
    GPIO.cleanup()


def left(sleep_time):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)
    time.sleep(sleep_time)
    GPIO.cleanup()

# operations
OPS = {
    'w': ahead,
    's': back,
    'a': left,
    'd': right,
    'p': stop,
    'q': None,
}

def move(op):
    init()
    OPS[op](TIME_STEP)

def cli():
    while(True):
        op = raw_input("enter command:")
        if(op != 'q'):
            move(op)
        else:
            print "byby"
            break

def main():
    while(True):
        op = raw_input("go or die?\n")
        if op == "go":
            cli()
        else:
            return

if __name__ == '__main__':
    main()
