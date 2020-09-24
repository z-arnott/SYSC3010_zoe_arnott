# Powers and reads digital output from Soil Moisture YL69 with HL69 breakout board
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#name pins
power_out = 2
digital_in = 4
button = 15
#pin setup
GPIO.setup(power_out, GPIO.OUT)
GPIO.setup(digital_in, GPIO.IN)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def check_moisture():
    GPIO.output(power_out, GPIO.HIGH)
    is_moist = GPIO.input(digital_in)
    GPIO.output(power_out, GPIO.LOW)
    return is_moist

while True:
   if GPIO.input(button):
       if check_moisture():
          print("plant is MOIST")
       else:
           print("plant is thirsty")
