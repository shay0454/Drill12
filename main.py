from pico2d import open_canvas, delay, close_canvas
import game_framework
import os
os.chdir(os.path.dirname(__file__))
import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
close_canvas()

