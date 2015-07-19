from tdl import event


class GameState(object):

    def __init__(self):
        pass

    def handle_input(self, key_event, *args):
        raise NotImplementedError("GameState child has not implemented input handling!")


class MainState(GameState):

    def __init__(self):
        pass

    def handle_input(self, key_event, player):
        if key_event.key == 'KP8':
            player.move(0, -1)
        elif key_event.key == 'KP2':
            player.move(0, 1)
        elif key_event.key == 'KP4':
            player.move(-1, 0)
        elif key_event.key == 'KP6':
            player.move(1, 0)

