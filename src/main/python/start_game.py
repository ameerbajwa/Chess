from src.main.python.chessboard import creating_chessboard
from src.main.python.chesspieces import creating_chess_pieces

print ('WELCOME TO AMEER\'S CHESS GAME')

chessboard = creating_chessboard.initialize_chessboard()
chessboard_with_pieces = creating_chessboard.initialize_chess_pieces(chessboard)
print (chessboard)

player_1 = input('Who will be player_1? (ENTER "White" or "Black") ')
if (player_1 == 'White'):
    player_2 = 'Black'
else:
    player_2 = 'White'

# game_finished = False
#
# while (game_finished != True):
#
#     player_1_chess_piece = input('Which piece to move? ')
#     player_1_move_to = input('To? ')
#     move_chess_piece(player_1_chess_piece, player_1_move_to)

