from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from scraping import Scraping


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--start-maximized')

    chrome = Service('c:\chromedriver.exe')
    driver = webdriver.Chrome(service=chrome, options=chrome_options)
    driver.get('https://telefonesimportados.netlify.app/')
    
    scraping = Scraping(driver)
    scraping.web_scraping()
    #scraping.workbook()
    driver.quit()