from importlib.resources import path
import os
import shutil
import time


path=input("Enter the name of the directory to be sorted:")

days=30

seconds=time.time() - (days * 24 * 60* 60)

if os.path.exists(path):
    for folder, subFolder, files in os.walk(path):
       