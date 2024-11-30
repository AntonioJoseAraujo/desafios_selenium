from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--incognito', '--start-maximized']

    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'C:\\Users\\anton\\Downloads'

    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,

        'download.directory_upgrade': True,

        'download.prompt_for_download': False,

        "profile.default_content_setting_values.notifications": 2,

        "profile.default_content_setting_values.automatic_downloads": 1,
    })

    driver = webdriver.Chrome(options=chrome_options)
    return driver


driver = iniciar_driver()

driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollTop)")
input('')
driver.close()