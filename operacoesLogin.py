import mysql.connector
import conexao
from random import randint
db_connection = conexao.conectar() #Abrindo a conexão com o banco de dados
con = db_connection.cursor()


def cpf_validate(numbers):
    #  Obtém os números do CPF e ignora outros caracteres
    cpf = [int(char) for char in numbers if char.isdigit()]

    #  Verifica se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
    #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
    #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
    if cpf == cpf[::-1]:
        return False

    #  Valida os dois dígitos verificadores
    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return False
    return True

def inserir(nome, cpf, celular, email, senha):
    try:
        sql = "insert into gerente(nome, cpf, celular, email, senha) values('{}','{}','{}','{}','{}')".format(nome, cpf, celular, email, senha)
        con.execute(sql)#Prepara o comando para ser executado
        db_connection.commit()#Executa o comando no banco de dados
        print(con.rowcount, " Funcionário Inserido! ")
    except Exception as erro:
        print(erro)

