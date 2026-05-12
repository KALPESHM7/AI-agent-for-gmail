# this is for testing if the agent is connecting to whatsapp
import pywhatkit

# Send message instantly

pywhatkit.sendwhatmsg_instantly(
    phone_no="+91",# should add the phone number with country code
    message="Hello from OpenClaw AI Agent!",
    wait_time=15,
    tab_close=True
)

print("WhatsApp message sent!")

