import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os
load_dotenv()

def send_welcome_message(sender_email, recipient_email, recipient_name, token):
    subject = "Welcome to Call Vibe – Stay Connected, Stay Informed!"
    body = f"""
        Hi {recipient_name.capitalize()},

        Welcome to Call Vibe! We're so excited to have you in our community.

        At Call Vibe, we believe in the power of genuine connections and vibrant conversations. Whether you're here to network, share your thoughts, or simply vibe with others, you're in the right place.

        Here’s how to get started:
        1. Set up your profile – let others know the real you.
        2. Explore and connect – find people who match your vibe.
        3. Start chatting – voice your thoughts, share your world, and enjoy the flow.

        If you ever need support, we’re just one message away.

        Stay real. Stay connected. Stay vibing.

        Please click the link below for verification:
        {token}

        Warm regards,  
        The Call Vibe Team
        """

    html = f"""
        <html>
        <body>
            <p>Hi <strong>{recipient_name.capitalize()}</strong>,</p>

            <p>Welcome to <strong>Call Vibe</strong>! We're thrilled to have you on board.</p>

            <p>Call Vibe is your space to connect, communicate, and share your vibe with like-minded people. Whether you're in it for deep convos or just light vibes, you're part of something special.</p>

            <p><strong>Here’s how to get started:</strong></p>
            <ol>
            <li><strong>Complete your profile</strong> – Show off your style and personality.</li>
            <li><strong>Explore the community</strong> – Discover others who share your interests.</li>
            <li><strong>Start a conversation</strong> – Voice chats, messages, and good vibes await.</li>
            </ol>
            <h4>
                Please click the link below for verification:
                {token}
            </h4>
            <p>If you have any questions, feel free to reach out anytime. We're here to support your journey.</p>

            <p>Keep vibing,  
            <br>The Call Vibe Team</p>
        </body>
        </html>
        """
    print(sender_email, recipient_email, recipient_name)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    body = body
    html = html
    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(html, 'html'))
  
    try:
        connection = smtplib.SMTP_SSL(host=os.getenv('EMAIL_HOST'), port=465)
        connection.ehlo()
        # connection.starttls()
        connection.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
        connection.sendmail(os.getenv('EMAIL_HOST_USER'), recipient_email, msg.as_string())
        connection.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occured while sending email: {e}")


def send_verification_message(sender_email, recipient_email, recipient_name, token):
    subject = "Verify Your Email for Call Vibe – Stay Connected!"
    
    # Plain text version of the message
    body = f"""
        Hi {recipient_name.capitalize()},
        
        Thanks for registering with Call Vibe! We’re excited to have you on board.

        To complete your registration and start using Call Vibe, please verify your email address by clicking the link below:

        Verification Code: {token}

        The request for this access originated from IP address....

        If you were not trying to sign up for Call Vibe or you did not make this request, please ignore this email.

        If you need further assistance, feel free to contact us at support@callvibe.com.

        Best regards,  
        The Call Vibe Team
    """

    # HTML version of the message
    html = f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <div style="text-align: center; margin-bottom: 20px;">
                <img src="" alt="Call Vibe Logo" style="width: 200px;"/>
            </div>
            <p>Hi <strong>{recipient_name.capitalize()}</strong>,</p>

            <p>Thanks for registering with <strong>Call Vibe</strong>! We’re excited to have you with us.</p>

            <p>To complete your registration and start using Call Vibe, please verify your email address by clicking the link below:</p>

            <h4><strong>Verification Code:</strong> {token}</h4>

            <p>The request for this access originated from IP address....</p>

            <p>If you did not make this request, please ignore this email. If you need help, feel free to contact us at <a href="mailto:support@callvibe.com">support@callvibe.com</a>.</p>

            <p><a href="{token}" style="display: inline-block; padding: 12px 20px; background-color: #0d6efd; color: white; font-size: 16px; text-decoration: none; border-radius: 5px; margin-top: 20px;">Verify Your Email</a></p>

            <p>Best regards,  
            <br>The Call Vibe Team</p>
        </body>
        </html>
    """
    print(sender_email, recipient_email, recipient_name)
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    body = body
    html = html
    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEText(html, 'html'))
  
    try:
        connection = smtplib.SMTP_SSL(host=os.getenv('EMAIL_HOST'), port=465)
        connection.ehlo()
        # connection.starttls()
        connection.login(os.getenv('EMAIL_HOST_USER'), os.getenv('EMAIL_HOST_PASSWORD'))
        connection.sendmail(os.getenv('EMAIL_HOST_USER'), recipient_email, msg.as_string())
        connection.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error occured while sending email: {e}")

# def change_password_code(sender_email, recipient_email, recipient_name, ver_code):
#     subject = "Verification code for change password"
#     body = f"""Hello {recipient_name}
#             Here is the verification code below:

#             {ver_code}
#     """

#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = recipient_email
#     body = body
#     msg.attach(MIMEText(body, 'plain'))
#     try:
#         conn = smtplib.SMTP_SSL(MAIL_SERVER)
#         conn.login(MAIL_SENDER, MAIL_PASSWORD)
#         conn.sendmail(MAIL_SENDER, recipient_email, msg.as_string())
#         conn.quit()
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Error occured while sending email: {e}")