import colors
import game_object as obj
from operator import add
import tdl


class Actor(obj.Renderable):

    def __init__(self, name, pos, char, color_tuple=(colors.WHITE, None), *args):
        super().__init__(pos, char, color_tuple)
        self.name = name

    def move(self, dx, dy):
        self.position = tuple(map(add, (dx, dy), self.position))

    def draw(self, console):
        console.set_colors(self.fg_color, self.bg_color)
        console.draw_char(self.position[0], self.position[1], self.char)

    def update(self):
        pass

