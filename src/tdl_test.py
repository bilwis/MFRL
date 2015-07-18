#!/usr/bin/python3

"""
This is the main module for MFRL and contains the main() function.
"""


import tdl
import colors as color

SCREEN_WIDTH = 80  #: The width of the main console
SCREEN_HEIGHT = 50  #: The height of the main console
LIMIT_FPS = 20  #: The maximum fps


def main():
    """ The main function starting MFRL

    :rtype: None
    """
    if __name__ == '__main__':
        root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT)
        tdl.set_fps(LIMIT_FPS)

        while not tdl.event.is_window_closed():
            root.set_colors(color.YELLOW, color.BLACK)
            root.draw_char(1, 1, '@')
            tdl.flush()
