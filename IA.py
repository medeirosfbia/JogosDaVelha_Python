#Feito com o AI Google Studio que é um ambiente de IA que Usa o modelo Gemini da Google
#Prompt Usado:
#Poderia gerar um jogo da velha Usando Python:
#-O jogo da velha precisa de um verificador se o jogo acabou,que indique se alguem ganhou ou se deu velha
#-O verificador será o norte para que o jogo pare
#-precisa ter um sistema para que não seja possivel jogar em um local que já foi jogado anteriormente
#-Tbm é necessario que o jogo seja por posições tipo
#1|2|3
#4|5|6
#7|8|9
#para que seja facil do jogador jogar
#-Vc pode usar todos os recursos que vc quiser para gerar esse jogo da velha

def print_board(board):
  """Imprime o tabuleiro do jogo."""
  print(f"{board[0]} | {board[1]} | {board[2]}")
  print("---------")
  print(f"{board[3]} | {board[4]} | {board[5]}")
  print("---------")
  print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board):
  """Verifica se há um vencedor."""
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                    (0, 3, 6), (1, 4, 7), (2, 5, 8),
                    (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
      return board[condition[0]]
  if " " not in board:
    return "Empate!"
  return None

def play_game():
  """Inicia e gerencia o jogo da velha."""
  board = [" " for _ in range(9)]
  current_player = "X"
  winner = None

  while winner is None:
    print_board(board)
    print(f"É a vez do jogador {current_player}")

    try:
      position = int(input("Escolha uma posição (1-9): ")) - 1
      if position not in range(9) or board[position] != " ":
        raise ValueError
      board[position] = current_player
      winner = check_win(board)
      current_player = "O" if current_player == "X" else "X"
    except ValueError:
      print("Jogada inválida. Tente novamente.")

  print_board(board)
  if winner == "Empate!":
    print("O jogo empatou!")
  else:
    print(f"O jogador {winner} venceu!")

if __name__ == "__main__":
  play_game()