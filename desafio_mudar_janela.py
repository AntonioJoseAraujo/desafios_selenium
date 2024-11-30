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
sleep(5)
janela_princial = driver.current_window_handle
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)
botao_janela = driver.find_element(By.XPATH,'//button[text()="Abrir nova janela"]')
sleep(1)
driver.execute_script('arguments[0].click()',botao_janela)
sleep(1)
janelas = driver.window_handles
for janela in janelas:
    if janela not in janela_princial:
        driver.switch_to.window(janela)
        sleep(1)
        cx_texto = driver.find_element(By.XPATH,"//textarea[@id='opiniao_sobre_curso']")
        sleep(1)
        cx_texto.click()
        sleep(1)
        cx_texto.send_keys('Estou adorando o curso!')
        sleep(2)
        botao_pesquisa = driver.find_element(By.XPATH, "//button[@id='fazer_pesquisa']")
        sleep(1)
        botao_pesquisa.click()
        sleep(1)
        driver.execute_script('window.scrollTo(0,300);')
        sleep(2)
        driver.close()
driver.switch_to.window(janela_princial)
sleep(2)
cx_depoimento = driver.find_element(By.XPATH, '//textarea[@name="campo_depoimento"]')
sleep(1)
cx_depoimento.click()
sleep(1)
cx_depoimento.send_keys('Antonio Jose de Araujo')

input('')
driver.close()