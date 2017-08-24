TYPE = None
HOST = None
PORT = None

def load_config(configParser):
    global TYPE
    global HOST
    global PORT

    try:
        TYPE = configParser.get("proxy", "type")
        HOST = configParser.get("proxy", "host")
        PORT = configParser.get("proxy", "port")
    except NoOptionError as er:
        pass
