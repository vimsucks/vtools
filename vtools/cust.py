import requests
from pyquery import PyQuery

USERNAME = None
PASSWORD = None

def load_config(configParser):
    global USERNAME
    global PASSWORD

    try:
        USERNAME = configParser.get("cust", "username")
        PASSWORD = configParser.get("cust", "password")
    except NoOptionError as er:
        pass

def get_login_session(username=None, password=None):
    global USERNAME
    global PASSWORD

    if username == None or password == None:
        username = USERNAME
        password = PASSWORD

    session = requests.Session()
    __VIEWSTATE = "/wEPDwUJMTQyNDg3OTM5ZGQ="
    __EVENTVALIDATION = "/wEWBAK4vfWFDAKl1bKzCQK1qbSWCwKM54rGBg=="
    LOGIN_URL = 'http://jwgl.cust.edu.cn/teachwebsl/login.aspx'
    session.post(LOGIN_URL, {
        "__VIEWSTATE": __VIEWSTATE,
        "__EVENTVALIDATION": __EVENTVALIDATION,
        "txtUserName": username,
        "txtPassWord": password,
        "Button1": "登录"
    })
    return session

def get_login_response(username=None, password=None):
    global USERNAME
    global PASSWORD

    if username == None or password == None:
        username = USERNAME
        password = PASSWORD

    session = requests.Session()
    __VIEWSTATE = "/wEPDwUJMTQyNDg3OTM5ZGQ="
    __EVENTVALIDATION = "/wEWBAK4vfWFDAKl1bKzCQK1qbSWCwKM54rGBg=="
    LOGIN_URL = 'http://jwgl.cust.edu.cn/teachwebsl/login.aspx'
    return session.post(LOGIN_URL, {
        "__VIEWSTATE": __VIEWSTATE,
        "__EVENTVALIDATION": __EVENTVALIDATION,
        "txtUserName": username,
        "txtPassWord": password,
        "Button1": "登录"
    })

def validate_login(session):
    INDEX_URL = "http://jwgl.cust.edu.cn/teachweb/index1.aspx"
    index_html = session.get(INDEX_URL).text
    doc = PyQuery(index_html)
    if len(doc("#StudentNameValueLabel")) != 0:
        return (True, doc("#StudentNameValueLabel").text())
    else:
        return (False, None)

def get_viewstate_and_eventvalidation():
    LOGIN_URL = 'http://jwgl.cust.edu.cn/teachwebsl/login.aspx'
    login_html = requests.get(LOGIN_URL).text
    doc = PyQuery(login_html)
    __VIEWSTATE = doc("#__VIEWSTATE").attr("value")
    __EVENTVALIDATION = doc("#__EVENTVALIDATION").attr("value")
    return (__VIEWSTATE, __EVENTVALIDATION)
