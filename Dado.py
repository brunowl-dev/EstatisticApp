class Dado:
    def __init__(self, xi, fi):
        self.xi = xi
        self.fi = fi
        self.fr = 0 # Frequência relativa
        self.frp = 0 # Frequência relativa percentual
    
    def calcula_frequencias(self, n):
        # Calcula todo tipo de frequência e outras fórmulas
        self.fr = self.fi / n
        self.frp = self.fr * 100

    @classmethod
    def cria_dado(cls, xi, fi):
        return cls(xi, fi)