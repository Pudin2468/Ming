class calcular_imc:

    def __init__(self, usuario, medidas):
        self.usuario = usuario
        self.medidas = medidas

    def calcular_valor_imc(self):
        if self.medidas.altura == 0:
            raise ValueError("A altura não pode ser zero")
        imc = self.medidas.peso / (self.medidas.altura ** 2)
        return imc