import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

portNo = 23
portlist = [17, 27, 22, 23, 24, 25]
portlist2 = [23, 24, 25]
portlist3 = [17, 27, 22]


def run():
    for port in portlist:
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.LOW)
        time.sleep(20)
        GPIO.output(port, GPIO.HIGH)


def stop():
    for port in portlist:
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.HIGH)

def runPort(port):
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.LOW)

def stopPort(port):
        GPIO.setup(port, GPIO.OUT)
        GPIO.output(port, GPIO.HIGH)
# LEFT_BTN_PIN = 13
# LEFT_PIN_BOUNCE = 1000

# RIGHT_BTN_PIN = 5
# RIGHT_PIN_BOUNCE = 2000

# # configure interrups for buttons
# GPIO.setup(LEFT_BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# GPIO.setup(RIGHT_BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# def left_btn(ctx):
#     for port in portlist2:
#         GPIO.setup(port, GPIO.OUT)
#         GPIO.output(port, GPIO.LOW)
#         time.sleep(2)
#         GPIO.output(port, GPIO.HIGH)

# def right_btn(ctx):
#     for port in portlist2:
#         GPIO.setup(port, GPIO.OUT)
#         GPIO.output(port, GPIO.LOW)
#         time.sleep(2)
#         GPIO.output(port, GPIO.HIGH)

# GPIO.add_event_detect(LEFT_BTN_PIN, GPIO.FALLING, callback=left_btn, bouncetime=LEFT_PIN_BOUNCE)
# GPIO.add_event_detect(RIGHT_BTN_PIN, GPIO.FALLING, callback=right_btn, bouncetime=RIGHT_PIN_BOUNCE)

port = 25
try:
    while True:
        #runPort(port)
        #time.sleep(20)
        #stopPort(port)
        run()
except KeyboardInterrupt:
    #stopPort(port)
    stop()
    print('interrupted!')
