import numpy as np
moves = ['1','2','3','4','5','6','7','8','9']

### Function that returns one of four things: -1 if the game isn't finished yet, 0 if its a draw game,
### 1 if X wins and 2 if O wins
def is_solved(boardNp):
    # Verify lines
    for line in boardNp:
        if np.count_nonzero(line == 'x') == 3:
            return 1
        elif np.count_nonzero(line == 'o') == 3:
            return 2

    # Verify columns
    for i in range(0,3):
        if np.count_nonzero(boardNp[:,i] == 'x') == 3:
            return 1
        elif np.count_nonzero(boardNp[:,i] == 'o') == 3:
            return 2

    # Verify diagonals
    if np.count_nonzero(np.diag(boardNp) == 'x') == 3 or np.count_nonzero(np.fliplr(boardNp).diagonal() == 'x')== 3:
        return 1
    elif np.count_nonzero(np.diag(boardNp) == 'o') == 3 or np.count_nonzero(np.fliplr(boardNp).diagonal() == 'o')== 3:
        return 2

    # Verify if its not finished yet or if its draw (in that order)
    if len(moves) != 0:
        return -1
    else:
        return 0


#print array
def print_out(board):
    print("-" * 10)
    for row in board:
        print(" | ".join([str(cell) for cell in row]))
        print("-" * 10)

#function game
def playing(game,player):
    # Runs while the game isn't fished yet
    while is_solved(game) == -1:
        print(f"Vez do jogador {player}")

        # Runs until the player give a acceptable input
        while True:
            if is_solved(game) != -1:
                break
            else:
                print_out(game)
                locations = input("Onde vc deseja jogar? (1-9):")

                # Here whe test if the place that the player put is empty
                if locations in moves:   # Yes --> the place will be replaced by its symbol
                    moves.remove(locations)
                    game[game == locations] = player
                    if player == 'x': player = 'o'
                    else: player = 'x'
                else:                             # No --> He will have to put it all over again
                    print('Insira num local vazio/valido!')
                


# main function
def main():
    # Inicialize the game board
    game = np.array([['1','2','3'], ['4','5','6'], ['7','8','9']])
    player = 'x'  # player that starts the game

    playing(game, player)  # Call the game function
    # And in the end, when the function returns that the game ended we have te results
    # We print the final board and the winner
    print_out(game)
    if is_solved(game) == 1:
        print(f'O vencedor é o jogador X')
        
    elif is_solved(game) == 2:
        print(f'O vencedor é o jogador O')
        
    else: 
        print(f'O jogo deu velha')
        
main()
