import matplotlib.pyplot as plt

def gerar_grafico():
    # Ler os dados do arquivo txt
    with open('aproveitamento.txt', 'r') as file:
        lines = file.readlines()

    # Extrair os dados
    dias = []
    carros_produzidos = []
    carros_em_producao = []

    for line in lines:
        dados = line.split()
        dias.append(int(dados[0]))
        carros_produzidos.append(int(dados[1]))
        carros_em_producao.append(int(dados[2]))

    # Criar os gráficos
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Gráfico para Carros Produzidos
    axs[0].plot(dias, carros_produzidos, label='Carros Produzidos', color='tab:red')
    axs[0].set_ylabel('Quantidade de Carros Produzidos')
    axs[0].set_title('Produção de Carros ao Longo do Tempo')
    axs[0].legend()

    # Gráfico para Carros em Produção
    axs[1].plot(dias, carros_em_producao, label='Carros em Produção', color='tab:blue')
    axs[1].set_xlabel('Dias')
    axs[1].set_ylabel('Quantidade de Carros em Produção')
    axs[1].legend()

    plt.tight_layout()
    plt.show()