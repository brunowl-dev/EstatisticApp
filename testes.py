import os
import csv
from Dado import Dado
from Tabela import Tabela

leitura = list()
CAMINHO_TABELAS = 'Estaticapp/tabelas/' # Caminho da pasta onde estão as tabelas
os.makedirs(CAMINHO_TABELAS, exist_ok=True)
for file in os.listdir(CAMINHO_TABELAS): #Leitura das tabelas na lista tabela para sua manipulação
    dados = list()
    try:
        with open(CAMINHO_TABELAS + file, 'r', newline='') as arquivo:
            csv_reader = csv.reader(arquivo, delimiter=';')
            next(csv_reader)
            for linha in csv_reader:
                xi = float(linha[0])
                fi = int(linha[1])
                dado = Dado.cria_dado(xi, fi)
                dados.append(dado)
    except Exception as e:
        print('Tabela ainda não existe ou não tem nenhum dado!')
    file = Tabela.cria_tabela(file)
    for dado in dados:
        file.adiciona_dado(dado)
    leitura.append(file)
    
for item in leitura:
    print(item.nome)