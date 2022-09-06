import os
import configparser

## Example
EX_VAR = "An example global var"

# Class to store settings
class prjSettings:
    
    def __init__(self):
        pass

## FILES
prj_files = prjSettings()

prj_files.dir_root  = os.path.abspath(os.path.dirname(__file__)) # Project root is defined by globalsettings.py location
prj_files.dir_data  = os.path.join(prj_files.dir_root, "data")
prj_files.dir_raw   = os.path.join(prj_files.dir_data, "raw")
prj_files.dir_clean = os.path.join(prj_files.dir_data, "clean")

prj_files.cfg_file = os.path.join(prj_files.dir_root, "config.ini")

# RAW DATA
prj_files.raw_salsas_file  = os.path.join(prj_files.dir_raw, "Lock - Salsas frias .xlsx")
prj_files.raw_airpass_file = os.path.join(prj_files.dir_raw, "AirPassengers.csv")
prj_files.raw_airqual_file = os.path.join(prj_files.dir_raw, "airquality.csv")
prj_files.raw_cars_file    = os.path.join(prj_files.dir_raw, "cars.csv")
prj_files.raw_iris_file    = os.path.join(prj_files.dir_raw, "iris.csv")
prj_files.raw_mtcars_file  = os.path.join(prj_files.dir_raw, "mtcars.csv")

# CLEAN DATA
prj_files.clean_salsas_file = os.path.join(prj_files.dir_clean, "salsas")
prj_files.all_data          = os.path.join(prj_files.dir_clean, "all_data")

## CONSTANTS
prj_const = prjSettings()

prj_const.my_pi = 3.141592

## CONFIG FILE
prj_cfg = prjSettings()

config = configparser.ConfigParser()

config.read(prj_files.cfg_file)

prj_cfg.serveraliveinterval = config['DEFAULT']['Serveraliveinterval']
prj_cfg.compression         = config['DEFAULT']['Compression']
prj_cfg.compressionlevel    = config['DEFAULT']['Compressionlevel']
prj_cfg.forwardx11          = config['DEFAULT']['Forwardx11']

## ETC