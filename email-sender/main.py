import smtplib
from openpyxl import load_workbook


# def xls_reading():
#     wb = load_workbook('test.xlsx')


server = 'smtp.mail.ru'
user = 'ivanivanov777moscow@mail.ru'
password = '3znjDsTaav1CggTX6yPR'

with open('recipients.txt') as recipients:
    recipients = list(recipients.readline())
    sender = 'ivanivanov777moscow@mail.ru'
    msg = 'Hello world!'
    mail = smtplib.SMTP_SSL(server)
    mail.login(user, password)
    mail.sendmail(sender, recipients, msg)
    mail.quit()
