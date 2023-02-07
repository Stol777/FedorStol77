import smtplib
from email.mime.text import MIMEText


def send_email(message, subject):
    sender = "Bujvolisimus@yandex.ru"
    password = 'ijzzcephfwbhgyxz'
    # sender = 'ivanivanov777moscow@mail.ru'
    # password = 'yep0PXE5datKhtMrN6aN'
    # sender = 'pythonproject@rambler.ru'
    # password = '68RfYFHE3xYE@vJ'

    server = smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    # server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = subject
        server.sendmail(sender, 'deutsch2288@yandex.ru', msg.as_string())
        return "Сообщение отправлено!"

    except Exception as _ex:
        return f"{_ex}\nВозможная проблема: проверьте логин или пароль"


def main():
    subject = 'Привет!'   # input('Введите тему сообщения: ')
    message = 'Завтра в школе что-то важное'   # input('Введите сообщение: ')
    print(send_email(message, subject))


if __name__ == '__main__':
    main()









# msg = '123'
# msg = MIMEText(msg)
# print(type(msg.as_string()))
