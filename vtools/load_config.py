import configparser
import os

from vtools import mail

def load_config(configPath=os.environ.get("HOME")+"/.vtools.conf"):
    try:
        with open(configPath) as configFile:
            configParser = configparser.ConfigParser()
            configParser.readfp(configFile)
            mail.loadConfig(configParser)
    except FileNotFoundError as er:
        print("Configuration file " + str(configPath) + " not found, fail to load config")

if __name__ == "__main__":
    load_config()
