from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import blue_archive.split as split
import os

chrome_option = Options()
chrome_option.add_argument("--headless")

# Create a browser instance with ChromeDriver
browser = webdriver.Chrome(options=chrome_option)

# Visit the web page
url = "https://bluearchive.jp/news/newsJump"

# Wait for the page to load completely
browser.implicitly_wait(10)

def fetch():

    browser.get(url)

    catalogue_box = browser.find_element(By.CLASS_NAME, "catalogueBox")
    li_element = catalogue_box.find_elements(By.TAG_NAME, "li")


    category = li_element[0].text.split('\n')[0]
    li_element[0].click()

    if category == 'お知らせ':
        category = 'news'
    elif category == 'メンテナンス':
        category = 'maintenance'
    elif category == 'イベント':
        category = 'event'

    browser.switch_to.window(browser.window_handles[-1])

    if os.path.exists('./blue_archive/color_fetch.js'):
        with open('./blue_archive/color_fetch.js', 'r', encoding="utf-8") as f:
            js_color = f.read()

    if os.path.exists('./blue_archive/fetch.js'):
        with open('./blue_archive/fetch.js', 'r', encoding="utf-8") as f:
            js = f.read()

    colors = browser.execute_script(js_color)
    content = browser.execute_script(js)

    if not os.path.exists('tmp'):
        os.makedirs('tmp')

    with open(f'./tmp/{category}.txt', 'w', encoding="utf-8") as f:
        for txt in content:
            f.write(txt.text+'\n')
    
    return *(split.read(category)), browser.current_url, colors

    
