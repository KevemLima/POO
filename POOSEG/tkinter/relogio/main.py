from tkinter import *
import tkinter
from datetime import datetime

#cores
cor1 = "#3d3d3d" #preta
cor2 = "#FFFFFF" #branca

janela = Tk()
janela.title('Relógio Digital')
janela.geometry("440x180")
janela.resizable(width = FALSE, height = FALSE)
janela.config(bg = cor1)

def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.strftime("%d")
    mes = tempo.strftime("%b") #B = January // b = Jan
    ano = tempo.strftime("%Y")
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text="", font=("Arial 80"), bg = cor1, fg = cor2)
l1.grid(row = 0, column = 0, sticky = NW, padx = 5)


l2 = Label(janela, text="21/01/2025", font="Arial 16", bg = cor1,fg = cor2)
l2.grid(row = 1, column = 0, sticky = NW, padx = 5)

relogio()
janela.mainloop()
