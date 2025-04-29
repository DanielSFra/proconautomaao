import pyautogui
import time

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3)
pyautogui.write("https://proconweb.ssp.go.gov.br/#/baixarArquivo")
pyautogui.press("enter")
time.sleep(3)
# principal
pyautogui.click(x=1334, y=312)
time.sleep(3)
#area do fornecedor
pyautogui.click(x=642, y=625)
time.sleep(3)
#clicando no botão Entrar
pyautogui.click(x=571, y=804)
time.sleep(3)
#clicando no botão baixar arquivo
pyautogui.click(x=631, y=311)
time.sleep(3)
#clicando no botão baixar download
pyautogui.click(x=741, y=414)
time.sleep(3)
