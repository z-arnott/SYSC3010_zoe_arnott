# POST simulated ECG data to ThingSpeak channel
import requests
import time


key = "D222ZGCJNCGK29TD"

#Simulated ECG data points
data_x = [40, 38, 42, 43, 44, 45, 44, 43, 42,41, 40, 40, 40, 40, 40, 39, 42, 43, 60, 80, 100, 120, 80, 50, 5, 10, 20, 30, 40, 50, 35, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 51, 50, 49, 48, 45, 42, 40, 40]

for x in data_x:

    try:
        r = requests.post("https://api.thingspeak.com/update?api_key=D222ZGCJNCGK29TD&field1={x}")
        print (r.status_code)
    except:
        print("failed")
    # Delay next POST request for 15 seconds, min update interval on ThingSpeak
    time.sleep(15)