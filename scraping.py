from selenium.webdriver.common.by import By
from openpyxl import Workbook
from datetime import datetime
import re


class Scraping:
    
    def __init__(self, driver):
        self.driver = driver

        self.num_pages = By.XPATH, '/html/body/div[5]/div[2]/div[2]/div/div/nav/ul'
        self.btn_next = By.XPATH, '/html/body/div[5]/div[2]/div[2]/div/div/nav/ul/li[7]/a'
    
    def web_scraping(self):
        self.list_nome_phone = []
        self.list_preco_phone = []

        pages = self.driver.find_element(*self.num_pages).text
        pages = re.sub(r'\n', '', pages)
        if '«' in pages:
            pages = str(pages).strip('«').strip('»').strip()

        for page in range(1, len(pages)):
            for item in range(1, 13):
                nome_phone = self.driver.find_elements(By.XPATH, f'/html/body/div[5]/div[2]/div[1]/div[{item}]/div/h2/a')
                preco_phone = self.driver.find_elements(By.XPATH, f'/html/body/div[5]/div[2]/div[1]/div[{item}]/div/div[2]/ins')
                self.list_nome_phone.append(nome_phone[0].text)
                self.list_preco_phone.append(preco_phone[0].text)
            self.driver.find_element(*self.btn_next).click()
        print(self.list_nome_phone)
        print(self.list_preco_phone)

    def workbook(self, lines, file='telefones importados.xlsx'):
        self.wb = Workbook()
        self.wb.save(file)
        self.ws = self.wb.active

        self.ws.cell(column=1, row=lines).value = ""
        self.ws.cell(column=2, row=lines).value = ""
        self.ws.cell(column=2, row=lines).value = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.wb.save(file)