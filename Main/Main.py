from models.usuario import Usuario
from models.medidas import Medidas
from services.imc_service import calcular_imc

# Criando um usuário
usuario = Usuario(nome="João", idade=30, sexo="Masculino")
# Criando as medidas do usuário
medidas = Medidas(peso=80, altura=1.75)
# Calculando o IMC do usuário
imc_calculator = calcular_imc(usuario, medidas)
imc = imc_calculator.calcular_valor_imc()
print(f"O IMC de {usuario.nome} é: {imc:.2f}")
