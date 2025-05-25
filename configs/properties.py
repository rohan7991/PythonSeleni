"""This module will read the data from config file"""
import configparser
import os

class AppConfig:
    def __init__(self, app_path):
        self.app = app_path
class Properties:
    config_file = AppConfig(r"configs\default_config.ini")
    config_file_path = config_file.app
    # Get the directory of the current script (root directory)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Construct the path to lib_global.py in the commons folder
    file_path = os.path.abspath(os.path.join(current_dir, '..', 'default_config.ini'))
    file_path = r"\\".join(file_path.split("\\"))
    print(file_path)
    config = configparser.ConfigParser()
    config.read(file_path)
    print(config.sections())
    print(config['Browser']['browser_type'])
    print(config['Application'])
    url = config['Application']['url']
    browser_type = config["Browser"]["browser_type"]