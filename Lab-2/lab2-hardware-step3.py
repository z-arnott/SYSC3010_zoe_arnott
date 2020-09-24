# Powers and reads digital output from Soil Moisture YL69 with HL69 breakout board
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#name pins
power_out = 2
digital_in = 4
button = 15

#pin setup
GPIO.setup(2, GPIO.OUT)
GPIO.setup(4, GPIO.IN)
GPIO.setup(15, GPIO.IN)


def check_moisture():
    GPIO.output(power_out, HIGH)
    return GPIO.input(digital_in, HIGH)

while true:
    # button is active low
    if not GPIO.input(button):
        if check_moisture():
            #send to "plant is happy" to thingspeak
        else:
            #send water your plant to thingspeak
