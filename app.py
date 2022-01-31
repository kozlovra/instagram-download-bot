import os, pickle, time
from config import cfg_usr, cfg_paswd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

def parse(url):
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument('log-level=3')
  chrome_app = Service(f"{os.path.dirname(os.path.abspath(__file__))}/Include/chromedriver.exe")
  driver = webdriver.Chrome(service=chrome_app, options=chrome_options)
  if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/Include/cookies.pkl"):
    driver.get('https://instagram.com')
    time.sleep(0.5)
    cookies = pickle.load(open(f"{os.path.dirname(os.path.abspath(__file__))}/Include/cookies.pkl", "rb"))
    for cookie in cookies:
      driver.add_cookie(cookie)
    driver.refresh()
  else:
    driver.get('https://www.instagram.com')
    time.sleep(1)
    username_input = driver.find_element(By.NAME, 'username')
    username_input.send_keys(cfg_usr)
    time.sleep(2)
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(cfg_paswd)
    time.sleep(2)
    password_input.send_keys(Keys.ENTER)
    pickle.dump(driver.get_cookies(), open(f"{os.path.dirname(os.path.abspath(__file__))}/Include/cookies.pkl", "wb"))

  driver.get(url)
  soup = BeautifulSoup(driver.page_source, 'lxml')
  driver.close()
  response = soup.find_all('img')
  urlretrieve( response[0]['src'], f"{os.path.dirname(os.path.abspath(__file__))}/photo.jpg")


def main():
  parse('https://www.instagram.com/p/CYcXvhEPEvV/')

if __name__ == '__main__':
  main()