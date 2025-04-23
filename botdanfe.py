import os
import sys
import threading
import time
import keyboard
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from botcity.core import DesktopBot
from downloadanfe import downloadanfe
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



# Configurar o ChromeDriver com a opção de ini
# ciar maximizado
#chrome_options = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Iniciar o navegador maximizado
chrome_options.add_argument("--disable-application-cache")  # Desativa o cache do navegador
chrome_options.add_argument("--disk-cache-size=0")  # Define o tamanho do cache como 0


# Desativar a mensagem "Chrome está sendo controlado por um software de teste automatizado"
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

link_file = "link.txt"  # Nome do arquivo para armazenar o link
contagem = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "35", "40", "45", "50", "100", "150", "200", "250", "300", "350"]

def save_link(link):
    with open(link_file, "w") as file:
        file.write(link)

def load_link():
    if os.path.exists(link_file):
        with open(link_file, "r") as file:
            return file.read().strip()
    return ""

link_salvo = load_link()  # Carregar o link ao iniciar o bot

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def release_keys():
    if keyboard.is_pressed('ctrl'):
        keyboard.release('ctrl')
    if keyboard.is_pressed('shift'):
        keyboard.release('shift')

def interromper():
    while True:
        if keyboard.is_pressed('e'):
            release_keys()
            os._exit(0)

def parar():
    while True:
        if keyboard.is_pressed('r'):
            release_keys()
            restart_program()

class Bot(DesktopBot):
    def action(self, execution=None):
        global link_salvo  # Usar a variável global

        def iniciar_download():
            nonlocal contador
            link_salvo = link_var.get()
            save_link(link_salvo)  # Salvar o link em um arquivo
            cont = int(contagem_var.get())
            threading.Thread(target=interromper).start()
            threading.Thread(target=parar).start()

            PROXY = '45.140.143.77:18080'
            #chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--proxy-server=%s' % PROXY)  # Configurar o proxy
            service = Service(ChromeDriverManager(version="134.0.6998.178").install())
            #service = Service("chromedriver.exe")
            driver = webdriver.Chrome(service=service, options=chrome_options)
            time.sleep(5)
            driver.get(link_salvo)  # Testar o proxy com o Google
            time.sleep(5)  # Esperar 5 segundos para carregar a página

            # Inicializar o navegador controlado pelo Selenium
            #service = Service(ChromeDriverManager().install())
            #driver = webdriver.Chrome(service=service, options=chrome_options)
            #driver.get(link_salvo)  # Abre o link no navegador maximizado



            # Chamar a função para realizar o download
            downloadanfe(contador, cont, bot=self, self=self, driver=driver)

        contador = 0    

        # Criar a janela principal usando ttkbootstrap
        app = ttk.Window(themename="flatly")  # Escolha um tema claro
        app.title("DOWNLOAD")
        app.geometry("500x300")  # Ajustar o tamanho da janela

        # Configurar o fundo branco
        app.configure(bg="white")

        # Layout da interface usando grid
        frame = ttk.Frame(app, padding=20)
        frame.grid(row=0, column=0, sticky=NSEW)

        # Configurar o layout responsivo
        app.columnconfigure(0, weight=1)
        app.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        # Campo de link
        ttk.Label(frame, text="Link:", anchor=E, font=("Helvetica", 12)).grid(row=0, column=0, sticky=E, pady=5)
        link_var = ttk.StringVar(value=link_salvo)
        ttk.Entry(frame, textvariable=link_var).grid(row=0, column=1, sticky=EW, padx=10)

        # Linha em branco
        ttk.Label(frame, text="", background="white").grid(row=1, column=0, columnspan=2, pady=10)

        # Campo de quantidade ao lado do texto
        ttk.Label(frame, text="Quantidade de DANFE para download:", anchor=W, font=("Helvetica", 12)).grid(row=2, column=0, sticky=W, pady=5)
        contagem_var = ttk.StringVar(value=contagem[0])
        ttk.Combobox(frame, textvariable=contagem_var, values=contagem, width=10).grid(row=2, column=1, sticky=W, padx=10)

        # Linha em branco
        ttk.Label(frame, text="", background="white").grid(row=3, column=0, columnspan=2, pady=10)

        # Instruções
        ttk.Label(frame, text="Para interromper, pressione 'e'.", anchor=W, font=("Helvetica", 10), foreground="red").grid(row=4, column=0, columnspan=2, pady=10)

        # Linha em branco
        ttk.Label(frame, text="", background="white").grid(row=5, column=0, columnspan=2, pady=10)

        # Botão de download
        ttk.Button(frame, text="INICIAR", command=iniciar_download, bootstyle="info").grid(row=6, column=0, columnspan=2, pady=10)

        app.mainloop()

    def not_found(self, label):
        print(f"Element not found: {label}") 

if __name__ == '__main__':
    Bot.main()