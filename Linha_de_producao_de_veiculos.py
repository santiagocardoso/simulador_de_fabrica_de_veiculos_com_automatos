'''
Final work of LFA

Members:
    Santiago Cardoso
    Lucas Gabriel
'''

''' _.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~._ '''
#  Inicialização do simulador, defina os seguintes critérios:
quantidade_dias_simulacao = 5 #  Número de dias que a simulação leva
quantidade_carros = 5 #  Número de carros limite que a fábrica consegue produzir
''' _.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~.__.~"~._.~"~._.~"~._.~"~._ '''

# -*- coding: utf-8 -*-

#  m = quantidade_carros * quantidade_dias_simulacao
m = 1

import random

veiculos = {
    "SUV":
    """
    ____/   ___
   |_   \__'  _\\
   `-(*)----(*)'

        SUV
    """,

    "Hatch":
    """
        ____
      _/____]__
     |_v'_]"__"]
     `UJ-uJ--uJ
        
        HATCH
    """,

    "Sedan":
    """
        ____
      _/____)__
     |_v'_)"__")
     `UJ-uJ--uJ

        SEDAN
    """,

    "Minivan":
    """
       _____
      i_____i
      ["___"]
      |J---L|
      
      MINIVAN
    """,

    "Fusca":
    """
      .(___).
     (O\_!_/O)

       FUSCA
    """
}

class Fornecedora:
    def __init__(self):
        self.estoque_pneus = random.randint(1, 4) * m
        self.estoque_latarias = random.randint(20, 100) * m
        self.estoque_bancos = random.randint(500, 1123) * m
        self.estoque_motores = random.randint(5, 30) * m
        self.estoque_baterias = random.randint(10, 20) * m
        self.estoque_freios = random.randint(20, 53) * m
        self.estoque_suspensoes = random.randint(35, 70) * m
        self.estoque_direcoes_eletricas = random.randint(10, 20) * m
        self.estoque_direcoes_mecanicas = random.randint(20, 36) * m
        self.estoque_direcoes_hidraulicas = random.randint(5, 15) * m
        self.estoque_vidros = random.randint(1500, 3000) * m
        self.estoque_portas = random.randint(260, 520) * m
        self.estoque_chassi = random.randint(400, 802) * m
        self.estoque_ar_condicionado = random.randint(10, 20) * m
        self.estoque_farois = random.randint(216, 433) * m
        self.estoque_retrovisor = random.randint(50, 100) * m
        self.estoque_cambio_manual = random.randint(49, 99) * m
        self.estoque_cambio_automatico = random.randint(40, 80) * m


    def pedir_pecas(self, tipo, quantidade):
            
            estoque = getattr(self,tipo)

            if(estoque == 0):
                return 0

            if(quantidade>estoque):
                setattr(self,tipo, 0)
                return estoque
                
            setattr(self,tipo,estoque-quantidade)
            return quantidade

    def to_string(self):
        return f"==============================================================\nEstoque restante da fornecedora:\nPneus:{self.estoque_pneus}\nLatarias:{self.estoque_latarias}\nBancos:{self.estoque_bancos}\nMotores:{self.estoque_motores}\nBaterias:{self.estoque_baterias}\nFreios:{self.estoque_freios}\nSuspensoes:{self.estoque_suspensoes}\nDireções elétricas:{self.estoque_direcoes_eletricas}\nDireções hidráulicas:{self.estoque_direcoes_hidraulicas}\nDireções mecânicas:{self.estoque_direcoes_mecanicas}\nVidros:{self.estoque_vidros}\nPortas:{self.estoque_portas}\nChassis:{self.estoque_chassi}\nAres condicionados:{self.estoque_ar_condicionado}\nFaróis:{self.estoque_farois}\nRetrovisores:{self.estoque_retrovisor}\nCâmbios manuais:{self.estoque_cambio_manual}\nCâmbios automáticos:{self.estoque_cambio_automatico}\n==============================================================\n"


