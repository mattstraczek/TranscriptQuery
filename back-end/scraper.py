# import requests

# url = "https://www.youtube.com/watch?v=D4xCGnwjMZQ&ab_channel=JohnWatsonRooney"
# resp = requests.get(url)

# print(resp.text)

# r = requests.request("POST", url, )
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)
link = str(sys.argv[1])
driver.get(link)
driver.implicitly_wait(10)

# CLICK SETTINGS BUTTON
try:
    element = driver.find_elements(By.XPATH, '//*[@id="button-shape"]/button')[0].click()
    # print("Click button")

except:
    print("exception")
    sleep(3)
    print("exception1")
    driver.refresh()
# print("After click settings")
# FIND 'Show transcript' BUTTON, THEN CLICK
# sleep(1)
sleep(0.5)
elements = driver.find_elements(By.TAG_NAME, 'ytd-menu-service-item-renderer')
transcript_btn_found = False
# print("Hello")
for element in elements:
    # FOUND BUTTON
    # print("Before")
    if element.find_element(By.TAG_NAME, 'yt-formatted-string').text == "Show transcript":
        # print("found")
        element.find_element(By.TAG_NAME, 'tp-yt-paper-item').click()
        # print("click")
        # sleep(3)
        transcript_btn_found = True
if not transcript_btn_found:
    print("No transcript for this video: ", flush=True)
    # driver.quit()
    # return False
else:
    elements = driver.find_elements(By.TAG_NAME, 'ytd-transcript-segment-renderer')
    idx = 1
    for element in elements:
        # timestamp
        ele = element.find_element(By.CSS_SELECTOR, '#segments-container > ytd-transcript-segment-renderer:nth-child(' + str(idx) + ') > div > div > div')
        # print(ele.text, flush=True)
        print(ele.text)
        # transcript at the current timestamp
        ele = element.find_element(By.CSS_SELECTOR, '#segments-container > ytd-transcript-segment-renderer:nth-child(' + str(idx) + ') > div > yt-formatted-string')
        # print(ele.text, flush=True)
        print(ele.text)
        idx += 1
    # print("Hello " + str(sys.argv[1]), flush=True)

#OPTIONAL
sleep(3)

driver.quit()

