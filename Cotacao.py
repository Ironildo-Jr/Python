from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase


def tela():
    window = Tk()
    window.title("Cotações")
    window.geometry("700x350")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window)
    janela.pack(side=BOTTOM)

    hud = Frame(window, width=700, height=300, bg="blue")
    hud.pack(side=TOP)

    tabela = ttk.Treeview(janela)

    tabela['columns'] = ('ID', 'Data', 'Hora','Id_forn','qtd','id_prod','total')

    tabela.column("#0", width=0, stretch=NO)
    tabela.column("ID", anchor=CENTER, width=100)
    tabela.column("Data", anchor=CENTER, width=100)
    tabela.column("Hora", anchor=CENTER, width=100)
    tabela.column("Id_forn", anchor=CENTER, width=100)
    tabela.column("qtd", anchor=CENTER, width=100)
    tabela.column("id_prod", anchor=CENTER, width=100)
    tabela.column("total", anchor=CENTER, width=100)

    tabela.heading("#0", text="", anchor=CENTER)
    tabela.heading("ID", text="ID", anchor=CENTER)
    tabela.heading("Data", text="Data", anchor=CENTER)
    tabela.heading("Hora", text="Hora", anchor=CENTER)
    tabela.heading("Id_forn", text="Fornecedor", anchor=CENTER)
    tabela.heading("qtd", text="Quantidade", anchor=CENTER)
    tabela.heading("id_prod", text="Valor Unitário", anchor=CENTER)
    tabela.heading("total", text="Valor Total", anchor=CENTER)

    buttoncadastrar = ttk.Button(hud, text="Cadastrar", width=10, command=lambda: cadastrar())
    buttoncadastrar.place(x=220, y=40)

    buttoneditar = ttk.Button(hud, text="Editar", width=10, command=lambda: editar())
    buttoneditar.place(x=320, y=40)

    buttonsair = ttk.Button(hud, text="Voltar", width=10, command=lambda: [window.destroy()])
    buttonsair.place(x=420, y=40)

    buttonatual = ttk.Button(hud, text="Atualizar", width=10, command=lambda: [window.destroy(), tela()])
    buttonatual.place(x=320, y=80)

    for rows in DataBase.Cotacao():
        tabela.insert(parent='', index='end', iid=rows[0], text='', values=(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6]))

    tabela.pack()
    window.mainloop()


def editar():
    window = Tk()
    window.title("Cotações")
    window.geometry("400x300")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window, width=400, height=300, bg="blue")
    janela.pack()

    idlabel = Label(janela, text="Id:", font=("Century Gothic", 14), fg="black")
    idlabel.place(x=30, y=20)
    inputid = ttk.Entry(janela, width=30)
    inputid.place(x=200, y=25)

    data = Label(janela, text="Data:", font=("Century Gothic", 14), fg="black")
    data.place(x=30, y=55)
    inputdata = ttk.Entry(janela, width=30)
    inputdata.place(x=200, y=60)

    hora = Label(janela, text="Hora:", font=("Century Gothic", 14), fg="black")
    hora.place(x=30, y=90)
    inputhora = ttk.Entry(janela, width=30)
    inputhora.place(x=200, y=95)

    forn = Label(janela, text="Id do Fornecedor:", font=("Century Gothic", 14), fg="black")
    forn.place(x=30, y=125)
    inputforn = ttk.Entry(janela, width=30)
    inputforn.place(x=200, y=130)

    qtd = Label(janela, text="Quantidade Prod:", font=("Century Gothic", 14), fg="black")
    qtd.place(x=30, y=160)
    inputqtd = ttk.Entry(janela, width=30)
    inputqtd.place(x=200, y=165)

    prod = Label(janela, text="Produto:", font=("Century Gothic", 14), fg="black")
    prod.place(x=30, y=195)
    inputprod = ttk.Entry(janela, width=30)
    inputprod.place(x=200, y=200)

    buttonsalvar = ttk.Button(janela, text="Salvar Alterações",
                              command=lambda: [DataBase.editar_cot(inputid.get(), inputdata.get(), inputhora.get(), inputforn.get(), inputqtd.get(), inputprod.get(), str(DataBase.preco_prod(inputprod.get())*int(inputqtd.get()))), window.destroy()])
    buttonsalvar.place(x=160, y=230)


def cadastrar():
    window = Tk()
    window.title("Produtos")
    window.geometry("400x300")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window, width=600, height=300, bg="blue")
    janela.pack()

    data = Label(janela, text="Data:", font=("Century Gothic", 14), fg="black")
    data.place(x=30, y=20)
    inputdata = ttk.Entry(janela, width=30)
    inputdata.place(x=200, y=25)

    hora = Label(janela, text="Hora:", font=("Century Gothic", 14), fg="black")
    hora.place(x=30, y=55)
    inputhora = ttk.Entry(janela, width=30)
    inputhora.place(x=200, y=60)

    forn = Label(janela, text="Id do Fornecedor:", font=("Century Gothic", 14), fg="black")
    forn.place(x=30, y=90)
    inputforn = ttk.Entry(janela, width=30)
    inputforn.place(x=200, y=95)

    qtd = Label(janela, text="Quantidade Prod:", font=("Century Gothic", 14), fg="black")
    qtd.place(x=30, y=125)
    inputqtd = ttk.Entry(janela, width=30)
    inputqtd.place(x=200, y=130)

    idprod = Label(janela, text="Id do Produto:", font=("Century Gothic", 14), fg="black")
    idprod.place(x=30, y=160)
    inputprod = ttk.Entry(janela, width=30)
    inputprod.place(x=200, y=165)

    buttoncadastrar = ttk.Button(janela, text="Cadastrar", width=10,
                                 command=lambda: [DataBase.inserir_cot(inputdata.get(), inputhora.get(), inputforn.get(), inputqtd.get(), inputprod.get(), str(DataBase.preco_prod(inputprod.get())*int(inputqtd.get()))), window.destroy()])
    buttoncadastrar.place(x=160, y=230)
