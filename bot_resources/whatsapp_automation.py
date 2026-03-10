# WhatsApp Automation Bot
import pywhatkit as kit
from datetime import datetime

# Send instant message
kit.sendwhatmsg_instantly(
    phone_no="+919876543210",
    message="Hello from Python!",
    wait_time=10
)

# Schedule message
kit.sendwhatmsg("+919876543210", "Scheduled message", 15, 30)

# Send image
kit.sendwhats_image("+919876543210", "image.png", "Check this out!")

print("✅ Messages sent successfully!")
