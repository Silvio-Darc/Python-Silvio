import pyautogui
import time
import random
from faker import Faker
print("Primeiro passo: Deixe o bing aberto e a caixinha de pesquisa vazia\n")
print("Segundo passo: Volte para o console e aperte 'enter'\n")
print("Terceiro passo: Imediatamente após apertar 'enter', você terá 5 segundos para voltar ao bing\ne deixar o seu mouse em cima da caixinha de pesquisa\n")
print("Deixe o programa rodando até o fim, sem tirar o mouse de cima\n")
print("Caso precise parar antes, coloque o mouse no canto superior direito, o mais extremo possível")
print()
input("Aperte 'enter'")
fake = Faker()
time.sleep(5)
posicao = pyautogui.position()
caso = 30
while posicao != (0,0) and caso != 0:
    pyautogui.write(fake.word())
    # Pressiona Enter
    pyautogui.press('enter', interval=random.uniform(1, 1.5))
    # Seleciona a caixinha de pesquisa
    pyautogui.click(clicks=2, interval=1)
    # Seleciona o conteúdo nela
    pyautogui.hotkey("ctrl", "a")

    caso -= 1
    posicao = pyautogui.position()
