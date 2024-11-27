import sqlite3;

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("CREATE TABLE Fornecedores (id_forn INTEGER PRIMARY KEY,nome TEXT)")
cur.execute("CREATE TABLE Produtos (id_prod INTEGER PRIMARY KEY,descricao TEXT, preco REAL)")
cur.execute("CREATE TABLE Cotacao (id_cot INTEGER PRIMARY KEY,data TEXT,hora TEXT,id_forn INTEGER,qtd INTEGER,id_prod INTEGER,total REAL, FOREIGN KEY (id_forn) REFERENCES Fornecedores (id_forn), FOREIGN KEY (id_prod) REFERENCES Produtos (id_prod))")
conn.commit()

def inserir_forn(nome):
	cur.execute("""
		insert into Fornecedores(nome) values(?);
	""", (nome))
	conn.commit()


def fornecedores():
	cur.execute("""
		select * from Fornecedores;
	""")
	rows = cur.fetchall()
	return rows


def editar_forn(id, nome):
	cur.execute("""
		update Fornecedores set nome = ? where id_forn = ?;
	""", (nome, id))
	conn.commit()


def excluir_forn(id):
	cur.execute("""
		delete from Fornecedores where id_forn = ?
	""", (id,))
	conn.commit()


def inserir_prod(descricao,preco):
	cur.execute("""
		insert into Produtos(descricao,preco) values(?,?);
	""", (descricao, preco))
	conn.commit()


def Produtos():
	cur.execute("""
		select * from Produtos;
	""")
	rows = cur.fetchall()
	return rows


def editar_prod(id, descricao, preco):
	cur.execute("""
		update Produtos set descricao = ?, preco = ? where id_prod = ?;
	""", (descricao, preco, id))
	conn.commit()


def excluir_prod(id):
	cur.execute("""
		delete from Produtos where id_prod = ?
	""",(id,))
	conn.commit()


def inserir_cot(data, hora, idforn, qtd, idprod, total):
	cur.execute("""
		insert into Cotacao(data,hora,id_forn,qtd,id_prod,total) values(?,?,?,?,?,?);
	""",(data,hora,idforn,qtd,idprod,total))
	conn.commit()


def Cotacao():
	cur.execute("""
		select id_cot,data,hora,Fornecedores.nome,qtd,Produtos.preco,total from Cotacao
			inner join Fornecedores
				on Fornecedores.id_forn=Cotacao.id_forn
			inner join Produtos
				on Produtos.id_prod=Cotacao.id_prod;
	""")
	rows = cur.fetchall()
	return rows


def editar_cot(id, data, hora, idforn, qtd, idprod, total):
	cur.execute("""
		update Cotacao set data = ?, hora = ?, id_forn = ?, qtd = ?, id_prod = ?, total = ? where id_cot = ?;
	""", (data, hora, idforn, qtd, idprod, total, id))
	conn.commit()


def excluir_cot(id):
	cur.execute("""
		delete from Cotacao where id_cot = ?
	""",(id,))
	conn.commit()


def preco_prod(idprod):
	cur.execute("""
		select preco from Produtos where id_prod = ?
	""", (idprod,))
	for row in cur.fetchall():
		return row[0]
