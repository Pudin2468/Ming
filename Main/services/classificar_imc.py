class classificar_imc:
    
    # Classificação do IMC

    def classifica_imc(self, imc):
        if imc < 18.5:
            return "abaixo do peso"
        elif imc < 25:
            return "peso normal"
        elif imc < 30:
            return "sobrepeso"
        else:
            return "obesidade"

#fim do codigo# 