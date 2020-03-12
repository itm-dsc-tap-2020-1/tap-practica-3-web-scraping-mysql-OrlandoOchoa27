import tkinter as Tk
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector as mysql

conexion=mysql.connect(host='localhost')
operacion=conexion.cursor()
operacion.execute("SELECT * FROM web")

pag_inicial=input('Ingrese URL: ')
url=urlopen(pag_inicial)

print("\Enlaces extraidos de la pagina web "+pag_inicial+"\n")
bs=BeautifulSoup(url.read, 'html.parser')
for enlaces in bs.find_all("a"):
    pag=enlaces.get("href")
    b=False
    print("hred: {}".format(enlaces.get("href")))
print("\nFIn")

for pagina,status, in operacion.fetchall():
    print(pagina,status)


for pagina,status, in operacion.fetchall():
    url=pagina

    print("Enlaces extraidos \n")
    bs=BeautifulSoup(url.read(),'html.parser')
    for enlaces in bs.find_all("a"):
        pag=enlaces.get("href")
        b=False
        print("href: {}".format(enlaces.get("href")))
    print("\nFin")

    conexion.close()
