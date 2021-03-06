# POST student information to Lab Thingspeak channel
import httplib
import urllib

cmail = "zoe.arnott@carleton.ca"
project_group = "L2-M-3"
identifier = "b"
key = "54CDA6FJF4RCJ92C"

params = urllib.urlencode({'field1': cmail, 'key':key, 'field2':project_group, 'field3':identifier})
conn = httplib.HTTPConnection("api.thingspeak.com:80")
try:
    conn.request("POST", "/update", params)
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data)
    conn.close()
except:
    print("connection failed")

