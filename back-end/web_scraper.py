from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from datetime import date
import sys

# EXTRA OPTION FOR WEBDRIVER vvv
driver_service=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=driver_service)

# HEADLESS NO BROWSER vvv
# op = webdriver.ChromeOptions()
# # op.add_argument('headless')
# op.headless = True
# driver = webdriver.Chrome('./chromedriver.exe', options=op)
# driver = webdriver.Chrome('./chromedriver.exe', options=op)

# GET CHANNEL NAME
curr_year = date.today().year #2022
# start = curr_year - 2022
# end = curr_year - 2021
link = str(sys.argv[1])
# print(sys.argv[2])
start = curr_year - int(sys.argv[2])
end = curr_year - int(sys.argv[3])
channel_url = link
# print(start)
# print(end)
# print(channel_url)
# channel_url = "https://www.youtube.com/c/SpaceX/videos"
driver.get(channel_url)
driver.implicitly_wait(1)

### GET VIDEOS BY SCROLLING
try:
    scroll_height = 10000
    element = driver.find_element(By.TAG_NAME, 'ytd-continuation-item-renderer')
    while (element):
        scroll_func = "window.scrollTo(0, " + str(scroll_height) + ");"
        driver.execute_script(scroll_func)
        scroll_height *= 2
        sleep(0.1)
        # print(element)
        element = driver.find_element(By.TAG_NAME, 'ytd-continuation-item-renderer')
    sleep(0.5)
except:
    print("All videos loaded", flush=True)

### GET VIDEO NAME AND DATE

def parseDate(date):
    # Returns 0 if released less than a year ago, else returns number of years since upload
    # Ex: 2 years ago, 2. 10 months ago, 0. 26 days ago, 0.
    date_parsed = date.split(' ')
    if date_parsed[1] == 'year' or date_parsed[1] == 'years':
        return int(date_parsed[0])
    else:
        return 0

details = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
idxs_in_range = []
i = 0
for detail in details:
    video_date = detail.find_element(By.TAG_NAME, 'ytd-video-meta-block')
    video_date = video_date.find_element(By.ID, 'metadata-line')
    video_date = video_date.find_elements(By.TAG_NAME, 'span')
    years_ago = parseDate(video_date[1].text)
    
    if (years_ago >= start and years_ago <= end):
        # video_name = detail.find_element(By.TAG_NAME, 'h3')
        # video_name = video_name.find_element(By.TAG_NAME, 'a')
        # print(video_name.get_attribute("title"))

        idxs_in_range.append(i)
        # print(video_date[1].text)
        
    i += 1

### GET ALL LINKS
elements = driver.find_elements(By.ID, 'thumbnail')   
num = 0
transcript_links = []
i = 0
for element in elements:
    link = element.get_attribute("href")

    if (link and i in idxs_in_range):
        transcript_links.append(link)
    i += 1
# print("Number of videos: " + str(len(elements) - 2), flush=True)
print(transcript_links, flush=True)
driver.quit()









############## TESTING #############

# driver.get("https://www.youtube.com/watch?v=Hb5ZXUeGPHc&ab_channel=SpaceX")
# element = 0
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "style-scope ytd-channel-name"))
#     )
# finally:
#     # for ele in element:
#     #     title = ele.find_element(By.XPATH, '//*[@id="text"]/a')
#     #     print(title)
#     # /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string
#     # /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a 
#     title = element.find_element(By.XPATH, '//*[@id="text"]/a')
#     print(title.text)
#     print(title.get_attribute("href"))
    
#     print(element)
#     driver.quit()

############## TESTING #############

    # print(element)
    # //*[@id="items"]/ytd-menu-service-item-renderer[3]/tp-yt-paper-item
# except Exception:
#     traceback.print_exc()
#     print("exception2")
#     sleep(3)
#     print("exception3")
#     driver.refresh()
    
# Click 'open transcript'
# try:
#     driver.find_element_by_xpath("//*[@id='items']/ytd-menu-service-item-renderer/tp-yt-paper-item").click()
# except:
#     sleep(3)
#     driver.refresh()

# driver.quit()
# try:
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.CLASS_NAME, "yt-spec-button-shape-next__icon"))
#     # )
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.CLASS_NAME, 'style-scope ytd-watch-metadata'))
#     # )
#     element = driver.find_element((By.CLASS_NAME, 'style-scope ytd-watch-metadata'))
#     element = element.find_element(By.ID, 'button-shape')
#     element = element.find_element(By.XPATH, '//*[@id="button-shape"]/button').click()
#     driver.implicitly_wait(10)
#     # element = driver.find_element(By.XPATH, '//*[@id="button-shape"]/button')
#     # style-scope ytd-engagement-panel-section-list-renderer
#     # yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.presence_of_element_located((By.XPATH, "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[5]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[1]/div/div/div"))
#     # )
# finally:
#     # for ele in element:
#     #     title = ele.find_element(By.XPATH, '//*[@id="text"]/a')
#     #     print(title)
#     # /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string
#     # /html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a 
    
#     # title = element.find_elements(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[1]/ytd-engagement-panel-section-list-renderer[5]/div[2]/ytd-transcript-renderer/div[2]/ytd-transcript-search-panel-renderer/div[2]/ytd-transcript-segment-list-renderer/div[1]/ytd-transcript-segment-renderer[1]/div/div/div')
#     # title = element.find_elements(By.CLASS_NAME, 'segment-timestamp style-scope ytd-transcript-segment-renderer')

#     # for t in title:
#     #     print("Individual elements")
#     #     print(t.text)
#     # print(title.text)
#     # print(title.get_attribute("href"))
    
#     print("Element")
#     print(element)
#     driver.quit()

# search = driver.find_element(by=By.NAME,value="q")

# search.send_keys("Selenium")

# search.send_keys(Keys.ENTER)
# print("Hello")

# elementSource = driver.find_element(By.CLASS_NAME, "yt-simple-endpoint style-scope yt-formatted-string")

# print(elementSource)

# print(elementSource.get_attribute("aria-label"))
# print(elementSource[0])