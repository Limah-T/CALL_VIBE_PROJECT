import africastalking

# Initialize Africa's Talking
africastalking.initialize(
    username='sandbox',
    api_key='atsk_9296dd1acf574ee76743287e7d9c84444acc5086e9fbf3f51ad032e30e0c8ecbda1183c0'
)

class SendSMS:
    sms = africastalking.SMS
    def send(self):
        recipients = ["+2349137230948"]
        message = "Hey Limah!\nOTP: 66785\nFor your phonenumber verification from Call Vibe\nIf you did not request for this OTP,\nKindly send a message to this email and report the case - support@callvibe.com"
        sender = "Call Vibe"  # Optional sender ID for premium accounts

        try:
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print(f"Hey, I think we've got a problem!: {e}")


