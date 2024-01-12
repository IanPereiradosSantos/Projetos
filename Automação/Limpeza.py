# Passo a passo do projeto.
# Passo 1: Abrir a função executar do Windows (win + R);
# Passo 2: digitar "recent";
# Passo 3: Pressionar Enter;
# Passo 4: Clicar na pasta;
# Passo 5: Selecionar todos os arquivos com ctrl + A;
# Passo 6: Pressionar Delete;
# Passo 7: Aguardar;
# Passo 8: Fechar pasta recent com Control+F4;
# Passo 9: Abrir a função executar do Windows (win + R);
# Passo 10: Digitar "%temp%";
# Passo 11: Pressionar Enter;
# Passo 12: Clicar na pasta;
# Passo 13: Selecionar todos os arquivos com ctrl + A;
# Passo 14: Pressionar Delete;
# Passo 15: Pressionar a tecla up;
# Passo 16: Pressionar a tecla Enter;
# Passo 17: Pressionar a tecla down;
# Passo 18: Pressionar a tecla right;
# Passo 19: Pressionar a tecla Enter;
# Passo 20: Aguardar;
# Passo 21: Fechar pasta %temp% com Control+F4;
# Passo 22: Abrir a função executar do Windows (win + R);
# Passo 23: Digitar "temp";
# Passo 24: Pressionar Enter;
# Passo 25: Clicar na pasta;
# Passo 26: Selecionar todos os arquivos com ctrl + A;
# Passo 27: Pressionar Delete;
# Passo 28: Pressionar a tecla up;
# Passo 29: Pressionar a tecla Enter;
# Passo 30: Pressionar a tecla down;
# Passo 31: Pressionar a tecla right;
# Passo 32: Pressionar a tecla Enter;
# Passo 33: Aguardar;
# Passo 34: Fechar a pasta “temp” com Control+F4;
# Passo 35: Correr pro abraço!
import pyautogui
import time
time.sleep(5)
pyautogui.PAUSE = 1.5
pyautogui.hotkey("win", "r")
pyautogui.write("recent")
pyautogui.press("enter")
pyautogui.click(x=762, y=356)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyautogui.hotkey("ctrl", "f4")
pyautogui.hotkey("win", "r")
pyautogui.write("%temp%")
pyautogui.press("enter")
pyautogui.click(x=762, y=356)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyautogui.press("up")
pyautogui.press("enter")
pyautogui.press("down")
pyautogui.press("right")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "f4")
pyautogui.hotkey("win", "r")
pyautogui.write("temp")
pyautogui.press("enter")
pyautogui.click(x=762, y=356)
pyautogui.hotkey("ctrl", "a")
pyautogui.press("delete")
pyautogui.press("up")
pyautogui.press("enter")
pyautogui.press("down")
pyautogui.press("right")
pyautogui.press("enter")
pyautogui.hotkey("ctrl", "f4")







