from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBase


def tela():
    window = Tk()
    window.title("Produtos")
    window.geometry("600x350")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window)
    janela.pack(side=BOTTOM)

    hud = Frame(window, width=600, height=300, bg="blue")
    hud.pack(side=TOP)

    tabela = ttk.Treeview(janela)

    tabela['columns'] = ('ID', 'Descricao', 'Preco')

    tabela.column("#0", width=0, stretch=NO)
    tabela.column("ID", anchor=CENTER, width=100)
    tabela.column("Descricao", anchor=CENTER, width=100)
    tabela.column("Preco", anchor=CENTER, width=100)

    tabela.heading("#0", text="", anchor=CENTER)
    tabela.heading("ID", text="ID", anchor=CENTER)
    tabela.heading("Descricao", text="Descrição", anchor=CENTER)
    tabela.heading("Preco", text="Preço", anchor=CENTER)

    buttoncadastrar = ttk.Button(hud, text="Cadastrar", width=10, command=lambda: cadastrar())
    buttoncadastrar.place(x=100, y=40)

    buttoneditar = ttk.Button(hud, text="Editar", width=10, command=lambda: editar())
    buttoneditar.place(x=200, y=40)

    buttonexcluir = ttk.Button(hud, text="Excluir", width=10, command=lambda: excluir())
    buttonexcluir.place(x=300, y=40)

    buttonsair = ttk.Button(hud, text="Voltar", width=10, command=lambda: [window.destroy()])
    buttonsair.place(x=400, y=40)

    buttonatual = ttk.Button(hud, text="Atualizar", width=10, command=lambda: [window.destroy(), tela()])
    buttonatual.place(x=250, y=80)

    for rows in DataBase.Produtos():
        tabela.insert(parent='', index='end', iid=rows[0], text='', values=(rows[0], rows[1], rows[2]))

    tabela.pack()
    window.mainloop()


def editar():
    window = Tk()
    window.title("Produtos")
    window.geometry("350x170")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window, width=350, height=170, bg="blue")
    janela.pack()

    idlabel = Label(janela, text="Id:", font=("Century Gothic", 14), fg="black")
    idlabel.place(x=30, y=20)
    inputid = ttk.Entry(janela, width=30)
    inputid.place(x=140, y=25)

    descricao = Label(janela, text="Descrição:", font=("Century Gothic", 14), fg="black")
    descricao.place(x=30, y=55)
    inputdescr = ttk.Entry(janela, width=30)
    inputdescr.place(x=140, y=60)

    preco = Label(janela, text="Preço:", font=("Century Gothic", 14), fg="black")
    preco.place(x=30, y=90)
    inputpreco = ttk.Entry(janela, width=30)
    inputpreco.place(x=140, y=95)

    buttonsalvar = ttk.Button(janela, text="Salvar Alterações",
                              command=lambda: [DataBase.editar_prod(inputid.get(), inputdescr.get(), inputpreco.get()),
                                               window.destroy()])
    buttonsalvar.place(x=140, y=130)


def excluir():
    window = Tk()
    window.title("Produtos")
    window.geometry("300x100")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window, width=600, height=300, bg="blue")
    janela.pack()

    idlabel = Label(janela, text="Id:", font=("Century Gothic", 14), fg="black")
    idlabel.place(x=30, y=20)

    inputid = ttk.Entry(janela, width=30)
    inputid.place(x=100, y=25)

    buttonexcluir = ttk.Button(janela, text="Excluir", width=10,
                               command=lambda: [DataBase.excluir_prod(inputid.get()), window.destroy()])
    buttonexcluir.place(x=160, y=60)


def cadastrar():
    window = Tk()
    window.title("Produtos")
    window.geometry("300x150")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window, width=600, height=300, bg="blue")
    janela.pack()

    descricao = Label(janela, text="Descrição:", font=("Century Gothic", 14), fg="black")
    descricao.place(x=30, y=20)
    inputdescr = ttk.Entry(janela, width=30)
    inputdescr.place(x=100, y=25)

    preco = Label(janela, text="Preço:", font=("Century Gothic", 14), fg="black")
    preco.place(x=30, y=50)
    inputpreco = ttk.Entry(janela, width=30)
    inputpreco.place(x=100, y=55)

    buttoncadastrar = ttk.Button(janela, text="Cadastrar", width=10,
                                 command=lambda: [DataBase.inserir_prod(inputdescr.get(), inputpreco.get()), window.destroy()])
    buttoncadastrar.place(x=160, y=80)
