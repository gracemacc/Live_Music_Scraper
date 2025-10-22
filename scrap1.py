from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

profile_path = "/Users/grace.macneil/Local_Band_Scraper/profile_data"

#Configure the Browser
chrome_options = Options()
#access saved login cookies and session data
chrome_options.add_argument(f"user-data-dir={profile_path}")#one time manual login will get saved
driver = webdriver.Chrome(options=chrome_options)

#Navigate to Target URL (Facebook)
target_url = 'https://www.facebook.com/'
print(f"Opening browser and navigating to: {target_url}")
driver.get(target_url)
time.sleep(60) #give time to login
print(f"Page Title is: {driver.title}")#confirm correct page loaded
#Close Browser
driver.quit()
print("Browser closed. Setup check complete!")