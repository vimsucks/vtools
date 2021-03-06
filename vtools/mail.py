from configparser import NoOptionError
import smtplib
import socks
from email.mime.text import MIMEText  # 引入smtplib和MIMEText
from vtools import proxy

HOST = None
PORT = None
USERNAME = None
PASSWORD = None
SSL = None
SUBJECT_PREFIX = None
USE_PROXY = None
PROXY_TYPE_CODE = {
    "socks5": socks.SOCKS5,
    "socks4": socks.SOCKS4,
    "http": socks.HTTP
}


def load_config(configParser):
    """
    Load mail config
    """
    global HOST
    global PORT
    global USERNAME
    global PASSWORD
    global SSL
    global SUBJECT_PREFIX
    global USE_PROXY

    # those options are required
    try:
        HOST = configParser.get("mail", "host")
        PORT = configParser.get("mail", "port")
        USERNAME = configParser.get("mail", "username")
        PASSWORD = configParser.get("mail", "password")
        SSL = configParser.get("mail", "ssl")
        USE_PROXY = configParser.get("mail", "use_proxy")
    except NoOptionError as er:
        print("In order to use mail function, you have to ensure in the configuration file, mail section has [host, port, username, password] these 4 options")

    # those are optional
    try:
        SUBJECT_PREFIX = configParser.get("mail", "subject_prefix")
    except NoOptionError as er:
        pass


def send(receiver, subject, text):
    global HOST
    global PORT
    global USERNAME
    global PASSWORD
    global SSL
    global SUBJECT_PREFIX
    global USE_PROXY
    global PROXY_TYPE_CODE

    if HOST == None or PORT == None or USERNAME == None or PASSWORD == None:
        print("In order to use mail function, you have to ensure in the configuration file, mail section has [host, port, username, password] these 4 options")
        return

    if USE_PROXY == "true":
        socks.set_default_proxy(PROXY_TYPE_CODE[proxy.TYPE], proxy.HOST, int(proxy.PORT))
        socks.wrapmodule(smtplib)



    msg = MIMEText(text, 'html')
    if SUBJECT_PREFIX != None:
        msg['subject'] = SUBJECT_PREFIX + " " + subject
    else:
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
