from board import Board

board_1 = Board()
board_2 = Board()

board_1.populate_board_with_ships()
board_2.populate_board_with_ships()

someone_won = board_1.won() or board_2.won()

while not someone_won:
    board_1.shoot()
    board_2.shoot()
    someone_won = board_1.won() or board_2.won()