class Carro:
    #  TIPOS = Sedan, Hatch, SUV, Minivan, Fusca
    #  MODELO A = direção elétrica + automático + 4 portas + ar condicionado
    #  MODELO B = direção elétrica + manual + 4 portas + ar condicionado
    #  MODELO C = direção hidráulica + manual + 2 portas + ventilaço
    #  MODELO D = direção mecânica + manual + 4 portas + ventilacao
    
    def __init__(self, tipo, modelo):
        self.tipo = tipo
        self.modelo = modelo
        self.completado = False
        self.direcao = "eletrica"
        self.cambio = "automatico"
        self.qtd_portas = 4
        self.ar = "ar condicionado"

        self.pneus = 0
        self.lataria = 0
        self.bancos = 0
        self.motor = 0
        self.bateria = 0
        self.freios = 0
        self.suspensoes = 0
        self.direcao_tipo = 0
        self.vidros = 0
        self.portas = 0
        self.chassi = 0
        self.ar_condicionado = 0
        self.farois = 0
        self.retrovisores = 0
        self.cambio_tipo = 0

        self.pecas_faltantes = {}
        
        if modelo == "MODELO B":
            self.cambio = "manual"
            
        elif modelo == "MODELO C":
            self.direcao = "hidraulica"
            self.cambio = "manual"
            self.qtd_portas = 2
            self.ar = "ventilacao"
            
        elif modelo == "MODELO D":
            self.direcao = "mecanica"
            self.cambio = "manual"
            self.ar = "ventilacao"
            
    def to_string(self):
        return f"{self.tipo}, direcao {self.direcao}, {self.cambio}, {self.qtd_portas} portas, {self.ar}"


