import configparser

def config_parser(config_file,tag):
    config = configparser.ConfigParser()
    config.read(config_file)
    if(tag == 'Telegram'):
        return config[tag]['token'],config[tag]['chatid']
    elif(tag == 'Arduino'):
        return config[tag]['ip'],config[tag]['port']