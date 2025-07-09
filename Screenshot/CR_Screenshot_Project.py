# once the given changes are made, this CR[Code Review] file must be deleted from the repo
import ctypes
from datetime import date,timedelta
import os ## not all the methods or classes in this module are used, hence import only the necessary ones
import pyautogui
import sys
import time ## unsued module is present here
##! Please change the default tab size to 4 spaces - right now it is 8 spaces
def stop_function(): ##provide space here to improve readbility
        '''show prompt message box''' ##docstring is not enough here: ## ALSO please download the extension: autoDocstring, it is very
        ctypes.windll.user32.MessageBoxW(0, "Projects folder is not exist in current folder path", "Info", 0x00)
        sys.exit()
def stop_function_1():
        ctypes.windll.user32.MessageBoxW(0, "day_1.txt file is not exist in current folder path", "Info", 0x00)
        sys.exit()

try: ## need not leave space after try

        files = os.listdir(os.path.join(os.path.expanduser("~"),"Documents","Projects"))
except FileNotFoundError: ## what about other possible exceptions
        stop_function()

count = 0

date =  date.today()

days_to_add = timedelta(days=15)

future_date = date + days_to_add


date = str(date)

file = "day_1.txt"

try:
        path = os.path.join(os.path.expanduser("~"),"Documents","Projects") ##NOTE: These strings here can be replaced with global variables
except FileNotFoundError:
        stop_function()

file_path = os.path.join(path,file)


try:

    f = open(file_path ,"r") ## kindly use 'with' block here isntead of using 'open' and 'close' functions

    ver = f.read()

    f.close()

except FileNotFoundError:
        stop_function_1()

if ver == date:
    f = open(file_path ,"w") ## kindly use 'with' block here isntead of using 'open' and 'close' functions
    f.write(f"{future_date}")
    f.close()
    for i in files:
        if i.endswith((".jpeg",".jpg")): ##!this is amazing ! nice use of tuples to work with the method 'endswidth' SUPERBB!!!
            os.remove(os.path.join(path,i)) ##DO NOT Chain more than 2 function calls - it is not easy to read if you do this.

files = os.listdir(os.path.join(os.path.expanduser("~"),"Documents","Projects"))
print(type(files)) ## Also include info about what you are printing
for i in files:
    if i.endswith((".jpeg",".jpg")): ## NOTE: This tuple is reused many times - better use a global variable instead
        count += 1

screenshot = pyautogui.screenshot() #take screenshot
##NOTE: These comments here: "#take screenshot"  is not required because the method used is already clear and the user can understand what is happening here
screenshot.show() #to view the screenshot image on the screen

#screenshot.save(os.path.join(os.path.expanduser("~"),"Documents","Projects",f"image_{count}.jpg")) #save the image in current path location

##NOTE: instead of chainging so much methods - seperate them into different lines# FOR E.G.:
screenshot_file_name = f"image_{count}.jpg"
screenshot_file_path = os.path.join(os.path.expanduser("~"),"Documents","Projects",)
screenshot.save(screenshot_file_path)



#SOME CORNER CASES AND ADDITIONAL TEST CASE THAT WOULD BE NICE TO COVER:
#--------------------------------------------------------------------------------
# 1. don't use "day.txt": read screenshot save date and computer's current date and take the decision to delete older images
# 2. Provide option to user to skip delete option - may be command terminal or using windows message box
# 3. have a config file to
#   => what format to save the image in?
#   => where to read and save the screenshots - right now we have hardcoded - it is best to mention in the config file
#   => how old can the screenshots be? user can alter this data to control the age of screenshot : 15days/30 days/100 days/ etc.,.
# YOU CAN READ ABOUT config files (or) .ini files
# 4. [ADVANCED] Log all the steps that the application takes - this creates a solid bug report and consoler logs -
#   the developer or the user can take a look at this log and understand what went wrong