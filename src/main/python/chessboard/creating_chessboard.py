import pandas as pd

def initialize_chessboard(white, black):
    chessboard = [[''] * 8 for i in range(0,8)]
    print (chessboard)

    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    indices = [i for i in range(1,9)]
    chessboard_table = pd.DataFrame(data=chessboard, columns=columns, index=indices)

    print (chessboard_table)

initialize_chessboard('player_1', 'player_2')