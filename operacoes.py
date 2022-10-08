import mysql.connector
import conexao
import this
this.msg = ""

db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()

def inserir(cpf, nome,  celular, email, senha):
    try:
        sql = "insert into gerente(cpf, nome, celular, email, senha) values('{}','{}','{}','{}','{}')".format(cpf, nome, celular, email, senha)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        return con.rowcount, "Inserido!"
    except Exception as erro:
        return erro

