from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Fornecedores
import Cotacao
import Produtos


window = Tk()
window.title("Menu")
window.geometry("600x300")
window.configure(background="grey")
window.resizable(width=False, height=False)

logo = PhotoImage(file="Images/conceito-tecnologia.png")

upframe = Frame(window, width=600, height=120, bg="blue", relief="raise")
upframe.pack(side=TOP)

downframe = Frame(window, width=600, height=170, bg="lightblue", relief="raise")
downframe.pack(side=BOTTOM)

logoLabel = Label(upframe, image=logo, bg="lightblue")
logoLabel.place(x=200, y=10)

buttonForn = ttk.Button(downframe, text="Fornecedores", width=20, command=lambda:Fornecedores.tela())
buttonForn.place(x=50,y=70)

buttonProd = ttk.Button(downframe, text="Produtos", width=20, command=lambda:Produtos.tela())
buttonProd.place(x=235,y=70)

buttonCot = ttk.Button(downframe, text="Cotacao", width=20, command=lambda:Cotacao.tela())
buttonCot.place(x=420,y=70)

window.mainloop()

