from models.usuario import Usuario
from models.medidas import Medidas
from services.imc_service import calcular_imc
from services.classificar_imc import classificar_imc

# Criando um usuário
usuario = Usuario(nome="João", idade=68, sexo="Masculino")

# Criando as medidas do usuário
medidas = Medidas(peso=82, altura=1.68)

# Calculando o IMC do usuário
imc_calculator = calcular_imc(usuario, medidas)
imc = imc_calculator.calcular_valor_imc()

# Classificando o IMC do usuário
classificador = classificar_imc()
classificacao = classificador.classifica_imc(imc)
print(f"O IMC de {usuario.nome} é: {imc:.2f}")
print(f"A classificação do IMC de {usuario.nome} é: {classificacao}")
