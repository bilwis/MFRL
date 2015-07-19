import uuid


class GameObject(object):

    def __init__(self):
        self.uuid = uuid.uuid4()


class Renderable(GameObject):

    def __init__(self, pos, char, colors):
        super().__init__()
        self.position = pos
        self.char = char
        self.fg_color = colors[0]

        if len(colors) == 2:
            self.bg_color = colors[1]
        else:
            self.bg_color = None