class LinhaProducao:
    def __init__(self):
        self.fornecedora = Fornecedora()

        self.pilha_carros = []
        self.pilha_carros_finalizados = []
        self.pilha_carros_em_producao = []

        self.estoque_pneus = random.randint(100, 500) * m
        self.estoque_latarias = random.randint(50, 300) * m
        self.estoque_bancos = random.randint(500, 3000) * m
        self.estoque_motores = random.randint(25, 100) * m
        self.estoque_baterias = random.randint(100, 500) * m
        self.estoque_freios = random.randint(200, 1000) * m
        self.estoque_suspensoes = random.randint(300, 1000) * m
        self.estoque_direcoes_eletricas = random.randint(10, 50) * m
        self.estoque_direcoes_mecanicas = random.randint(10, 50) * m
        self.estoque_direcoes_hidraulicas = random.randint(10, 50) * m
        self.estoque_vidros = random.randint(500, 1500) * m
        self.estoque_portas = random.randint(250, 750) * m
        self.estoque_chassi = random.randint(500, 1500) * m
        self.estoque_ar_condicionado = random.randint(10, 50) * m
        self.estoque_farois = random.randint(200, 800) * m
        self.estoque_retrovisor = random.randint(100, 400) * m
        self.estoque_cambio_manual = random.randint(100, 300) * m
        self.estoque_cambio_automatico = random.randint(100, 300) * m

        self.dia = 1

    
    def to_string(self):
        return f"==============================================================\nEstoque restante da linha de produção:\nPneus:{self.estoque_pneus}\nLatarias:{self.estoque_latarias}\nBancos:{self.estoque_bancos}\nMotores:{self.estoque_motores}\nBaterias:{self.estoque_baterias}\nFreios:{self.estoque_freios}\nSuspensoes:{self.estoque_suspensoes}\nDireções elétricas:{self.estoque_direcoes_eletricas}\nDireções hidráulicas:{self.estoque_direcoes_hidraulicas}\nDireções mecânicas:{self.estoque_direcoes_mecanicas}\nVidros:{self.estoque_vidros}\nPortas:{self.estoque_portas}\nChassis:{self.estoque_chassi}\nAres condicionados:{self.estoque_ar_condicionado}\nFaróis:{self.estoque_farois}\nRetrovisores:{self.estoque_retrovisor}\nCâmbios manuais:{self.estoque_cambio_manual}\nCâmbios automáticos:{self.estoque_cambio_automatico}\n==============================================================\n"


    def produzir_carro(self, tipo, modelo):
        self.terminar_carros_incompletos()
        carro = Carro(tipo, modelo)
        self.pilha_carros.append(carro)
        self.executar_producao(carro)

    def terminar_carros_incompletos(self):
        for carro in self.pilha_carros_em_producao:
            self.executar_producao(carro)


    def executar_producao(self, carro, falha = False, local_de_falha = None):
        if(quantidade_carros > 1000):
            erro = random.randint(1,1000) #  Erro aleatório na máquina de produção de 0.1%
        elif(quantidade_carros > 100 and quantidade_carros <= 1000):
            erro = random.randint(1,500) #  Erro aleatório na máquina de produção de 0.5%   
        elif(quantidade_carros > 10 and quantidade_carros <= 100):
            erro = random.randint(1, 100) #  Erro de 1%
        else:
            erro = random.randint(1, 20) #  Erro de 5%
        
        if(falha or erro == 14): #  Se cair em 14 é considerado como erro da máquina
            carro.completado = False
            return

        if(self.estoque_chassi == 0):
            self.estoque_chassi = self.fornecedora.pedir_pecas("estoque_chassi",10)
            falha = True
            carro.pecas_faltantes["chassi"] = 1

        #  Simulação das etapas de produção
        elif(self.estoque_chassi > 0):
            self.estoque_chassi -= 1
            carro.chassi = 1
            
        
        if(self.estoque_pneus < 4): #  Se temos menos do que 4 pneus
            if(self.estoque_pneus == 0):  # Se o estoque for igual a 0
                self.estoque_pneus = self.fornecedora.pedir_pecas("estoque_pneus",10) #  Pedimos M (quantidade_veiculos * quantidade_dias_simulacao) peças para a fornecedora
                falha = True
                carro.pecas_faltantes["pneus"] = 4

            else: #  Se o estoque tiver > 0 e < 4
                carro.pneus = self.estoque_pneus #  Recebe o estoque
                self.estoque_pneus = 0 #  Zera o estoque
                falha = True
                carro.pecas_faltantes["pneus"] = 4 - carro.pneus 
        
        elif(self.estoque_pneus >= 4):
            self.estoque_pneus -= 4
            carro.pneus = 4

        if(self.estoque_motores == 0):
            self.estoque_motores = self.fornecedora.pedir_pecas("estoque_motores",10)
            falha = True
            carro.pecas_faltantes["motor"] = 1    

        elif(self.estoque_motores > 0):
            self.estoque_motores -= 1
            carro.motor = 1
            
        
        if(self.estoque_baterias == 0):
            self.estoque_baterias = self.fornecedora.pedir_pecas("estoque_baterias",10)
            falha = True
            carro.pecas_faltantes["bateria"] = 1

        elif(self.estoque_baterias > 0):
            self.estoque_baterias -= 1
            carro.bateria = 1
        

        if(self.estoque_freios < 4):
            if(self.estoque_freios == 0):
                self.estoque_freios = self.fornecedora.pedir_pecas("estoque_freios", 10)
                falha = True
                carro.pecas_faltantes["freios"] = 4
            else:
                carro.freios = self.estoque_freios
                self.estoque_freios = 0
                falha = True
                carro.pecas_faltantes["freio"] = 4 - carro.freios
        
        elif(self.estoque_freios >= 4):
            self.estoque_freios -= 4
            carro.freios = 4


        if(self.estoque_suspensoes < 4):
            if(self.estoque_suspensoes == 0):
                self.estoque_suspensoes = self.fornecedora.pedir_pecas("estoque_suspensoes", 10)
                falha = True
                carro.pecas_faltantes["suspensoes"] = 4
            else:
                carro.suspensoes = self.estoque_suspensoes
                self.estoque_suspensoes = 0
                falha = True
                carro.pecas_faltantes["suspensoes"] = 4 - carro.suspensoes
        
        elif(self.estoque_suspensoes >= 4):
            self.estoque_suspensoes -= 4
            carro.suspensoes = 4

        
        if(self.estoque_bancos < 5):
            if(self.estoque_bancos == 0):
                self.estoque_bancos = self.fornecedora.pedir_pecas("estoque_bancos", 10)
                falha = True
                carro.pecas_faltantes["bancos"] = 5
            else:
                carro.bancos = self.estoque_bancos
                self.estoque_bancos = 0
                falha = True
                carro.pecas_faltantes["bancos"] = 5 - carro.bancos
        
        elif(self.estoque_bancos >= 5):
            self.estoque_bancos -= 5
            carro.bancos = 5

        if(self.estoque_latarias == 0):
            self.estoque_latarias = self.fornecedora.pedir_pecas("estoque_latarias",10)
            falha = True
            carro.pecas_faltantes["lataria"] = 1

        elif(self.estoque_latarias > 0):
            self.estoque_latarias -= 1
            carro.lataria = 1
            

        if(self.estoque_farois < 4):
            if(self.estoque_farois == 0):
                self.estoque_farois = self.fornecedora.pedir_pecas("estoque_farois", 10)
                falha = True
                carro.pecas_faltantes["farois"] = 4
            else:
                carro.farois = self.estoque_farois
                self.estoque_farois = 0
                falha = True
                carro.pecas_faltantes["farois"] = 4 - carro.farois
        
        elif(self.estoque_farois >= 4):
            self.estoque_farois -= 4
            carro.farois = 4


        if(self.estoque_retrovisor < 3):
            if(self.estoque_retrovisor == 0):
                self.estoque_retrovisor = self.fornecedora.pedir_pecas("estoque_retrovisor", 10)
                falha = True
                carro.pecas_faltantes["retrovisores"] = 3
            else:
                carro.retrovisores = self.estoque_retrovisor
                self.estoque_retrovisor = 0
                falha = True
                carro.pecas_faltantes["retrovisores"] = 3 - carro.retrovisores
        
        elif(self.estoque_retrovisor >= 3):
            self.estoque_retrovisor -= 3
            carro.retrovisores = 3 
                

        #  A partir do autômato direção temos 4 transções para cada autômato, onde cada transição representa um modelo
        if(carro.modelo == "MODELO A"):

            if(self.estoque_direcoes_eletricas == 0):
                self.estoque_direcoes_eletricas = self.fornecedora.pedir_pecas("estoque_direcoes_eletricas",10)
                falha = True
                carro.pecas_faltantes["direcao_eletrica"] = 1

            elif(self.estoque_direcoes_eletricas>0):
                self.estoque_direcoes_eletricas -= 1
                carro.direcao_tipo = 1


            if(self.estoque_portas < 4):
                if(self.estoque_portas == 0):
                    self.estoque_portas = self.fornecedora.pedir_pecas("estoque_portas", 10)
                    falha = True
                    carro.pecas_faltantes["portas"] = 4
                else:
                    carro.portas = self.estoque_portas
                    self.estoque_portas = 0
                    falha = True
                    carro.pecas_faltantes["portas"] = 4 - carro.portas
        
            elif(self.estoque_portas >= 4):
                self.estoque_portas -= 4
                carro.portas = 4


            if(self.estoque_vidros < 6):
                if(self.estoque_vidros == 0):
                    self.estoque_vidros = self.fornecedora.pedir_pecas("estoque_vidros", 10)
                    falha = True
                    carro.pecas_faltantes["vidros"] = 6
                else:
                    carro.vidros = self.estoque_vidros
                    self.estoque_vidros = 0
                    falha = True
                    carro.pecas_faltantes["vidros"] = 6 - carro.vidros
        
            elif(self.estoque_vidros >= 6):
                self.estoque_vidros -= 6
                carro.vidros = 6
                
            if(self.estoque_cambio_automatico == 0):
                self.estoque_cambio_automatico = self.fornecedora.pedir_pecas("estoque_cambio_automatico",10)
                falha = True
                carro.pecas_faltantes["cambio_automatico"] = 1

            elif(self.estoque_cambio_automatico>0):    
                self.estoque_cambio_automatico -= 1
                carro.cambio = 1
            
            if(self.estoque_ar_condicionado == 0):
                self.estoque_ar_condicionado = self.fornecedora.pedir_pecas("estoque_ar_condicionado",10)
                falha = True
                carro.pecas_faltantes["ar_condicionado"] = 1

            elif(self.estoque_ar_condicionado>0):    
                self.estoque_ar_condicionado -= 1
                carro.ar_condicionado = 1
            
            
        if (carro.modelo == "MODELO B"):

            if(self.estoque_direcoes_eletricas == 0):
                self.estoque_direcoes_eletricas = self.fornecedora.pedir_pecas("estoque_direcoes_eletricas",10)
                falha = True
                carro.pecas_faltantes["direcao_eletrica"] = 1

            elif(self.estoque_direcoes_eletricas>0):
                self.estoque_direcoes_eletricas -= 1
                carro.direcao_tipo = 1
            

            if(self.estoque_portas < 4):
                if(self.estoque_portas == 0):
                    self.estoque_portas = self.fornecedora.pedir_pecas("estoque_portas", 10)
                    falha = True
                    carro.pecas_faltantes["portas"] = 4
                else:
                    carro.portas = self.estoque_portas
                    self.estoque_portas = 0
                    falha = True
                    carro.pecas_faltantes["portas"] = 4 - carro.portas
        
            elif(self.estoque_portas >= 4):
                self.estoque_portas -= 4
                carro.portas = 4


            if(self.estoque_vidros < 6):
                if(self.estoque_vidros == 0):
                    self.estoque_vidros = self.fornecedora.pedir_pecas("estoque_vidros", 10)
                    falha = True
                    carro.pecas_faltantes["vidros"] = 6
                else:
                    carro.vidros = self.estoque_vidros
                    self.estoque_vidros = 0
                    falha = True
                    carro.pecas_faltantes["vidros"] = 6 - carro.vidros
        
            elif(self.estoque_vidros >= 6):
                self.estoque_vidros -= 6
                carro.vidros = 6

            if(self.estoque_cambio_manual == 0):
                self.estoque_cambio_manual = self.fornecedora.pedir_pecas("estoque_cambio_manual",10)
                falha = True
                carro.pecas_faltantes["cambio_manual"] = 1

            elif(self.estoque_cambio_manual>0):    
                self.estoque_cambio_manual -= 1
                carro.cambio = 1

            if(self.estoque_ar_condicionado == 0):
                self.estoque_ar_condicionado = self.fornecedora.pedir_pecas("estoque_ar_condicionado",10)
                falha = True
                carro.pecas_faltantes["ar_condicionado"] = 1

            elif(self.estoque_ar_condicionado>0):    
                self.estoque_ar_condicionado -= 1
                carro.ar_condicionado = 1


        if(carro.modelo == "MODELO C"):

            if(self.estoque_direcoes_hidraulicas == 0):
                self.estoque_direcoes_hidraulicas = self.fornecedora.pedir_pecas("estoque_direcoes_hidraulicas",10)
                falha = True
                carro.pecas_faltantes["direcao_hidraulica"] = 1

            elif(self.estoque_direcoes_hidraulicas>0):
                self.estoque_direcoes_hidraulicas -= 1
                carro.direcao_tipo = 1
            

            if(self.estoque_portas < 2):
                if(self.estoque_portas == 0):
                    self.estoque_portas = self.fornecedora.pedir_pecas("estoque_portas", 10)
                    falha = True
                    carro.pecas_faltantes["portas"] = 2
                else:
                    falha = True
                    carro.portas = self.estoque_portas
                    self.estoque_portas = 0
                    carro.pecas_faltantes["portas"] = 2 - carro.portas
        
            elif(self.estoque_portas >= 2):
                self.estoque_portas -= 2
                carro.portas = 2
            

            if(self.estoque_vidros < 4):
                if(self.estoque_vidros == 0):
                    self.estoque_vidros = self.fornecedora.pedir_pecas("estoque_vidros", 10)
                    falha = True
                    carro.pecas_faltantes["vidros"] = 4
                else:
                    carro.vidros = self.estoque_vidros
                    self.estoque_vidros = 0
                    falha = True
                    carro.pecas_faltantes["vidros"] = 4 - carro.vidros
        
            elif(self.estoque_vidros >= 4):
                self.estoque_vidros -= 6
                carro.vidros = 4

            if(self.estoque_cambio_manual == 0):
                self.estoque_cambio_manual = self.fornecedora.pedir_pecas("estoque_cambio_manual",10)
                falha = True
                carro.pecas_faltantes["cambio_manual"] = 1

            elif(self.estoque_cambio_manual>0):    
                self.estoque_cambio_manual -= 1
                carro.cambio = 1

            
        if(carro.modelo == "MODELO D"):

            if(self.estoque_direcoes_mecanicas == 0):
                self.estoque_direcoes_mecanicas = self.fornecedora.pedir_pecas("estoque_direcoes_mecanicas",10)
                falha = True
                carro.pecas_faltantes["direcao_mecanica"] = 1

            elif(self.estoque_direcoes_mecanicas>0):
                self.estoque_direcoes_mecanicas -= 1
                carro.direcao_tipo = 1


            if(self.estoque_portas < 4):
                if(self.estoque_portas == 0):
                    self.estoque_portas = self.fornecedora.pedir_pecas("estoque_portas", 10)
                    falha = True
                    carro.pecas_faltantes["portas"] = 4
                else:
                    carro.portas = self.estoque_portas
                    self.estoque_portas = 0
                    falha = True
                    carro.pecas_faltantes["portas"] = 4 - carro.portas

            elif(self.estoque_portas >= 4):
                self.estoque_portas -= 4
                carro.portas = 4


            if(self.estoque_vidros < 6):
                if(self.estoque_vidros == 0):
                    self.estoque_vidros = self.fornecedora.pedir_pecas("estoque_vidros", 10)
                    falha = True
                    carro.pecas_faltantes["vidros"] = 6
                else:
                    carro.vidros = self.estoque_vidros
                    self.estoque_vidros = 0
                    falha = True
                    carro.pecas_faltantes["vidros"] = 6 - carro.vidros
        
            elif(self.estoque_vidros >= 6):
                self.estoque_vidros -= 6
                carro.vidros = 6

            if(self.estoque_cambio_manual == 0):
                self.estoque_cambio_manual = self.fornecedora.pedir_pecas("estoque_cambio_manual",10)
                falha = True
                carro.pecas_faltantes["cambio_manual"] = 1

            elif(self.estoque_cambio_manual>0):    
                self.estoque_cambio_manual -= 1
                carro.cambio = 1

        #  Caso ocorra uma falha na montagem do veículo por conta de falta de peças
        if(falha):
            self.estoque_chassi += carro.chassi
            self.estoque_pneus += carro.pneus
            self.estoque_motores += carro.motor
            self.estoque_baterias += carro.bateria
            self.estoque_freios += carro.freios            
            self.estoque_suspensoes += carro.suspensoes
            self.estoque_bancos += carro.bancos
            self.estoque_latarias += carro.lataria
            self.estoque_farois += carro.farois
            self.estoque_retrovisor += carro.retrovisores

            if(carro.modelo == "A"):
                self.estoque_direcoes_eletricas+= carro.direcao_tipo
                self.estoque_cambio_automatico += carro.cambio_tipo
                self.estoque_portas += carro.portas
                self.estoque_vidros += carro.vidros
                self.estoque_ar_condicionado += carro.ar_condicionado

                
            if(carro.modelo == "B"):
                self.estoque_direcoes_eletricas += carro.direcao_tipo
                self.estoque_cambio_manual += carro.cambio_tipo
                self.estoque_portas += carro.portas
                self.estoque_vidros += carro.vidros
                self.estoque_ar_condicionado += carro.ar_condicionado

            if(carro.modelo == "C"):
                self.estoque_direcoes_hidraulicas += carro.direcao_tipo
                self.estoque_cambio_manual += carro.cambio_tipo
                self.estoque_portas += carro.portas
                self.estoque_vidros += carro.vidros


            if(carro.modelo == "D"):
                self.estoque_direcoes_mecanicas += carro.direcao_tipo
                self.estoque_cambio_manual += carro.cambio_tipo
                self.estoque_portas += carro.portas
                self.estoque_vidros += carro.vidros

            
            carro.completado = False
            return
        
        carro.completado = True  #  Simulação de finalização
        self.pilha_carros_finalizados.append(carro)
        self.pilha_carros.remove(carro)
        if carro in self.pilha_carros_em_producao:
            self.pilha_carros_em_producao.remove(carro)
    

    def relatorio_diario(self, tempo_de_execucao):
        self.pilha_carros_em_producao = [carro for carro in self.pilha_carros if not carro.completado]

        Sedan = [carro for carro in self.pilha_carros_finalizados if carro.tipo == "Sedan"]
        Hatch = [carro for carro in self.pilha_carros_finalizados if carro.tipo == "Hatch"]
        SUV = [carro for carro in self.pilha_carros_finalizados if carro.tipo == "SUV"]
        Minivan = [carro for carro in self.pilha_carros_finalizados if carro.tipo == "Minivan"]
        Fusca = [carro for carro in self.pilha_carros_finalizados if carro.tipo == "Fusca"]
        
        if (tempo_de_execucao > 0):
            relatorio = (f"\n==============================================================\nRelatório Diário - Dia {self.dia}:\nTempo (simulação) de fábricação por veículo: {tempo_de_execucao:.10f} segundos\nTempo (simulação) total: {tempo_de_execucao * quantidade_carros:.10f} segundos\n")
        else:
            relatorio = (f"\n==============================================================\nRelatório Diário - Dia {self.dia}:\n")

        relatorio += "==============================================================\n"
        relatorio += f"Carros Finalizados: {len(self.pilha_carros_finalizados)}\n"
        relatorio += "Detalhes:\n\n"
        
        relatorio += "Sedan:\n"
        for carro in Sedan:
            relatorio += f"{carro.to_string()}\n"
        
        relatorio += "\nHatch:\n"
        for carro in Hatch:
            relatorio += f"{carro.to_string()}\n"
        
        relatorio += "\nSUV:\n"
        for carro in SUV:
            relatorio += f"{carro.to_string()}\n"

        relatorio += "\nMinivan:\n"
        for carro in Minivan:
            relatorio += f"{carro.to_string()}\n"

        relatorio += "\nFusca:\n"
        for carro in Fusca:
            relatorio += f"{carro.to_string()}\n"

        relatorio += f"\nCarros em Produção: {len(self.pilha_carros_em_producao)}\n"
        relatorio += "Detalhes:\n"
        for carro in self.pilha_carros_em_producao:
            relatorio += f"- Tipo: {carro.tipo}, Modelo: {carro.modelo} - Em produção\n"
        
        relatorio += "==============================================================\n"

        # Save the daily report to a text file
        file_name = "relatorio_diario.txt"
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(relatorio)

        aproveitamento = f"{self.dia} {len(self.pilha_carros_finalizados)} {len(self.pilha_carros_em_producao)}\n"

        # Criar gráfico de aproveitamento
        file_name = "aproveitamento.txt"
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(aproveitamento)

        print(relatorio)

        while self.pilha_carros_finalizados:
            carro = self.pilha_carros_finalizados.pop(0) #  Remove o elemento do topo
            print(veiculos[carro.tipo])
        
        self.dia += 1
