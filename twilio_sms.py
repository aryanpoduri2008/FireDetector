from twilio.rest import Client

account_sid = 'AC9b6db539daaf8adce9a1b248b8f6b97e'
auth_token = '7282b9a408a17a148f4b3a3b2712a695'
twilio_phone_number = '8338979791'
your_phone_number = '6506276216'  # Your personal phone number

client = Client(account_sid, auth_token)


def trigger_emergency_call():
    call = client.calls.create(
        to=your_phone_number,
        from_=twilio_phone_number,
        url="http://demo.twilio.com/docs/voice.xml"  # Sample voice message URL
    )
    print(f"Emergency call initiated: {call.sid}")


def send_sms():
    message = client.messages.create(
        body="Fire detected! Please check immediately.",
        to=your_phone_number,
        from_=twilio_phone_number
    )
    print(f"SMS sent: {message.sid}")