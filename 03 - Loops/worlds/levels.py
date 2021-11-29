import random
from ottopy import get_robo_builder

def hello(world):
    for x in range(8):
        world.add_flag(2+x,1)
    world.add_flag_count_goal(8)
    world.add_home_goal(10, 1)

def hello_pick(world):
    for x in range(8):
        world.add_flag(2+x,1)
    world.add_flag_count_goal(8)
    world.add_object(10, 1, 'apple', 1)
    world.add_pick_obj_goal(10, 1, 'apple', 1)


def around_the_room(world):
    for x in range(7):
        world.add_flag(2+x,1)
        world.add_flag(8,2+x)
        world.add_flag(1+x, 8)
        world.add_flag(1,1+x)
    world.add_flag_count_goal(28)

def jump_loop(world):
    for x in range(10):
        world.add_wall(x+1,1,'east')
        if x == 9:
            break  
        world.add_object(x+2, 1, 'star', 1 )
        world.add_pick_obj_goal(x+2, 1, 'star', 1 )

        
def take_5_and_put_5(world):
    for x in range(5):
        world.add_object(x+2, 1, 'star',1)
    world.add_drop_obj_goal(7, 1, 'star',5)

def pick_star(world):
    world.add_pick_obj_goal(6,1, "star", 10)

def pick_flowers(world):
    world.add_pick_obj_goal(2,1, "daisy", 10)
    world.add_pick_obj_goal(4,1, "daisy", 10)
    world.add_pick_obj_goal(3,1, "daisy", 10)
    world.add_pick_obj_goal(5,1, "daisy", 10)

get_robo = get_robo_builder(levels={
    'around_the_room': around_the_room,
    'jump_loop': jump_loop,
    'pick_star': pick_star,
    'pick_flowers': pick_flowers,
    'take_5_and_put_5': take_5_and_put_5,
    'hello':hello,
    'hello_pick': hello_pick
})