from src.main.python.chessboard import creating_chessboard
from src.main.python.chesspieces import chess_piece_moves
import sys

print('WELCOME TO AMEER\'S CHESS GAME\n')

chessboard = creating_chessboard.initialize_chessboard()
chessboard_with_pieces = creating_chessboard.initialize_chess_pieces(chessboard)
print(chessboard)
print('\n')

game_finished = False
counter = 1

while game_finished != True:

    if (counter % 2) == 1:
        player = 'White'
    else:
        player = 'Black'

    print('Player ' + player + '\'s turn')
    chess_piece = str(input('Which piece would you like to move? '))
    chess_piece_position = str(input('At? '))
    move_to = str(input('To? '))
    print('\n')
    chessboard, game_status, turn = chess_piece_moves.move_chess_piece(chess_piece, chess_piece_position, move_to, chessboard, player)
    print(chessboard)
    print('\n')

    if game_status == 'Checkmate':
        game_finished = True

    if turn == 'success':
        counter += 1
    else:
        print ('Player ' + player + '\nTry Again.')

sys.exit()

