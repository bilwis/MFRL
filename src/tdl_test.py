#!/usr/bin/python3

"""
This is the main module/start script for MFRL.
"""

import tdl
import gamestate as state
import actor

SCREEN_WIDTH = 80  #: The width of the main console
SCREEN_HEIGHT = 50  #: The height of the main console
LIMIT_FPS = 20  #: The maximum fps


def draw(renderable_list):
    """
    This function draws all Renderable objects
    :param renderable_list: The list of objects to render.
    """

    main_console.clear()

    for re in renderable_list:
        re.draw(main_console)

    root.clear()
    root.blit(main_console)


if __name__ == '__main__':
    root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT)
    tdl.set_fps(LIMIT_FPS)

    gamestate = state.MainState()

    actors = []
    player = actor.Actor("Player", (1, 1), '@')
    actors.append(player)

    main_console = tdl.Console(SCREEN_WIDTH, SCREEN_HEIGHT)

    draw(actors)
    tdl.flush()

    while not tdl.event.is_window_closed():
        key_ev = tdl.event.key_wait()
        gamestate.handle_input(key_ev, player)

        draw(actors)
        tdl.flush()


