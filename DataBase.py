import psycopg2

conn = psycopg2.connect(host="localhost",database="conceito",user="postgres",password="root")
cur = conn.cursor()


def inserir_forn(nome):
	cur.execute("""
		insert into Fornecedores(nome) values(%s);
	""", (nome,))
	conn.commit()


def fornecedores():
	cur.execute("""
		select * from Fornecedores;
	""")
	rows = cur.fetchall()
	return rows


def editar_forn(id, nome):
	cur.execute("""
		update Fornecedores set nome = %s where id_forn = %s;
	""", (nome, id))
	conn.commit()


def excluir_forn(id):
	cur.execute("""
		delete from Fornecedores where id_forn = %s
	""", (id,))
	conn.commit()


def inserir_prod(descricao,preco):
	cur.execute("""
		insert into Produtos(descricao,preco) values(%s,%s);
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
		update Produtos set descricao = %s, preco = %s where id_prod = %s;
	""", (descricao, preco, id))
	conn.commit()


def excluir_prod(id):
	cur.execute("""
		delete from Produtos where id_prod = %s
	""",(id,))
	conn.commit()


def inserir_cot(data, hora, idforn, qtd, idprod, total):
	cur.execute("""
		insert into Cotacao(datta,hora,id_forn,qtd,id_prod,total) values(%s,%s,%s,%s,%s,%s);
	""",(data,hora,idforn,qtd,idprod,total))
	conn.commit()


def Cotacao():
	cur.execute("""
		select id_cot,datta,hora,Fornecedores.nome,qtd,Produtos.preco,total from Cotacao
			inner join Fornecedores
				on Fornecedores.id_forn=Cotacao.id_forn
			inner join Produtos
				on Produtos.id_prod=Cotacao.id_prod;
	""")
	rows = cur.fetchall()
	return rows


def editar_cot(id, data, hora, idforn, qtd, idprod, total):
	cur.execute("""
		update Cotacao set datta = %s, hora = %s, id_forn = %s, qtd = %s, id_prod = %s, total = %s where id_cot = %s;
	""", (data, hora, idforn, qtd, idprod, total, id))
	conn.commit()


def excluir_cot(id):
	cur.execute("""
		delete from Cotacao where id_cot = %s
	""",(id,))
	conn.commit()


def preco_prod(idprod):
	cur.execute("""
		select preco from Produtos where id_prod = %s
	""", (idprod,))
	for row in cur.fetchall():
		return row[0]