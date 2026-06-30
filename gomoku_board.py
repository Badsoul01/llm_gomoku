from subprocess import check_output


class Board:

    def __init__(self):
        self.width = 15
        self.height = 15
        self.win_count = 5
        self.grid = {}


        for x in range(self.width):
            for y in range(self.height):
                self.grid[(x,y)] = "."

    def display(self):

        for x in range(self.width):
            for y in range(self.height):
                symbol = self.grid.get((x,y))

                print(symbol, end="")

            print()

    def checking_winnings(self,coords,symbol):

        x,y = coords
        directions = [
            (1,0),
            (0,1),
            (1,1),
            (1,-1)
        ]
        for dx,dy in directions:
            count_of_symbol = 1

            for step in range(1,5):
                if self.grid.get(x+step*dx,y+step*dy) == symbol:
                    count_of_symbol +=1

            for step in range(1,5):
                if self.grid.get(x-step*dx,y-step*dy) == symbol:
                    count_of_symbol +=1

            if count_of_symbol >=self.win_count:
                return True

        return False




test = Board()
test.display()