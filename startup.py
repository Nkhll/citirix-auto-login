from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import glob
""" import config  # Import the config file """
import config_local

config = config_local

chrome_options = Options()
driver = webdriver.Chrome()

# Open the website
driver.get(config.login_url)

# Wait for the page to load
time.sleep(10)

# Find and fill the username field
username = driver.find_element(By.ID, "login")
username.send_keys(config.username)

# Find and fill the password field
password = driver.find_element(By.ID, "passwd")
password.send_keys(config.password)

# Find and click the login button
login_button = driver.find_element(By.ID, "loginBtn")
login_button.click()

# Wait for a while to see the result

desktop_access_button = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CLASS_NAME, "wica")))
time.sleep(0.2)
desktop_access_button.click()

""" time.sleep(20)
desktop_access_button = driver.find_element(By.CLASS_NAME, 'wica')
desktop_access_button.click() """

time.sleep(12)
authorized_access_button = driver.find_element(By.LINK_TEXT, 'OK')
authorized_access_button.click()

time.sleep(15)
download_desktop_button = driver.find_element(By.CLASS_NAME, 'storeapp-details-link')
download_desktop_button.click()

time.sleep(12)

# Identify the most recently downloaded file
download_dir = config.download_dir
list_of_files = glob.glob(os.path.join(download_dir, '*.ica'))
latest_file = max(list_of_files, key=os.path.getctime)
print(f"Downloaded file: {latest_file}")

# Open the downloaded file
os.startfile(latest_file)

time.sleep(10)
# Close the browser
driver.quit()
