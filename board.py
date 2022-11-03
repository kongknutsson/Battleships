HORI = "horizontal"
VERTI = "vertical"
EMPTY_CELL = " "
HIT_BOAT_CELL = "X"

class Board:

    def __init__(self) -> None:
        self.cells = self.create_cells()
        self.ship_types = {"B": 5, "F": 4, "C1": 3, "C2": 3, "C3": 3}

    def create_cells(self):
        return [ [EMPTY_CELL]*10 for i in range(10)]

    def populate_board_with_ships(self):
        for ship_name, ship_length in self.ship_types.items(): 
            print(f"Now placing ship {ship_name} with length {ship_length}")
            valid_placement = False 
            while not valid_placement:
                row = self.get_coords_from_user("row")
                col = self.get_coords_from_user("col")
                orientation = self.get_orientation_from_user()
                valid_placement = self.valid_ship_setting(col, row, orientation, ship_length)
                if valid_placement == False: 
                    print("Wrong choice of inputs, choose again for same boat.")
            self.set_ship(row, col, orientation, ship_length, ship_name)

    def set_ship(self, row, col, orientation, ship_length, ship_name):
        if orientation == HORI: 
            for offset in range(ship_length):
                self.cells[row][col - offset] = ship_name
        if orientation == VERTI: 
            for offset in range(ship_length):
                self.cells[row - offset][col] = ship_name
        self.print()

    def valid_ship_setting(self, col, row, orientation, ship_length):
        if orientation == HORI:
            if col < ship_length - 1:
                print("Horizontally wrong.")
                return False 
            for offset in range(ship_length):
                if self.cells[row][col - offset] != EMPTY_CELL:
                    print("Ship intersects another ship!")
                    return False
            
        if orientation == VERTI:
            if row < ship_length -1:
                print("Vertically wrong")
                return False 
            for offset in range(ship_length):
                print("Ship intersects another ship!")
                if self.cells[row - offset][col] != EMPTY_CELL:
                    return False 
        
        return True
           
    def get_orientation_from_user(self):
        orientation = input(f"Choose orientation ({HORI}, {VERTI}): ")
        while orientation not in [HORI, VERTI]:
            orientation = input(f"Wrong text entered! Choose orientation ({HORI}, {VERTI}): ")
        return orientation

    def get_coords_from_user(self, coord_type: str):
        inp = int(input(f"Choose {coord_type} (0 indexed): "))
        while inp < 0 or inp > len(self.cells) - 1:
            inp = int(input(f"You an out of bounds {coord_type} value, try again: "))
        return inp

    def shoot(self, row: int, col: int) -> bool:
        
        if self.cells[row][col] == EMPTY_CELL or self.cells[row][col] == HIT_BOAT_CELL:
            return False 
        print("You hit the ship!")
        hit_ship = self.cells[row][col]
        self.cells[row][col] = HIT_BOAT_CELL

        possible_cells = self.cells[row]
        for current_col in len(self.cells):
            current_cell = self.cells[row][current_col]
            possible_cells.append(current_cell)

        if possible_cells.count(hit_ship) == 0:
            print("This ship is sunk!")

        return True
        
    def won(self) -> bool:
        for ship_name in self.ship_types:
             for row in self.cells: 
                if ship_name in row: 
                    return False

    def print(self) -> None:
        for row in self.cells: 
            print(row)