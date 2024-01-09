
# Imports #

import pyautogui # extensão que permite clicar, escrever e etc #
import pandas
import time

# Quais os processos do código? #
# Apertar Win #
# Entrar no Google #
# Digitar o Link #
# Acessar o Link #
# Fazer Login #
# Cadastrar o produto 1 #
# voltar ao inicio #
# Cadastrar o produto 2 #
# ... e continua até acabar #


# CODIGO #

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
login = ("normalaccont.matheus@gmail.com")
password = ("40028922")
# Abrir o google #
pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
pyautogui.press("tab")
pyautogui.press("enter")

# Entrar no Link #
pyautogui.write(str(link))
pyautogui.press("enter")

# Login #
pyautogui.press("tab")
pyautogui.write(str(login))
pyautogui.press("tab")
pyautogui.write(str(password))
pyautogui.press("tab")
pyautogui.press("enter")


tabela = pandas.read_csv("produtos.csv")
for linha in tabela.index:
  # presets para as colunas da tabela #
  # codigo,marca,tipo,categoria,preco_unitario,custo,obs #

  C1 = tabela.loc[linha, "codigo"]
  C2 = tabela.loc[linha, "marca"]
  C3 = tabela.loc[linha, "tipo"]
  C4 = tabela.loc[linha, "categoria"]
  C5 = tabela.loc[linha, "preco_unitario"]
  C6 = tabela.loc[linha, "custo"]
  C7 = tabela.loc[linha, "obs"]
  # selecione a primeira caixa do formulario #
  pyautogui.press("tab")
  # Codigo #
  pyautogui.write(str(C1))
  pyautogui.press("tab")
  # marca #
  pyautogui.write(str(C2))
  pyautogui.press("tab")
  # tipo #
  pyautogui.write(str(C3))
  pyautogui.press("tab")
  # categoria #
  pyautogui.write(str(C4))
  pyautogui.press("tab")
  # preco_unitario #
  pyautogui.write(str(C5))
  pyautogui.press("tab")
  # custo #
  pyautogui.write(str(C6))
  pyautogui.press("tab")
  # obs #
  pyautogui.write(str(C7))
  pyautogui.press("tab")

  # Enviar #
  pyautogui.press("enter")

  # Começar do inicio da pagina #
  pyautogui.scroll (400)
  pyautogui.click(x=200, y=540)