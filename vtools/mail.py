from configparser import NoOptionError
import smtplib  
from email.mime.text import MIMEText  # 引入smtplib和MIMEText

HOST = None
PORT = None
USERNAME = None
PASSWORD = None
SSL = None


def loadConfig(configParser):
    global HOST
    global PORT
    global USERNAME
    global PASSWORD
    global SSL

    try:
        HOST = configParser.get("mail", "host")
        PORT = configParser.get("mail", "port")
        USERNAME = configParser.get("mail", "username")
        PASSWORD = configParser.get("mail", "password")
        SSL = configParser.get("mail", "ssl")
    except NoOptionError as er:
        print("In order to use mail function, you have to ensure in the configuration file, mail section has [host, port, username, password] these 4 options")


def send(receiver, subject, text):
    global HOST
    global PORT
    global USERNAME
    global PASSWORD
    global SSL

    if HOST == None or PORT == None or USERNAME == None or PASSWORD == None or SSL == None:
        print("In order to use mail function, you have to ensure in the configuration file, mail section has [host, port, username, password] these 4 options")
        return

    msg = MIMEText(text, 'html')
    msg['subject'] = subject
    msg['from'] = USERNAME
    msg['to'] = receiver

    if SSL == "true":
        s = smtplib.SMTP_SSL(HOST, PORT)
    else:
        s = smtplib.SMTP(HOST, PORT)

    s.login(USERNAME, PASSWORD)
    s.sendmail(USERNAME, receiver, msg.as_string())
    s.quit()
    print("Sueecessfully sent to " + receiver)
