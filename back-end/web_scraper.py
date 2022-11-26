from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# EXTRA OPTION FOR WEBDRIVER vvv
driver_service=Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=driver_service)
driver2 = webdriver.Chrome(service=driver_service)

# HEADLESS NO BROWSER vvv
# op = webdriver.ChromeOptions()
# # op.add_argument('headless')
# op.headless = True
# driver = webdriver.Chrome('./chromedriver.exe', options=op)
# driver2 = webdriver.Chrome('./chromedriver.exe', options=op)

def getTranscript(link):
    # GET CHANNEL NAME
    # driver.get("https://www.youtube.com/watch?v=Hb5ZXUeGPHc&ab_channel=SpaceX")
    
    driver.get(link)
    driver.implicitly_wait(3)

    # CLICK SETTINGS BUTTON
    try:
        element = driver.find_elements(By.XPATH, '//*[@id="button-shape"]/button')[0].click()
        
    except:
        print("exception")
        sleep(3)
        print("exception1")
        driver.refresh()

    # FIND 'Show transcript' BUTTON, THEN CLICK
    elements = driver.find_elements(By.TAG_NAME, 'ytd-menu-service-item-renderer')
    transcript_btn_found = False
    for element in elements:
        # FOUND BUTTON
        if element.find_element(By.TAG_NAME, 'yt-formatted-string').text == "Show transcript":
            element.find_element(By.TAG_NAME, 'tp-yt-paper-item').click()
            transcript_btn_found = True
    if not transcript_btn_found:
        print("No transcript for this video: " + link, flush=True)
        # driver.quit()
        return False

    # GO THROUGH TRANSCRIPT
    # elements = driver.find_elements(By.TAG_NAME, 'ytd-transcript-segment-renderer')
    # idx = 1
    # for element in elements:
    #     # timestamp
    #     ele = element.find_element(By.CSS_SELECTOR, '#segments-container > ytd-transcript-segment-renderer:nth-child(' + str(idx) + ') > div > div > div')
    #     # print(ele.text, flush=True)
    #     print(ele.text)
    #     # transcript at the current timestamp
    #     ele = element.find_element(By.CSS_SELECTOR, '#segments-container > ytd-transcript-segment-renderer:nth-child(' + str(idx) + ') > div > yt-formatted-string')
    #     # print(ele.text, flush=True)
    #     print(ele.text)
    #     idx += 1
    # driver.quit()
    return True
    

# GET CHANNEL NAME
channel_url = "https://www.youtube.com/c/SpaceX/videos"
driver2.get(channel_url)
# driver.get("https://stackoverflow.com/questions/55400703/how-to-scroll-down-in-youtube-using-selenium")
driver2.implicitly_wait(1)

# GET VIDEOS

try:
    scroll_height = 10000
    element = driver2.find_element(By.TAG_NAME, 'ytd-continuation-item-renderer')
    while (element):
        scroll_func = "window.scrollTo(0, " + str(scroll_height) + ");"
        driver2.execute_script(scroll_func)
        scroll_height *= 2
        sleep(0.1)
        # print(element)
        element = driver2.find_element(By.TAG_NAME, 'ytd-continuation-item-renderer')
    sleep(0.5)
except:
    print("All videos loaded", flush=True)

# for i in range(3):
elements = driver2.find_elements(By.ID, 'thumbnail')
num = 0
transcript_links = []
for element in elements:
    # print(element.get_attribute("href"))
    link = element.get_attribute("href")
    # driver.get(channel_url)
    
    if (link):
        # Go to video, get transcript if one is available
        # if num == 10:
        #     driver2.quit()
        #     break
        # if getTranscript(link):
        #     num += 1
        #     transcript_links.append(link)
        # print(num)
        transcript_links.append(link)
        # print(link, flush=True)
        
# print("Number of videos: " + str(len(elements) - 2), flush=True)
print(transcript_links, flush=True)
driver2.quit()









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