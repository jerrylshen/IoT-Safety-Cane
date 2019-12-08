from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = {}
auth_token = {}
client = Client(account_sid, auth_token)

phone_numbers = {}



def send_alert(url):
    for number in phone_numbers:
        message = client.messages \
                    .create(
                         body="FALL DETECTED! Maps: " + str(url),
                         from_={},
                         to=number
                         )
def send_false():
    for number in phone_numbers:
        message = client.messages \
                    .create(
                         body="FALSE ALARM",
                         from_={},
                         to=number
                         )
        