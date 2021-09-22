# Mostra a tabela de placar
def mostrarTabela():
    for elemento in tabela:
        for linha in elemento.values():
            print(linha)
    print()

# Adiciona um novo jogador na tabela
def adicionarJogador(jogador):
    calculaPontos(jogador)
    tabela.append({
        'linha1': '|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(jogador['nome'], jogador['vitorias'], jogador['empates'], jogador['derrotas'], jogador['pontos']),
        'linha2': '-' * 106,
    },)

# Calcula a pontuação do jogador
def calculaPontos(jogador):
    pontuacao = (jogador['vitorias'] * 3) + jogador['empates']
    jogador['pontos'] = pontuacao

# Mostra o menu de ações
def abrirMenu():
    menu = ['0 - Adicionar Vitória', '1 - Adicionar Empate', '2 - Adicionar Derrota', '3 - Adicionar Jogador', '4 - Limpar Tabela', '5 - Sair']
    for item in menu:
        print(item)
    print()

# validando escolha menu
def validarOpcao():
        while True:
            try:
                opcaoMenu = int(input("Escolha a opcão(numero): "))
            except (TypeError, ValueError):
                print("Valor inválido, digite um número válido.")
            else:
                print()
                break
        return opcaoMenu

tabela = [
    {
        'linha1': '-' * 106,
        'linha2': '|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('Nome', 'Vitorias', 'Empates', 'Derrotas', 'Pontos'),
        'linha3': '-' * 106,
    },
]

jogadores = [
    {
        'nome': 'Lucas',
        'vitorias': 3,
        'empates': 3,
        'derrotas': 1,
        'pontos': 0
    },
    {
        'nome': 'Adriana',
        'vitorias': 1,
        'empates': 3,
        'derrotas': 3,
        'pontos': 0
    },
]

adicionarJogador(jogadores[0])
adicionarJogador(jogadores[1])

mostrarTabela()

while True:
    abrirMenu()
    
    opcaoMenu = validarOpcao()
    
    if opcaoMenu == 0:
        pass
    elif opcaoMenu == 1:
        pass
    elif opcaoMenu == 2:
        pass
    elif opcaoMenu == 3:
        pass
    elif opcaoMenu == 4:
        pass
    elif opcaoMenu == 5:
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")

