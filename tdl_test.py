import tdl
import colors as color

# actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20  # 20 frames-per-second maximum

root = tdl.init(SCREEN_WIDTH, SCREEN_HEIGHT)
tdl.set_fps(LIMIT_FPS)

while not tdl.event.is_window_closed():
    root.set_colors(color.YELLOW, color.BLACK)
    root.draw_char(1, 1, '@')
    tdl.flush()
