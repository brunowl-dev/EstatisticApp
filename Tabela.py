import csv

class Tabela:
    def __init__(self, nome):
        self.nome = nome
        self.dados = list()
        self.n = 0

    def adiciona_dado(self, dado):
        self.dados.append(dado)
        self.n += dado.fi

    def salvar_tabela(self):
        escrita = ['Xi', 'fi', 'fr', 'frp']
        with open(self.nome, 'w', newline='') as arquivo:
            csv_writer = csv.writer(arquivo, delimiter=';')
            csv_writer.writerow(escrita)
            for dado in self.dados:
                escrita = list()
                escrita.append(dado.xi)
                escrita.append(dado.fi)
                escrita.append(dado.fr)
                escrita.append(dado.frp)
                csv_writer.writerow(escrita)

    @classmethod
    def cria_tabela(cls, nome):
        return cls(nome)