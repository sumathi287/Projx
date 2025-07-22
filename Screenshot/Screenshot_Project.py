import ctypes
from datetime import date, timedelta
import os
import pyautogui
import sys
from datetime import datetime

# import time
import logging
import configparser
import pytz

india_timezone = pytz.timezone(
    "Asia/Kolkata"
)  # convert to a specific timezone("Asia/Kolkata")
if getattr(
    sys, "frozen", False
):  # execute if block if we run the scrippt by operating system directly (Windows) (note:without using any source code or IDE's)
    file_dir = os.path.dirname(sys.executable)
else:  # executing else block if we run the script using IDEs
    file_dir = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(file_dir, "screenshot_log.log")
# set up logging with specific configuration
logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logging.info("Program start.....")
config = configparser.ConfigParser()
file_read_path = os.path.join(file_dir, "config.ini")
if not os.path.isfile(
    file_read_path
):  # check if the "config.ini" file path is existing or not in script location
    logging.error("Missing config.ini file. Application cannot continue.")
    sys.exit(1)
file_read = config.read(
    file_read_path
)  # file_read_path -> is path of "config.ini" file

level_str_age_of_image = config.get("logging", "age_of_image", fallback="-1")

level_str_age_of_image = int(level_str_age_of_image)

level_str_Delete_of_images = config.get(
    "logging", "Delete_of_images", fallback="NO"
).upper()

level_str_image_extension_type = config.get(
    "logging", "image_extension_type", fallback=".jpg"
).lower()

level_str_image_type_to_delete = config.get(
    "logging", "image_type_to_delete", fallback=".jpg"
).lower()
log_level_str = config.get("logging", "level", fallback="DEBUG").upper()
# get the value of an attribute of an object by name (as a string).
log_level = getattr(logging, log_level_str, logging.DEBUG)
# set up logging with specific configuration
logging.basicConfig(
    filename=log_file_path,
    level=log_level,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def date_calculation(image_dir, image_name):
    """
       Calculate the number of days between two date objects
       Delete the image object (specfic extention:selected by user)if the calculated days is match with user input
    Args:
        image_dir(str): here i use the absolute path to access the folder path for image to deleting process
        image_name(str):(.JPEG, .PNG, .GIF, .TIFF, .WebP, .SVG, .BMP, and .HEIF)

    Returns:
        None
    """
    current_date = datetime.now(india_timezone)
    timestamp_from_saved_path = os.path.getctime(
        image_dir
    )  # to get Raw timestamp (timestamp (a float) - the number of seconds since the Unix epoch (Jan 1, 1970).)
    date_from_saved_path = datetime.fromtimestamp(
        timestamp_from_saved_path
    )  # convert Raw timestamp to readable timestamp
    date_from_saved_path = india_timezone.localize(
        date_from_saved_path
    )  # convert to India Standard Time (IST)
    age_of_image_calculated = (
        current_date - date_from_saved_path
    ).days  # number of days between two date objects (date of object_image and current date)
    if age_of_image_calculated == level_str_age_of_image:
        if level_str_Delete_of_images == "YES":
            os.remove(image_dir)
            logging.info(
                f"successfully deleted image:{image_name}"
            )  # logging message about to represent deleted image name


folder_list = os.listdir(file_dir)

# logic to identify the extention type of objects(images) from the script location and call the function with passing arg:send the object location ,object name to deleting process
for i in folder_list:
    if i.endswith(level_str_image_type_to_delete):
        image_path_var = os.path.join(file_dir, i)
        date_calculation(image_path_var, i)
screenshot = pyautogui.screenshot()
logging.info("screenshot was successfully taken")
screenshot.show()
time_stamp = datetime.now(india_timezone)
formating_str = time_stamp.strftime("%d-%m-%Y-%H_%M_%S")
file_saved_path = os.path.join(
    file_dir, f"image_{formating_str}{level_str_image_extension_type}"
)
logging.info(
    f"the saved image name :image_{formating_str}{level_str_image_extension_type}"
)
screenshot.save(file_saved_path)
logging.info(f"screenshot was successfully saved in the {file_dir} path ")
logging.info(f"Program end....")
