'''
Compiliamo con un bot il foglio dati excel

'''


import os
from time import sleep
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pandas import read_csv

PATH = os.path.dirname(__file__)
os.chdir(PATH)


NUMBEO_LINK = 'https://it.numbeo.com'
CATEGORIE = {
    "Criminalità": "Paura che ci rubino l\'automobile",
    "Assistenza Sanitaria": "Cordialità e gentilezza del personale sanitario",
    "Inquinamento": "Insoddisfazione per la Nettezza Urbana"
}


df = read_csv('./citta_latine.csv', index_col=0, encoding='utf-8')

chrome_driver = ChromeDriverManager().install()
driver = Chrome(service=Service(chrome_driver))
driver.maximize_window()
driver.get(NUMBEO_LINK)


for luogo in df.index:
    try:
        driver.find_element(
            By.ID,
            'city_selector_menu_city_id').send_keys(luogo)
        sleep(2)
        driver.find_element(By.CLASS_NAME, 'ui-menu-item').click()

        for categoria, indice in CATEGORIE.items():
            driver.find_element(
                By.XPATH,
                f'//span[contains(@class,"nobreak")]/a[text()="{categoria}"]').click()
            indice_tr = driver.find_element(
                By.XPATH,
                f'//td[text()="{indice}"]/parent::tr')
            valore_td = indice_tr.find_element(By.CLASS_NAME, 'indexValueTd')
            df.loc[luogo, categoria] = valore_td.text
            sleep(2)
    except:
        continue


df.to_csv("città_latine_compilato.csv")
