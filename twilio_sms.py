from twilio.rest import Client

account_sid = 'AC9b6db539daaf8adce9a1b248b8f6b97e'
auth_token = '27eb1135c85b971391b8f4dbef221b98'
twilio_phone_number = 'whatsapp:+14155238886'
your_phone_number = 'whatsapp:+16506276216'  # Your personal phone number

client = Client(account_sid, auth_token)


def trigger_emergency_call():
    call = client.calls.create(
        to=your_phone_number,
        from_=twilio_phone_number,
        url="https://handler.twilio.com/twiml/EHa01dfc4b7041f5d2145e7842c25424db"  # Sample voice message URL
    )
    print(f"Emergency call initiated: {call.sid}")


def send_sms():
    message = client.messages.create(
        body="Fire detected! Please check immediately.",
        to=your_phone_number,
        from_=twilio_phone_number
    )
    print(f"SMS sent: {message.sid}")