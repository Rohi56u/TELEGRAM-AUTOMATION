# Email Automation Script
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(to_email, subject, body, attachment=None):
    from_email = "your_email@gmail.com"
    password = "your_app_password"  # Use App Password for Gmail
    
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'html'))
    
    # Add attachment if provided
    if attachment:
        with open(attachment, 'rb') as f:
            attach = MIMEApplication(f.read(), _subtype="pdf")
            attach.add_header('Content-Disposition', 'attachment', 
                            filename=attachment.split('/')[-1])
            msg.attach(attach)
    
    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)
    
    print(f"✅ Email sent to {to_email}")

# Send email
send_email(
    "recipient@example.com",
    "Automated Email",
    "<h1>Hello!</h1><p>This is automated email.</p>"
)
