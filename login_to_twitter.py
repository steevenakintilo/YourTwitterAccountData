
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--blink-settings=imagesEnabled=false')
options.add_argument("--log-level=3")  # Suppress all logging levels

# C:\Users\your_usernema\AppData\Local\Google\Chrome\User Data
#Replace your_username with your username
#and Profile 3 by your profile number

options.add_argument(r"--user-data-dir=C:\Users\your_username\AppData\Local\Google\Chrome\User Data\Profile 3")
options.add_argument(r'--profile-directory=Profile 3')
#options.add_argument('headless')
driver = webdriver.Chrome(options=options)  # You can change this to whichever browser you prefer and have installed
username_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'  
button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div'
password_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
login_button_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div'

driver.get("https://twitter.com/i/flow/login")
time.sleep(120)