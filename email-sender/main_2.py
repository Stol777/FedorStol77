import smtplib
from email.mime.text import MIMEText


def send_email(message):
    sender = "sender@yandex.ru"
    password = 'qwerty123'

    server = smtplib.SMTP("smtp.yandex.ru", 465)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Тема сообщения"
        server.sendmail(sender, sender, msg.as_string())
        return "Сообщение отправлено!"

    except Exception as _ex:
        return f"{_ex}\nПроверьте логин или пароль!"
