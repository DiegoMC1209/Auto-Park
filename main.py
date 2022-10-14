import re
import operacoesLogin, operacoes
from flask import Flask, render_template, request, flash, url_for
import this

this.dados = 0

pessoa = Flask(__name__) #representando uma variável do tipo flask

@pessoa.route('/', methods=['GET', 'POST'])
def pag_inicial():
    return render_template('/index.html', titulo='Página Principal')

@pessoa.route('/login.html', methods=['GET', 'POST'])
def pag_login():
    if request.method == 'POST':
        this.cpf = request.form['cpfGerente']
        this.senha = request.form['senhaGerente']
    return render_template('/login.html', titulo='Página Principal')

#cadastrar Funcionário
@pessoa.route('/cadastrarFunc.html', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.cpf = request.form['coletarCpf']
        this.nome = request.form['coletarNome']
        this.celular = request.form['coletarCelular']
        this.email = request.form['coletarEmail']
        this.senha = request.form['coletarSenha']

        if operacoesLogin.cpf_validate(this.cpf) == True:
            this.dados = operacoes.inserir(this.cpf, this.nome, this.celular, this.email, this.senha)
            return render_template('/cadastrarFunc.html', titulo='Página De Cadastro', resultado=this.dados)
        else:
            this.dados = "ERRO, favor informe um CPF válido!"
    return render_template('/cadastrarFunc.html', titulo='Página De Cadastro', resultado=this.dados)

if __name__ == "__main__":
    pessoa.run(debug=True, port=5000)