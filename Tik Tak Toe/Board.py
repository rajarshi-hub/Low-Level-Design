
from Cell import Cell


class Board:

    def __init__(self):
        self.cells = [[Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()], [Cell(), Cell(), Cell()]]

    def populate_cell(self,x,y, choice):
        if x < 0 or  y < 0 or x >= 3 or y >= 3:
            return False
        if self.cells[x][y].val != '-':
            return False
        self.cells[x][y].val = choice
        return True

    def check_rows(self, choice):

        for i in range(0,3):
            j = 0
            while j < 3:
                if self.cells[i][j].val != choice:
                    break
                j+=1
            if j == 3:
                return True

        return False

    def check_column(self, choice):

        for i in range(0, 3):
            j = 0
            while j < 3:
                if self.cells[j][i].val != choice:
                    break
                j += 1
            if j == 3:
                return True

        return False

    def check_diagonal(self, choice):

        i = 0
        j = 0
        while i < 3:
            if self.cells[i][j].val != choice:
                break
            i += 1
            j += 1
        if i == 3:
            return True
        i = 0
        j = 2
        while i < 3:
            if self.cells[i][j].val != choice:
                break
            i += 1
            j -= 1
        return i == 3

    def all_cells_filled(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.cells[i][j].val == '-':
                    return False
        return True

    def print_board(self):
        for i in range(0,3):
            for j in range(0,3):
                print(self.cells[i][j].val, end=' ')
            print('')