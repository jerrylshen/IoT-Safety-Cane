import sendSMS
import urllib.request, json
READ_API_KEY={}
CHANNEL_ID=926596
def sendURL():
    conn = urllib.request.urlopen("http://api.thingspeak.com/channels/%s/feeds/last.json?api_key=%s" \
                           % (CHANNEL_ID,READ_API_KEY))

    response = conn.read()
    print("http status code=%s" % (conn.getcode()))
    data=json.loads(response)
    lat = data['field1'] # data['created_at'])
    lng = data['field2'] # data['created_at'])
    url_string = "http://www.google.com/maps/place/{},{}".format(lat,lng)
    #return url_string
    sendSMS.send_alert(url_string)
    
    
    


    conn.close()
