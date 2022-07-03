from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import os

from scraping import Scraping
from colors import Colors

if __name__ == '__main__':

    os.system('cls')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--start-maximized')

    chrome = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome, options=chrome_options)
    
    scraping = Scraping(driver)
    scraping.window_email()

    driver.get('https://telefonesimportados.netlify.app/')

    scraping.web_scraping()
    scraping.workbook()
    line = 2
    for nome, preco in zip(scraping.list_nome_phone, scraping.list_preco_phone):
        scraping.inserir_dados(line, nome, preco)
        line += 1
    scraping.wb.save(scraping.file)
    scraping.send_email()

    print('\n', '_' * 80)
    input(f'\tPrograma Finalizado. Aperte {Colors.blue} >> ENTER << {Colors.reset} para fechar o navegador')
    driver.quit()
