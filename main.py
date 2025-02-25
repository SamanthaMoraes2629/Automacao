import pyautogui
import pygetwindow as gw
import pandas
import time

pyautogui.PAUSE = 1

# Abrir o Google Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)

# Verificar se a janela do Chrome está maximizada
chrome_windows = [win for win in gw.getWindowsWithTitle('Google Chrome') if win.isActive]

if chrome_windows:
    chrome_window = chrome_windows[0]  # Seleciona a primeira janela ativa do Chrome
    if not chrome_window.isMaximized:
        print("A janela do Chrome não está maximizada. Maximizando...")
        chrome_window.maximize()
    else:
        print("A janela do Chrome já está maximizada.")
else:
    print("Nenhuma janela ativa do Google Chrome foi encontrada.")

# Navegar para o site e fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=2210, y=-192)
pyautogui.write("samanthatestes@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("tab")
pyautogui.press("enter")

# Ler a tabela de produtos
tabela = pandas.read_csv("produtos.csv")
print(tabela)
time.sleep(2)

# Processar cada linha da tabela
for linha in tabela.index:
    pyautogui.click(x=2187, y=-311)
    # Código
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # Marca
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    # Tipo
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    # Categoria
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    # Preço Unitário
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    # Custo
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    # Observação
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)
