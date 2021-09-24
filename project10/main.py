# Mostra a tabela de placar
def mostrarTabela():
    print('-' * 106)
    print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format('Nome', 'Vitorias', 'Empates', 'Derrotas', 'Pontos'))
    print('-' * 106)
    for jogador in jogadores:
        calculaPontos(jogador)
        print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'.format(jogador['nome'], jogador['vitorias'], jogador['empates'], jogador['derrotas'], jogador['pontos']))
        print('-' * 106)
    print()

# Mostra o menu de ações
def abrirMenu():
    menu = ['0 - Adicionar Vitória', '1 - Adicionar Empate', '2 - Adicionar Derrota', '3 - Limpar Tabela', '4 - Sair']
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

'''
# Adicionar um novo jogador na tabela {NÃO FUNCIONAL}

def adicionarJogador():
    nomeJogador = input("\nInsira o nome do jogador: ")
    
    jogador = {
        'nome': nomeJogador.capitalize(),
        'vitorias': 0,
        'empates': 0,
        'derrotas': 0,
        'pontos': 0
    }
    
    jogadores.append(jogador)   
'''
# Calcula a pontuação do jogador
def calculaPontos(jogador):
    pontuacao = (jogador['vitorias'] * 3) + jogador['empates'] - jogador['derrotas']
    jogador['pontos'] = pontuacao

# Adicionar Vitoria
def adicionarVitoria(jogadorGanhador):
    condicaoVitoria = False
    for jogador in jogadores:
        if jogador['nome'] == jogadorGanhador.capitalize():
            jogador['vitorias'] += 1
            calculaPontos(jogador)
            condicaoVitoria = True
    
    if condicaoVitoria:
        for jogador in jogadores:
            if jogador['nome'] != jogadorGanhador.capitalize():
                jogador['derrotas'] += 1
                calculaPontos(jogador)            
        mostrarTabela()

# Adicionar Empate
def adicionarEmpate():
    for jogador in jogadores:
        jogador['empates'] += 1
        calculaPontos(jogador)
                
    mostrarTabela()

# Adicionar Derrota
def adicionarDerrota(jogadorDerrotado):
    condicaoDerrota = False
    for jogador in jogadores:
        if jogador['nome'] == jogadorDerrotado.capitalize():
            jogador['derrotas'] += 1
            calculaPontos(jogador)
            condicaoDerrota = True
    
    if condicaoDerrota:
        for jogador in jogadores:
            if jogador['nome'] != jogadorDerrotado.capitalize():
                jogador['vitorias'] += 1
                calculaPontos(jogador)        
        mostrarTabela()

def limparPlacar():
    for jogador in jogadores:
        for dado in jogador.keys():
            if dado != 'nome':
                jogador[dado] = 0
    mostrarTabela()

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

mostrarTabela()

while True:
    abrirMenu()
    
    opcaoMenu = validarOpcao()
    
    if opcaoMenu == 0:
        ganhou = input("Qual jogador ganhou? ")       
        adicionarVitoria(ganhou)
    elif opcaoMenu == 1:
        adicionarEmpate()
    elif opcaoMenu == 2:
        perdeu = input("Qual jogador perdeu? ")
        adicionarDerrota(perdeu)
    elif opcaoMenu == 3:
        limparPlacar()
    elif opcaoMenu == 4:
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")

