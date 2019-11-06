from src.main.python.chessboard import creating_chessboard

print ('WELCOME TO AMEER\'S CHESS GAME')

white = input('Who will be white? (ENTER "player_1" or "player_2"')
if (white == 'player_1'):
    black = 'player_2'
else:
    black = 'player_1'

creating_chessboard.initialize_chessboard(white, black)

