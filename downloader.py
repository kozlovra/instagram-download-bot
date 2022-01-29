import time, os, pickle, random
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def get_image(self):
  driver = webdriver.Chrome(executable_path='/instabot/chromedriver.exe')
  driver.get('https://www.instagram.com')
  if os.path.exists('/instabot/cookies.pkl'):
    cookies = pickle.load(open("/instabot/cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(random.randint(2, 4))
    driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    driver.get(self)
    time.sleep(random.randint(2, 4))
    src = driver.find_element(By.TAG_NAME,'img')
    time.sleep(random.randint(2, 3))
    urlretrieve(src.get_attribute("src"), f"/instabot/img.jpg")
  pickle.dump(driver.get_cookies(), open("/instabot/cookies.pkl", "wb"))
  driver.close()
  driver.quit()

def main():
  get_image('https://www.instagram.com/p/CXmhvYoPyEO/')
  return

if __name__ == '__main__':
  main()