import random

from pico2d import *
import game_framework

import game_world
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global grass
    global boy
    global balls
    running = True

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    # fill here
    balls=[Ball(random.randint(0,1600),60,0.0) for i in range(30)]
    game_world.add_objects(balls,1)
    # 충돌 상황을 등록
    game_world.add_collision_pair('boy:ball',boy,None)
    game_world.add_collision_pair('boy:zombie',boy,None)

    for ball in balls:
        game_world.add_collision_pair('boy:ball',None,ball)

    zombies=[Zombie() for _ in range(5)]
    game_world.add_objects(zombies,1)
    
    for zombie in zombies:
        game_world.add_collision_pair('boy:zombie',None,zombie)
        game_world.add_collision_pair('ball:zombie',None,zombie)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collsions()
    # fill here
    '''for ball in balls.copy():
        if game_world.collide(boy,ball):
            print('COLLISION boy : ball')
            # 충돌 처리
            # 볼은 없앤다.
            balls.remove(ball)
            game_world.remove_object(ball)
            # 소년은 볼 카운트 증가
            boy.ball_count+=1'''

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

