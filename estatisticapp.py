import os
import csv
from Dado import Dado
from Tabela import Tabela
#\n
menu = -1

def leitura_tabelas():
    leitura = list()
    CAMINHO_TABELAS = 'Estatisticapp/tabelas/' # Caminho da pasta onde estão as tabelas
    os.makedirs(CAMINHO_TABELAS, exist_ok=True)
    for arquivo in os.listdir(CAMINHO_TABELAS): #Leitura das tabelas na lista tabela para sua manipulação
        dados = leitura_dados(CAMINHO_TABELAS + arquivo)
        tabela = Tabela.cria_tabela(CAMINHO_TABELAS + arquivo)
        if dados != -1:
            for dado in dados:
                tabela.adiciona_dado(dado)
        leitura.append(tabela)
    return leitura

def seleciona_tabela(tabelas):
    for i in range(len(tabelas)):
        print(f"{i} - {tabelas[i].nome}")
    while True:
        indice = int(input('Digite o índice da tabela: '))
        if indice < 0:
            print('Digite um valor positivo!')
            continue
        if indice >= len(tabelas):
            print('Índice fora do intervalo!')
            continue
        print(f'Tabela {tabelas[i].nome} selecionada!')
        return indice

def leitura_dados(nome):
        # Usuário escolhe a tabela, programa separa o nome, e cria uma instância tabela só para manipular escrita e leitura dos dados
        dados = list()
        try:
            with open(nome, 'r', newline='') as arquivo:
                csv_reader = csv.reader(arquivo, delimiter=';')
                next(csv_reader)
                for linha in csv_reader:
                    xi = float(linha[0])
                    fi = int(linha[1])
                    dado = Dado.cria_dado(xi, fi)
                    dados.append(dado)
        except (FileNotFoundError, StopIteration) as e:
            print('Tabela ainda não existe! ou não tem nenhum dado')
            return -1
        return dados

def seleciona_menu():
    while True:
        try:
            menu = int(input('EstatisticApp\n1-Criar tabela\n2-Seleciona tabela\n3-Adicionar dado\n4-Salvar tabela em .CSV\n5-Ver tabela\n6-Sair\n'))
            if (menu <= 0):
                print('Digite um valor positivo e maior que zero!')
        except Exception as e:
            print('Digite um valor válido!')
        if (menu > 0):
            return menu
            break

tabelas = leitura_tabelas()
dados = list()

while (menu != 6):
    os.system('cls')
    try:
        print(f'{tabela.nome} está selecionada!')
    except NameError:
        print('Nenhuma tabela selecionada...')

    menu = seleciona_menu()

    if menu == 6:
        print('Programa finalizando...')
        break
    elif (menu == 1): ##Criação de uma tabela
        nome = 'Estatisticapp/tabelas/'
        nome += input('Digite o nome da tabela: ')
        nome += '.csv'
        tabela = Tabela.cria_tabela(nome)
        tabelas.append(tabela)
        print(f"Tabela {tabela.nome} criada com sucesso!")
        os.system('pause') 
    elif (menu == 2):
        indice = seleciona_tabela(tabelas)
        tabela = tabelas[indice]
        os.system('pause')
    elif (menu == 3):
        if not dados:
            dados = leitura_dados(tabela.nome)
            if (dados == -1):
                dados = list()
        #DADO NOVO
        xi = float(input('Digite o valor desse novo dado: '))
        fi = int(input('Digite a frequência desse novo dado: '))
        novo_dado = Dado.cria_dado(xi, fi)
        dados.append(novo_dado)
        dados.sort(key=lambda d: d.xi)
        tabela = Tabela.cria_tabela(tabela.nome)
        for dado in dados:
            tabela.adiciona_dado(dado)
        for dado in tabela.dados:
            dado.calcula_frequencias(tabela.n)
        print('DADO ADICIONADO COM SUCESSO!')
        os.system('pause')
    elif (menu == 4):
        tabela.salvar_tabela()
        print(f'A tabela {tabela.nome} foi salva com sucesso e já está disponível para consulta em CSV!')
        os.system('pause')
    elif (menu == 5):
        print('Xi\tfi\tfr\tfrp')
        for dado in tabela.dados:
            dado.calcula_frequencias(tabela.n)
            print(f"{dado.xi}\t{dado.fi}\t{dado.fr:.4f}\t{dado.frp:.2f}%")
        os.system('pause')
        
### IDEIAS PARA PRÓXIMA VERSÃO
# SE O USUÁRIO JÁ DIGTOU UM XI, SOMAR OS FI'S
# MEDIDAS DE TENDENCIA CENTRAL
# MEDIA
# VARIANCIA E DESVIO PADRAO
# EXECUTÁVEL
# GUI