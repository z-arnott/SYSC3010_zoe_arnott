# Powers and reads digital output from Soil Moisture YL69 with HL69 breakout board
# Sensor is active low: 0 when soil moisture is above threshold, 1 when soil moisture is below threshold
import RPi.GPIO as GPIO
import time
import httplib
import urllib

key = "D222ZGCJNCGK29TD"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# name pins
power_out = 2
digital_in = 4
button = 15
# pin setup
GPIO.setup(power_out, GPIO.OUT)
GPIO.setup(digital_in, GPIO.IN)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def check_moisture():
    GPIO.output(power_out, GPIO.HIGH)
    time.sleep(0.1)
    is_moist = GPIO.input(digital_in)
    GPIO.output(power_out, GPIO.LOW)
    return is_moist


while True:
    if GPIO.input(button):
        moisture = check_moisture()
        print(moisture)
        param = urllib.urlencode({'field1': moisture, 'key':key})
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", param)
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        # delay 100 ms to prevent duplicate button presses
        time.sleep(0.1)