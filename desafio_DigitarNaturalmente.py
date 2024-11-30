from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import random


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


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(random.randint(1, 5)/30)  # Tempo de pausa para escrever


driver = iniciar_driver()
# navegar até o site
driver.get('https://cursoautomacao.netlify.app/desafios')
sleep(3)
driver.execute_script("window.scrollTo(0, 1000);")
sleep(1)
paragrafo = driver.find_element(
    By.XPATH, '//textarea[@id="campoparagrafo"]')


texto = """Aqui recomendo que você sempre tenha essa história pronta para contar de uma forma que saliente o seu interesse por a área. Isso porque caso você realmente esteja interessado na vaga, desta maneira você irá mostrar a quem estiver te analisando que você tem uma grande probabilidade de ser um profissional mais engajado com as tarefas da empresa. Capriche nessa história.
 """

digitar_naturalmente(texto, paragrafo)
botao_validar = driver.find_element(
    By.XPATH, '//button[@onclick="ValidarDesafio4()"]')
botao_validar.click()

input('')
driver.close()
