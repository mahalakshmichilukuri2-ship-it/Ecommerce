import smtplib
import config

try:
    server = smtplib.SMTP(
        config.MAIL_SERVER,
        config.MAIL_PORT,
        timeout=20
    )

    server.set_debuglevel(1)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(
        config.MAIL_USERNAME,
        config.MAIL_PASSWORD
    )

    print("Email connection successful!")

    server.quit()

except Exception as e:
    print("Email connection failed:", repr(e))