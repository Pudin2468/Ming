from flask import Flask, render_template, request
from models.usuario import Usuario
from models.medidas import Medidas
from services.imc_service import calcular_imc
from services.classificar_imc import classificar_imc

app = Flask(__name__)

# Rota para a página inicial #
@app.route( '/', methods=['get', 'post'])
def index():
    return render_template(('index.html'))

# Rota para calcular o IMC #
@app.route( '/calcular', methods=['post'])
def calcular():
    nome = request.form['nome']
    idade = int(request.form['idade'])
    sexo = request.form['sexo']
    peso = float(request.form['peso'])
    altura = float(request.form['altura'])

    usuario = Usuario(nome, idade, sexo)
    medidas = Medidas(peso, altura)
    imc_calculator = calcular_imc(usuario, medidas)
    imc = imc_calculator.calcular_valor_imc()
    classificador = classificar_imc()
    classificacao = classificador.classifica_imc(imc)
    
    return render_template('resultado.html', nome=nome, imc=imc, classificacao=classificacao)

if __name__ == '__main__':
    app.run(debug=True)

#fim do codigo#

