
import os

import ctypes

import time

import sys

#time.sleep(10)
temp = ""

def check_folder_path_exist():
    if not os.path.exists(r"C:\Users\Shanmugam\Documents\Projects\WallaPaper"):
        ctypes.windll.user32.MessageBoxW(0, "Wallpaper folder was not presented on this path\nplease can you check it!", "Error", 0x10)
def stop_function():
        ctypes.windll.user32.MessageBoxW(0, "Stopped the wallpaper changing successfully", "Info", 0x00)
        sys.exit()

check_folder_path_exist()

file_path = os.path.join(os.path.expanduser("~"),"Documents","Projects","WallaPaper")

file_extension = ('.jpg', '.jpeg', '.png','.webp','.gif','.bmp','.avif')

lis_dir = os.listdir(file_path)

lis_dir.sort()

while temp == "":

    if os.path.exists(r"C:\Users\Shanmugam\Documents\Projects\WallaPaper\stop.txt"):  # Choose any location you like
        stop_function()
       # break
      
    try:
        for i in lis_dir:
            if os.path.exists(r"C:\Users\Shanmugam\Documents\Projects\WallaPaper\stop.txt"):  # Choose any location you like
                stop_function()
                #break
            for j in file_extension:
                if os.path.exists(r"C:\Users\Shanmugam\Documents\Projects\WallaPaper\stop.txt"):  # Choose any location you like
                    stop_function()
                    #break
                if i.lower().endswith(j):
                    temp_wallpaper = os.path.join(file_path,i)
                    ctypes.windll.user32.SystemParametersInfoW(20,0,temp_wallpaper ,3)
                    time.sleep(5)
    except FileNotFoundError:
        check_folder_path_exist()