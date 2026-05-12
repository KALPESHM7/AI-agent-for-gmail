
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

EMAIL_USER = "appukalpesh@gmail.com"

# Gmail App Password
EMAIL_PASS = "tpwcxkrbdiwzkhfe"

# =========================
# EMAIL RECEIVERS
# =========================

RECEIVER_EMAILS = [
    "gasefan818@deapad.com",
    "s58dt3shj7@bwmyga.com"
]

# =========================
# WHATSAPP RECEIVERS
# =========================

WHATSAPP_NUMBERS = [
    "+917795764180",
    "+919114720220",
    "+919686462090",
    "+919686765247",
    "+919686906360"
]

# =========================
# CONNECT TO GMAIL
# =========================

mail = imaplib.IMAP4_SSL("imap.gmail.com")

mail.login(EMAIL_USER, EMAIL_PASS)

mail.select("inbox")

# Read latest 5 unread emails only
status, messages = mail.search(None, 'UNSEEN')

email_ids = messages[0].split()[-5:]

print(f"\nUnread Emails Found: {len(email_ids)}")

# =========================
# PROCESS EMAILS
# =========================

for e_id in email_ids:

    _, msg_data = mail.fetch(e_id, "(RFC822)")

    for response_part in msg_data:

        if isinstance(response_part, tuple):

            msg = email.message_from_bytes(
                response_part[1]
            )

            subject, encoding = decode_header(
                msg["Subject"]
            )[0]

            if isinstance(subject, bytes):

                subject = subject.decode()

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
                "password"
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
Summarize this IT issue professionally in one sentence.

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

            print("\nAI SUMMARY:")
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

            msg_email = MIMEText(alert_message)

            msg_email["Subject"] = (
                " Detected IT Issue"
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
AI Detected IT Issue

Subject:
{subject}

Summary:
{summary}
"""

            for number in WHATSAPP_NUMBERS:

                print(
                    f"\nSending WhatsApp to {number}"
                )

                pywhatkit.sendwhatmsg_instantly(
                    phone_no=number,
                    message=whatsapp_message,
                    wait_time=15,
                    tab_close=True
                )

                time.sleep(10)

            print(
                "\nWhatsApp notifications sent!"
            )

print("\nDone checking emails.")

