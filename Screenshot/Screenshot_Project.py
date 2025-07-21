import ctypes
from datetime import date,timedelta
import os
import pyautogui
import sys
from datetime import datetime
import time
import logging
import configparser
import pytz

india_timezone = pytz.timezone("Asia/Kolkata")

if getattr(sys,'frozen',False):
        file_dir = os.path.dirname(sys.executable)
else:
        file_dir = os.path.dirname(os.path.abspath(__file__))

log_file_path = os.path.join(file_dir,"screenshot_log.log")

logging.basicConfig(filename=log_file_path,level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")

#log_file_path = os.path.join(file_dir,"screenshot_log.log")

logging.info("Program start.....")

config = configparser.ConfigParser()

file_read_path = os.path.join(file_dir,"config.ini")

if not os.path.isfile(file_read_path):
    logging.error("Missing config.ini file. Application cannot continue.")
    sys.exit(1)


file_read = config.read(file_read_path)
                      
level_str_age_of_image = config.get("logging","age_of_image",fallback="-1")

level_str_age_of_image = int(level_str_age_of_image)

level_str_Delete_of_images = config.get("logging","Delete_of_images",fallback="NO").upper()



level_str_image_extension_type = config.get("logging","image_extension_type",fallback=".jpg").lower()

level_str_image_type_to_delete= config.get("logging","image_type_to_delete",fallback=".jpg").lower()

log_level_str = config.get("logging","level",fallback= "DEBUG").upper()

log_level = getattr(logging,log_level_str,logging.DEBUG)

#logging.basicConfig(filename=log_file_path,level=log_level,format="%(asctime)s - %(levelname)s - %(message)s")

def date_calculation(image_dir,image_name):
        current_date = datetime.now(india_timezone)
        timestamp_from_saved_path = os.path.getctime(image_dir)
        date_from_saved_path = datetime.fromtimestamp(timestamp_from_saved_path)
        date_from_saved_path = india_timezone.localize(date_from_saved_path)
        age_of_image_calculated = (current_date-date_from_saved_path).days
        if age_of_image_calculated == level_str_age_of_image:
                #response =  ctypes.windll.user32.MessageBoxW(0,"the age of {image_name} is {age_of_image}\nPress 'yes' if you want to delete it\nPress 'No' you want continue the screenshot process without deleting image","Info",0x04)
                if level_str_Delete_of_images == 'YES':
                        os.remove(image_dir)
                        logging.info(f"successfully deleted image:{image_name}")
                        #ctypes.windll.user32.MessageBoxW(0,f"the {image_name} is succesfully removed" , "Info", 0x00)
        


folder_list = os.listdir(file_dir)

for i in folder_list: #logic to increae the value of 'count' variable if the image is preent in current folder
        if i.endswith(level_str_image_type_to_delete):
                image_path_var =  os.path.join(file_dir,i)
                date_calculation(image_path_var,i)
#time.sleep(1)

screenshot = pyautogui.screenshot()

logging.info("screenshot was successfully taken")

screenshot.show()



time_stamp = datetime.now(india_timezone)

formating_str = time_stamp.strftime("%d-%m-%Y-%H_%M_%S")

file_saved_path = os.path.join( file_dir,f"image_{formating_str}{level_str_image_extension_type}")

logging.info(f"the saved image :image_{formating_str}{level_str_image_extension_type}")
screenshot.save(file_saved_path)
logging.info(f"screenshot was successfully saved in the {file_dir} path ")
logging.info(f"Program end....")