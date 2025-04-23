import threading
import time
from botcity.core import DesktopBot
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium import webdriver


primeira_execucao = True  # Variável de controle para a primeira execução

def downloadanfe(contador, cont, bot: DesktopBot, self: DesktopBot, driver,  executation=None):
    global primeira_execucao

    while contador < cont:
        self.wait(1000)
        
        # Verificar se é a primeira execução
        if primeira_execucao:
            bot.type_keys(["alt", "tab"]*2)
            self.wait(2000)
            bot.type_keys(["alt"])   # Executa o comando com 2 alternâncias
            #self.wait(1000)  # Aguarda 2 segundos para garantir que a alternância foi concluída
            primeira_execucao = False  # Marca como já executado

        else:
            bot.type_keys(["alt", "tab"]*1)
            self.wait(2000)
            #bot.type_keys(["alt"])   # Executa o comando com 1 alternância 


            
        self.wait(2000)
        bot.type_keys(["ctrl", "c"])  # Copiar a chave de acesso atual
        bot.type_keys(["alt", "tab"]*1)
        self.wait(1000)

        # Verificar se o tempo total de espera é maior ou igual a 2 segundos
        start_time3 = time.time()
        while True:
            if time.time() - start_time3 >= 2:
                self.wait(2000)
            else:
                break
            
        # Localizar o elemento no navegador já aberto
        input_element = driver.find_element(By.XPATH, '//*[@id="get-danfe"]/div/div/div[1]/div/div/div/input')

        # Colar o conteúdo da área de transferência no campo
        input_element.send_keys(Keys.CONTROL, 'v')

        self.wait(1000)
        bot.type_keys(["tab"])
        self.wait(3000)
        bot.type_keys(["enter"])
        self.wait(6000)

        # Continuar com o fluxo normal
        bot.type_keys(["tab"] * 3)
        bot.type_keys(["enter"])
        self.wait(1000)
        bot.type_keys(["tab"] * 8)
        bot.type_keys(["enter"])
        self.wait(1000)
        bot.type_keys(["ctrl", "v"])
        bot.type_keys(["enter"])
        bot.type_keys(["ctrl", "f4"])
        bot.type_keys(["shift", "tab"] * 2)
        bot.type_keys(["enter"])
        bot.type_keys(["alt", "tab"])
        bot.type_keys(["right"])
        self.wait(1000)
        self.paste("OK")
        bot.type_keys(["down"])
        bot.type_keys(["left"])
        self.wait(1000)                 
        bot.type_keys(["alt", "tab"]*1)
        #self.wait(2000)
        #bot.type_keys(["alt"]) 

        contador += 1
