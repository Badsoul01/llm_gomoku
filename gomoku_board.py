class Board:

    def __init__(self):
        self.width = 15
        self.height = 15
        self.grid = {}

        for x in range(self.width):
            for y in range(self.height):
                self.grid[(x,y)] = " "

    def display(self):

        for x in range(self.width):
            for y in range(self.height):
                symbol = self.grid.get((x,y))

                print(symbol, end="")

            print()

test = Board()
test.display()