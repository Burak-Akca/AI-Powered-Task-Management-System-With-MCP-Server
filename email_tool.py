from typing import Any
import smtplib
from email.message import EmailMessage
import asyncio

async def send_email(to_email: str, subject: str, body: str, from_email: str, password: str) -> str:
    """
    Send an email via SMTP.

    Args:
        to_email: recipient email
        subject: email subject
        body: email body content
        from_email: sender email (SMTP login)
        password: SMTP password or app password
    """
    try:
        msg = EmailMessage()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        # Gmail SMTP server
        loop = asyncio.get_event_loop()
        def send():
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(from_email, password)
                smtp.send_message(msg)
        await loop.run_in_executor(None, send)
        return "Email sent successfully."
    except Exception as e:
        return f"Failed to send email: {e}"
