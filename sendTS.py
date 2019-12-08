import readTS
import http.client
import urllib
import time
# Our ThingSpeak API Key: 
key = {}

def sendGPS(lat, long):
    
    #Calculate CPU temperature of Raspberry Pi in Degrees C
    #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
    params1 = urllib.parse.urlencode({'field1': lat, 'field2':long, 'key':key })
    #params2 = urllib.parse.urlencode({'field2': long, 'key':key }) 
    headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = http.client.HTTPConnection("api.thingspeak.com:80")
    try:
        conn.request("POST", "/update", params1, headers)
        #conn.request("POST", "/update", params2, headers)
        response = conn.getresponse()
        print(response.status, response.reason)
        #data = response.read()
        
        #conn.request("POST", "/update", params2, headers)
        #conn.request("POST", "/update", params2, headers)
        #response = conn.getresponse()
        #print(response.status, response.reason)
        #data = response.read()
        

    except:
        print("connection failed")
    conn.close()
