import configparser
import os

from vtools import mail
from vtools import cust
from vtools import proxy


def load_config(configPath=os.environ.get("HOME")+"/.vtools.conf"):
    """
    Load config from config file
    """
    try:
        with open(configPath) as configFile:
            configParser = configparser.ConfigParser()
            configParser.readfp(configFile)
            mail.load_config(configParser)
            cust.load_config(configParser)
            proxy.load_config(configParser)
    except FileNotFoundError as er:
        print("Configuration file " + str(configPath) + " not found, fail to load config")

if __name__ == "__main__":
    load_config()
