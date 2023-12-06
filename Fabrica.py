'''
Final work of LFA

Members:
    Santiago Cardoso
    Lucas Gabriel
'''

import os
import random
import time
import Linha_de_producao_de_veiculos as Linha
import Grafico as grafico

linha = Linha.LinhaProducao()

#  Pilha de dias
pilha_dias = ["D"] * Linha.quantidade_dias_simulacao

if os.path.exists("relatorio_diario.txt"): #  Deleta o arquivo anterior do relatório diário, caso ele exista
    os.remove("relatorio_diario.txt")

if os.path.exists("aproveitamento.txt"): #  Deleta o arquivo anterior do aproveitamento mensal, caso ele exista
    os.remove("aproveitamento.txt")

#  Simulação de produção de carros
while pilha_dias:
    start_time = time.time()

    #  Desempilhar um "D" para representar o dia que passa
    pilha_dias.pop()

    tipos_carros = ["Sedan", "SUV", "Hatch", "Minivan", "Fusca"]
    modelos = ["MODELO A", "MODELO B", "MODELO C", "MODELO D"]

    fita = []

    for _ in range(Linha.quantidade_carros):
        tipo_carro_aleatorio = random.choice(tipos_carros)
        modelo_aleatorio = random.choice(modelos)
        fita.append([tipo_carro_aleatorio, modelo_aleatorio])

    for element in fita:
        linha.produzir_carro(element[0], element[1])
    
    end_time = time.time()
    tempo_de_execucao = end_time - start_time

    #  Gerar relatório diário
    linha.relatorio_diario(tempo_de_execucao / Linha.quantidade_carros)

    input("\nAperte ENTER para passar o dia...")
    os.system("cls")

    if not pilha_dias:
        print("Cronograma de montagens finalizado!\n")

        if (not linha.pilha_carros_em_producao):
            print("Fábrica conseguiu realizar todo o processo de montagem!")
        else:
            print("Fábrica não conseguiu atingir a cota de veículos montados nos dias!")

        input("Aperte ENTER para fechar a fábrica...")
        os.system("cls")
        grafico.gerar_grafico()