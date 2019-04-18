import numpy as np
import graphics

class Tile():
    def __init__(self, row = 0, col = 0, prob = 0.0):
        self.set_row(row)
        self.set_col(col)
        self.set_prob(prob)

    def set_row(self, row = 0):
        self.row = row

    def set_col(self, col = 0):
        self.col = col

    def set_prob(self, prob = 0.0):
        self.prob = prob

    def draw(self, p1 = graphics.Point(0, 0), p2 = graphics.Point(0, 0)):
        return graphics.Rectangle(p1, p2)

    def __str__(self):
        return "Row: " + str(self.row) + "\nColumn: " + str(self.col) + "\nProbability: " + str(self.prob)

def test():
    t = Tile(0, 1)
    t.draw()
    print("Test")

if __name__ == "__main__":
    test()
