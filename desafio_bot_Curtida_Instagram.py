from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as CondicaoEsperada


def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--start-maximized',
                 '--incognito']

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

    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]

    )
    return driver, wait


driver, wait = iniciar_driver()

# Entrar no site do instagram
driver.get('https://www.instagram.com/')

# Clicar e digitar meu usuário
campo_usuario = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, '//input[@name="username"]')))
campo_usuario.send_keys('seu_email@gmail.com')
sleep(3)

# Clicar e digitar minha senha
campo_senha = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, '//input[@name="password"]')))
campo_senha.send_keys('123456789')
sleep(3)

# Clicar no campo entrar
botao_entrar = wait.until(CondicaoEsperada.element_to_be_clickable(
    (By.XPATH, '//div[text()="Entrar"]')))
sleep(3)
botao_entrar.click()
sleep(10)
# Navegar até a página alvo
driver.get('https://www.instagram.com/disciplinados_ofc')
sleep(5)

# Clicar na última  postagem
postagens = wait.until(CondicaoEsperada.visibility_of_any_elements_located(
    (By.XPATH, '//div[@class="_aagw"]')))
sleep(3)
postagens[0].click()
sleep(3)
# Verificar se postagem foi curtida, caso não tenha sido, clicar curtir, caso já tenha sido, aguardar 24hrs
try:
    verifica_curtida = driver.find_element(By.XPATH,
                                           '//section//div[@role="button"]//*[@aria-label="Curtir"]')
except:
    print('A imagem já havia sido curtida.')
else:
    botao_curtir = driver.find_elements(By.XPATH,
                                        '//article[@role="presentation"]//section//div[@role="button"]')
    sleep(5)
    driver.execute_script('arguments[0].click()', botao_curtir[0])
    print('Deu certo! A imagem acabou de ser curtida.')
    sleep(86400)
