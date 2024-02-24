import pandas as pd
import pyautogui as pg
import webbrowser as web
import time

data = pd.read_excel(r"C:\Users\LENOVO\Desktop\PROYECTO\gym\data\usuarios.xlsx")
data.head(3)

for i in range(len(data)):
    celular = data.loc[i,'celular'].astype(str)
    nombre = data.loc[i,'nombre']

    mensaje = "Hola " + nombre + ", este es un mensaje enviado a traves de la Web de Talar Gym, queremos avisarte que este sabado 24 de Febrero el gimnasio abrira de 10 a 13hs. Te esperamos!! 💪"

    firefox_path = "C:/Program Files/Mozilla Firefox/firefox.exe %s"
    web.get(firefox_path).open("https://web.whatsapp.com/send?phone=" + celular + "&text=" + mensaje)

    time.sleep(8)
    pg.click(1400,965)
    time.sleep(3)
    pg.click(button='left')
    time.sleep(3)
    pg.press('enter')
    time.sleep(3)
    pg.hotkey('ctrl', 'w')
    time.sleep(3)




