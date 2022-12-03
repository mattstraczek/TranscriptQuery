import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import sqlite3

driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)


# link = str(sys.argv[1])
link = "https://www.youtube.com/watch?v=yKVcDu7vv4w&ab_channel=SpaceX"
# link = "https://www.youtube.com/watch?v=vcsSc2iksC0"
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

### CLICK TRANSCRIPT BUTTON
sleep(0.5)
elements = driver.find_elements(By.TAG_NAME, 'ytd-menu-service-item-renderer')
transcript_btn_found = False

for element in elements:
    if element.find_element(By.TAG_NAME, 'yt-formatted-string').text == "Show transcript":
        element.find_element(By.TAG_NAME, 'tp-yt-paper-item').click()
        transcript_btn_found = True

transcript = []

### IF TRANSCRIPT BUTTON FOUND, CYCLE THROUGH TRANSCRIPT
if not transcript_btn_found:
    print("No transcript for this video: ", flush=True)
else:
    elements = driver.find_elements(By.TAG_NAME, 'ytd-transcript-segment-renderer')
    idx = 1
    for element in elements:
        # TIMESTAMP
        time = element.find_element(By.CSS_SELECTOR, '#segments-container > ytd-transcript-segment-renderer:nth-child(' + str(idx) + ') > div > div > div')
        # print(time.text)

        # TRANSCRIPT AT CURRENT TIMESTAMP
        curr_text = element.find_element(By.CSS_SELECTOR, '#segments-container > ytd-transcript-segment-renderer:nth-child(' + str(idx) + ') > div > yt-formatted-string')
        # print(curr_text.text)
        transcript.append((time.text, curr_text.text))
        idx += 1

# UPLOAD TRANSCRIPT TO DATABASE
con = sqlite3.connect("data/project.db") 
c = con.cursor()

# Ex: '[(0:06, Hello), (0:10, world), ...]'
transcript_val = "["
for i in range(len(transcript)):
    transcript_val += "(" + str(transcript[i][0]) + ", " + str(transcript[i][1]) + ")"
    if i != len(transcript) - 1:
        transcript_val += ", "
    else:
        transcript_val += "]"
print(transcript_val)


name = "test_name"
date_range = "test_date_range"
video_name = "test_Video_name"

c.execute('''INSERT INTO Users(ChannelName, DateRange, VideoName, Transcript) VALUES(?,?,?,?)''',(name, date_range, video_name, transcript_val))

con.commit()
c.execute("SELECT * FROM Users")
con.commit()
con.close()

#OPTIONAL?
sleep(3)

driver.quit()
