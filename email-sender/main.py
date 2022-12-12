import smtplib

server = 'smtp.mail.ru'
user = 'ivanivanov777moscow@mail.ru'
password = '3znjDsTaav1CggTX6yPR'

f = open("recipients.txt", 'r')
recipients = open('recipients.txt').readline()
# sender = 'ivanivanov777moscow@mail.ru'
# msg = 'Hello world!'
# mail = smtplib.SMTP_SSL(server)
# mail.login(user, password)
# mail.sendmail(sender, recipients, msg)
# mail.quit()

