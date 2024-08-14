board = [[1,2,3],[4,5,6],[7,8,9]] #Tabuleiro
# board = [['x','o','x'],['o','x','o'],['x','o','x']]
locais = [1,2,3,4,5,6,7,8,9] #locais

# Função para substituir um valor em uma lista
def replace_value(board, old_value, new_value):
    for row in board:
        for i, item in enumerate(row):
            if item == old_value:
                row[i] = new_value

#função pra imprimira o tabuleiro
def imprimir(board):
    print("-" * 10)
    for row in board:
        print(" | ".join([str(cell) for cell in row]))
        print("-" * 10)

#Escolha se vai ser X ou O
def escolha():
    Jogadas = {1:None,2:None}
    player = input("Escolha X ou O: ").upper()
    if player == "X":
        Jogadas[1] = "X"
        Jogadas[2] = "O"        
        return Jogadas
    elif player == "O":
        Jogadas[1] = "O" 
        Jogadas[2] = "X"  
        return Jogadas
    
#verificar se tem um ganhador
def verificar_ganhador(board):
    # Verificar linhas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != None:
            print(f"Jogador {row[0]} venceu!")
            return True

    # Verificar colunas
    for col in range(len(board[0])):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] != None):
            print(f"Jogador {board[0][col]} venceu!")
            return True

    # Verificar diagonais
    if (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]):
        if board[1][1] != None:
            print(f"Jogador {board[1][1]} venceu!")
            return True

    return False

#Jogando
def jogar(players,locais):
        if players == 'X':
            while True:
                if len(locais) == 0:
                    break
                elif verificar_ganhador(board) == True:
                    break
                print(f"Vez do jogador (X)")
                jogada = int(input("Digite a posição: "))
                if jogada in locais:                    
                    locais.remove(jogada)
                    replace_value(board, jogada, 'X')
                    imprimir(board)
                    return locais
                else:
                    imprimir(board)
                    print("Posição já preenchida ou não valida")
                    print(f'Essas posições estão livres{locais}')
                    
        elif players == 'O':
            while True:
                if len(locais) == 0:
                    break
                elif verificar_ganhador(board) == True:
                    break
                print("Vez do jogador (O)")
                jogada = int(input("Digite a posição: "))
                if jogada in locais:
                    replace_value(board, jogada, 'O')
                    locais.remove(jogada)
                    imprimir(board)
                    return locais
                else:
                    imprimir(board)
                    print("Posição já preenchida ou não valida")
                    print(f'Essas posições estão livres{locais}')
                    
def main():
    players=escolha()
    print("Escolha onde vc quer colocar o X ou O")
    imprimir(board)
    while True:
        jogar(players[1],locais)
        jogar(players[2],locais)
        if verificar_ganhador(board) == True:
            break
        elif len(locais) == 0:
            print("Velha")
            break

main()
