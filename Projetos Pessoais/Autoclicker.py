import pyautogui
import time
import random
time.sleep(5)
posicao = pyautogui.position()
caso = 30
while posicao != (0,0) and caso != 0:
    lista_de_palavras = [
        'casa', 'carro', 'janela', 'porta', 'computador', 'telefone', 'livro', 'caderno', 'caneta', 'mesa',
        'cadeira', 'gato', 'cachorro', 'elefante', 'girafa', 'borboleta', 'avião', 'barco', 'praia', 'montanha',
        'rio', 'oceano', 'floresta', 'cidade', 'vila', 'estrada', 'ponte', 'castelo', 'fortaleza', 'igreja',
        'museu', 'escola', 'universidade', 'mercado', 'restaurante', 'hospital', 'farmácia', 'padaria', 'biblioteca',
        'teatro', 'cinema', 'parque', 'jardim', 'praça', 'rua', 'avenida', 'bairro', 'cidade', 'estado'
    ]
    pyautogui.write(random.choice(lista_de_palavras))
    # Pressiona Enter
    pyautogui.press('enter', interval=0.5)
    # Seleciona a caixinha de pesquisa
    pyautogui.click(clicks=2, interval=0.5)
    # Seleciona o conteúdo nela
    pyautogui.hotkey("ctrl", "a", interval=0.5)

    caso -= 1
    posicao = pyautogui.position()
