import zipfile
from os import system
import os
import shutil
import time

def write_into_file(path, x):
    with open(path, "w") as f:
        f.write(str(x))

def print_file_info(path):
  try:
    f = open(path, 'r',encoding="utf-8")
    content = f.read()
    f.close()
    return(content)
  except:
    return("ok")

def get_account_creation_date(full_file):
  data = ""
  for f in full_file:
    if "createdAt" in f:
      data = f
      continue
  data = data.split(":")[1].replace('"',"").replace(" ","")[0:10]
  return data

def get_account_data(full_file,info):
  data = ""
  for f in full_file:
    if info in f:
      data = f
      continue
  data = data.split(":")[1].replace('"',"").replace(" ","")
  return data

def unzip_file():
  current_file = ""
  list_of_files = os.listdir()
  for file in list_of_files:
     if ".zip" in file:
        current_file = file
        break
  
  os.makedirs("twitter_data", exist_ok=True)
  with zipfile.ZipFile(current_file, 'r') as zip_ref:
      zip_ref.extractall("twitter_data")

def delete_data():
   shutil.rmtree("twitter_data")