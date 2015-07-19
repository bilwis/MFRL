import colors
from operator import add
import tdl


class Actor(object):

    def __init__(self, name, pos, char, color=colors.WHITE, *args):
        self.position = pos
        self.name = name
        self.char = char
        self.color = color

    def move(self, dx, dy):
        self.position = tuple(map(add, (dx, dy), self.position))

    def draw(self, console):
        console.set_colors(self.color, colors.BLACK)
        console.draw_char(self.position[0], self.position[1], self.char)

    def update(self):
        pass

