
import imaplib
import email
from email.header import decode_header
import smtplib
from email.mime.text import MIMEText
import ollama
import pywhatkit
import time

# =========================
# CONFIG
# =========================

EMAIL_USER = "" #to which mailid the messages should come

# Gmail App Password
EMAIL_PASS = "" #this is not gmail passsword ,need to generate this 

# =========================
# EMAIL RECEIVERS
# =========================

RECEIVER_EMAILS = [
    "bs0k58f58e@bwmyga.com",# to whom the messages should be sent
    "gasefan818@deapad.com"
]

# =========================
# WHATSAPP RECEIVERS
# =========================

WHATSAPP_NUMBERS = [ 
     "+919114720220",# to which whatsapp number messages should be sent
    # "+919686462090",
]

# =========================
# CONNECT TO GMAIL
# =========================

mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login(
    EMAIL_USER,
    EMAIL_PASS
)

mail.select("inbox")

# Read latest 5 unread emails only
status, messages = mail.search(
    None,
    'UNSEEN'
)

email_ids = messages[0].split()[-5:]

print(f"\nUnread Emails Found: {len(email_ids)}")

# =========================
# PROCESS EMAILS
# =========================

for e_id in email_ids:

    _, msg_data = mail.fetch(
        e_id,
        "(RFC822)"
    )

    for response_part in msg_data:

        if isinstance(response_part, tuple):

            msg = email.message_from_bytes(
                response_part[1]
            )

            subject, encoding = decode_header(
                msg["Subject"]
            )[0]

            if isinstance(subject, bytes):

                subject = subject.decode(
                    errors="ignore"
                )

            sender = msg.get("From")

            # =========================
            # FILTER PROMOTIONAL EMAILS
            # =========================

            skip_keywords = [
                "youtube",
                "linkedin",
                "newsletter",
                "promotion",
                "offers",
                "sale",
                "job",
                "alert",
                "noreply",
                "zerodha",
                "trading",
                "statement",
                "bank",
                "invoice",
                "receipt",
                "subscription",
                "coursera",
                "n8n",
                "jewellery"
            ]

            sender_lower = sender.lower()
            subject_lower = subject.lower()

            if any(
                word in sender_lower
                for word in skip_keywords
            ):
                print("\nSkipped promotional sender")
                continue

            if any(
                word in subject_lower
                for word in skip_keywords
            ):
                print("\nSkipped promotional subject")
                continue

            # =========================
            # IT ISSUE FILTER
            # =========================

            it_keywords = [
                "laptop",
                "system",
                "issue",
                "problem",
                "error",
                "not working",
                "slow",
                "restart",
                "crash",
                "network",
                "wifi",
                "login",
                "password",
                "unable"
            ]

            if not any(
                word in subject_lower
                for word in it_keywords
            ):
                print("\nSkipped non-IT email")
                continue

            # =========================
            # EXTRACT EMAIL BODY
            # =========================

            body = ""

            if msg.is_multipart():

                for part in msg.walk():

                    try:

                        payload = part.get_payload(
                            decode=True
                        )

                        if payload:

                            body += payload.decode(
                                errors="ignore"
                            )

                    except:
                        pass

            else:

                body = msg.get_payload(
                    decode=True
                ).decode(errors="ignore")

            print("\nEMAIL RECEIVED")
            print("Subject:", subject)
            print("Sender:", sender)

            # =========================
            # AI SUMMARY USING OLLAMA
            # =========================

            prompt = f"""
Summarize this  issue professionally in one sentence.

Subject:
{subject}

Body:
{body[:1000]}
"""

            response = ollama.chat(
                model="llama3:8b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            summary = response["message"]["content"]

            print("\nSUMMARY:")
            print(summary)

            # =========================
            # SEND EMAIL NOTIFICATION
            # =========================

            alert_message = f"""
New IT Issue Detected

From:
{sender}

Subject:
{subject}

AI Summary:
{summary}
"""

            msg_email = MIMEText(
                alert_message
            )

            msg_email["Subject"] = (
                "Detected IT Issue"
            )

            msg_email["From"] = EMAIL_USER

            msg_email["To"] = ", ".join(
                RECEIVER_EMAILS
            )

            server = smtplib.SMTP_SSL(
                "smtp.gmail.com",
                465
            )

            server.login(
                EMAIL_USER,
                EMAIL_PASS
            )

            server.sendmail(
                EMAIL_USER,
                RECEIVER_EMAILS,
                msg_email.as_string()
            )

            server.quit()

            print(
                "\nEmail notification sent!"
            )

            # =========================
            # SEND WHATSAPP ALERTS
            # =========================

            whatsapp_message = f"""
Detected IT Issue

From:
{sender}

Subject:
{subject}

Summary:
{summary}
"""

            for number in WHATSAPP_NUMBERS:

                try:

                    print(
                        f"\nSending WhatsApp to {number}"
                    )

                    pywhatkit.sendwhatmsg_instantly(
                        phone_no=number,
                        message=whatsapp_message,
                        wait_time=15,
                        tab_close=True,
                        close_time=5
                    )

                    print(
                        f"WhatsApp sent to {number}"
                    )

                    time.sleep(10)

                except Exception as e:

                    print(
                        f"WhatsApp failed for {number}"
                    )

                    print(e)

            print(
                "\nWhatsApp notifications completed!"
            )

print("\nDone checking emails.")

