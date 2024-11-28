import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Obter o diretório onde o executável está localizado
if getattr(sys, 'frozen', False):  # Executável gerado por PyInstaller
    diretorio_atual = os.path.dirname(sys.executable)  # Caminho do .exe
else:  # Execução direta do script Python
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho para o diretório de downloads padrão
usuario = os.getlogin()  # Nome do usuário do sistema
diretorio_downloads = os.path.join("C:\\Users\\", usuario, "\\Downloads")

# Verificar se a pasta Downloads existe, caso contrário, usar o diretório do executável
if not os.path.exists(diretorio_downloads):
    print(f"Pasta Downloads não encontrada. Usando o diretório do executável: {diretorio_atual}")
    diretorio_downloads = diretorio_atual

# Configuração do ChromeDriver
caminho_driver = os.path.join(diretorio_atual, "chromedriver.exe")
service = Service(caminho_driver)

# Configurando opções do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abrir em tela cheia
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": diretorio_downloads,  # Diretório de downloads
    "download.prompt_for_download": False,  # Não solicitar confirmação
    "download.directory_upgrade": True,  # Atualizar o diretório automaticamente
    "safebrowsing.enabled": True,  # Habilitar navegação segura
    "safebrowsing.disable_download_protection": True  # Desabilitar proteção contra download
})

# Inicializando o driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Imprimir o diretório de downloads configurado
print(f"Os arquivos serão baixados no diretório: {diretorio_downloads}")

# Configurando o serviço do ChromeDriver
service = Service(caminho_driver)

# Configurando opções do navegador
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Abrir em tela cheia

# Configurar as preferências de download do Chrome
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": diretorio_downloads,  # Pasta de download
    "download.prompt_for_download": False,  # Não solicitar confirmação
    "download.directory_upgrade": True,  # Forçar o download para o diretório especificado
    "safebrowsing.enabled": True,  # Habilitar navegação segura
    "safebrowsing.disable_download_protection": True  # Desabilitar a proteção contra download de arquivos
})

# Inicializando o driver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Imprimir o diretório de downloads configurado
print(f"Os arquivos serão baixados no diretório: {diretorio_downloads}")

# Função para verificar se o arquivo foi completamente baixado
def verificar_download(download_dir, nome_arquivo, tempo_espera=60):
    tempo_inicial = time.time()
    while True:
        # Verifica se o arquivo específico foi baixado
        arquivos = [f for f in os.listdir(download_dir) if f.startswith(nome_arquivo)]
        
        if arquivos:
            # Confirma se o arquivo foi baixado sem o sufixo temporário '.crdownload'
            for arquivo in arquivos:
                caminho_arquivo = os.path.normpath(os.path.join(download_dir, arquivo))
                # Verificar se termina exatamente com o nome esperado ou com ".pdf" no final
                if (caminho_arquivo.endswith(nome_arquivo) or caminho_arquivo.endswith(f"{nome_arquivo}.pdf")) and not caminho_arquivo.endswith(".crdownload"):
                    return True  # Arquivo foi baixado corretamente

        # Se o tempo de espera for excedido, retorna False
        if time.time() - tempo_inicial > tempo_espera:
            return False
        
        time.sleep(1)


# Lista de usuários
usuarios = [
    # troque por usuarios de sua escolha e quantos quiser
    {"email": "teste@gmail.com", "senha": "teste123"},
]

# Processar cada usuário
for usuario in usuarios:
    try:
        # Acessar a página de login
        driver.get("https://sso.tce.sp.gov.br/cas-server/login")
        
        # Esperar e preencher o email
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(usuario["email"])
        
        # Esperar e preencher a senha
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(usuario["senha"], Keys.RETURN)
        
        # Esperar o redirecionamento após login
        WebDriverWait(driver, 20).until(EC.url_contains("tce.sp.gov.br"))

        # Redirecionar para a URL específica
        driver.get("https://www.tce.sp.gov.br/cadtcesp/#!/")
        
        # Aguardar até que o nome da pessoa seja carregado corretamente
        nome_pessoa_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'hidden-sm-down ng-binding')]"))
        )
        
        # Verificar se o nome da pessoa não é "NONE NONE"
        nome_pessoa = nome_pessoa_element.text.strip()
        if nome_pessoa != "NONE NONE":
            print(f"Página cadtcesp carregada. Nome da pessoa: {nome_pessoa}")
            
            driver.get("https://www.tce.sp.gov.br/cadtcesp/#!/pessoa/cadastro")
            
            print("Redirecionado para a página de cadastro com sucesso.")
            
            # Aguardar um tempo maior para garantir que o botão esteja visível
            botao_certificado = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@type='button' and contains(@class, 'md-raised') and contains(., 'GERAR CERTIFICADO')]"))
            )
            botao_certificado.click()
            print("Botão 'GERAR CERTIFICADO' clicado com sucesso.")
            
            # Localizar o checkbox
            checkbox = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'md-checkbox[name="name"]'))
            )
            checkbox.click()
            
            botao_gerar_certificado = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'md-raised') and contains(., 'Gerar Certificado')]"))
            )
            botao_gerar_certificado.click()
            print("Botão 'Gerar Certificado' no modal clicado com sucesso.")
            
            # Definir o nome do arquivo baseado no nome da pessoa ou outro critério
            nome_arquivo_esperado = f"Declaração de Atualização Cadastral - {nome_pessoa}"

            # Esperar pelo download
            if verificar_download(diretorio_downloads, nome_arquivo_esperado):
                print(f"Download do arquivo concluído com sucesso para o usuário {nome_pessoa}.")
            else:
                print(f"Erro: O arquivo para o usuário {nome_pessoa} não foi baixado dentro do tempo esperado.")


            # Fechar modal
            botao_fechar = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@aria-hidden='true' and contains(@class, 'white-text')]"))
            )
            botao_fechar.click()
            print("Botão de fechar clicado.")
            
            # Logout
            driver.get("https://www.tce.sp.gov.br/cadtcesp/logout")
            print("Link de logout clicado.")
            
            botao_logout = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Sair')]"))
            )

            # Clicar no botão de logout
            botao_logout.click()

    except Exception as e:
        print(f"Erro ao processar o usuário {nome_pessoa}")

# Encerrar o navegador após o processamento de todos os usuários
driver.quit()
print("Processo concluído. Todos os usuários foram processados.")
