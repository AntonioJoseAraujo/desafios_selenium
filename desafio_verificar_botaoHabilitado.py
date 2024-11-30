from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


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

botao1 = driver.find_element(
    By.XPATH, "//*[starts-with(text(),'Botão') and contains(text(),'1')]")
botao2 = driver.find_element(
    By.XPATH, "//*[starts-with(text(),'Botão') and contains(text(),'2')]")
botao3 = driver.find_element(
    By.XPATH, "//*[starts-with(text(),'Botão') and contains(text(),'3')]")


if botao1.is_enabled():
    print('Botão 1 está habilitado')
else:
    print('Botão 1 está desabilitado')
if botao2.is_enabled():
    print('Botão 2 está habilitado')
else:
    print('Botão 2 está desabilitado')
if botao3.is_enabled():
    print('Botão 3 está habilitado')
else:
    print('Botão 3 está desabilitado')


input('')
driver.close()
