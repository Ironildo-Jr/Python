from tkinter import *
from tkinter import ttk
import DataBase


def tela():
    window = Tk()
    window.title("Fornecedores")
    window.geometry("600x350")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window)
    janela.pack(side=BOTTOM)

    hud = Frame(window, width=600, height=300, bg="blue")
    hud.pack(side=TOP)

    tabela = ttk.Treeview(janela)

    tabela['columns'] = ('ID', 'Nome')

    tabela.column("#0", width=0, stretch=NO)
    tabela.column("ID", anchor=CENTER, width=100)
    tabela.column("Nome", anchor=CENTER, width=100)

    tabela.heading("#0", text="", anchor=CENTER)
    tabela.heading("ID", text="ID", anchor=CENTER)
    tabela.heading("Nome", text="Nome", anchor=CENTER)

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

    for rows in DataBase.fornecedores():
        tabela.insert(parent='', index='end', iid=rows[0], text='', values=(rows[0], rows[1]))

    tabela.pack()
    window.mainloop()


def editar():
    window = Tk()
    window.title("Fornecedores")
    window.geometry("300x150")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window, width=300, height=150, bg="blue")
    janela.pack()

    idlabel = Label(janela, text="Id:", font=("Century Gothic", 14), fg="black")
    idlabel.place(x=30, y=20)
    inputid = ttk.Entry(janela, width=30)
    inputid.place(x=100, y=25)

    nome = Label(janela, text="Nome:", font=("Century Gothic", 14), fg="black")
    nome.place(x=30, y=55)
    inputnome = ttk.Entry(janela, width=30)
    inputnome.place(x=100, y=60)

    buttonsalvar = ttk.Button(janela, text="Salvar Alterações",
                              command=lambda: [DataBase.editar_forn(inputid.get(), inputnome.get()),
                                               window.destroy()])
    buttonsalvar.place(x=150, y=100)


def excluir():
    window = Tk()
    window.title("Fornecedores")
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
                               command=lambda: [DataBase.excluir_forn(inputid.get()), window.destroy()])
    buttonexcluir.place(x=160, y=60)


def cadastrar():
    window = Tk()
    window.title("Fornecedores")
    window.geometry("300x100")
    window.configure(background="grey")
    window.resizable(width=False, height=False)

    janela = Frame(window, width=600, height=300, bg="blue")
    janela.pack()

    nome = Label(janela, text="Nome:", font=("Century Gothic", 14), fg="black")
    nome.place(x=30, y=20)

    inputnome = ttk.Entry(janela, width=30)
    inputnome.place(x=100, y=25)

    buttoncadastrar = ttk.Button(janela, text="Cadastrar", width=10,
                                 command=lambda: [DataBase.inserir_forn(inputnome.get()), window.destroy()])
    buttoncadastrar.place(x=160, y=60)
