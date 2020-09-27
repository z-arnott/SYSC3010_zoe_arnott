# Read simulated ECG data from ThingSpeak channel
import requests


try:
    r = requests.get("https://api.thingspeak.com/channels/1156912/fields/2.json?api_key=W9SMONCUM7N2440D&results=2")
    print(r.status_code)
    print(r.json())
except:
    print("failed")