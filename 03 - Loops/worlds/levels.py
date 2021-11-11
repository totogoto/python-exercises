import random
from ottopy import get_robo_builder

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

def move_i(world):
    star_pos = [3,6,10,15]
    for x in range(2,16):
        if x in star_pos:
            world.add_object(x, 1, 'star', 1)
            world.add_pick_obj_goal(x, 1, 'star', 1)
        else:
            world.add_flag(x, 1)
    world.add_flag_count_goal(10)
            
def move_spiral(world):
    for i in range(5):
        world.add_flag(i +2,1)
    world.add_object(7, 1, 'star', 1)
    world.add_pick_obj_goal(7, 1, 'star', 1)

    for i in range(4):
        world.add_flag(7,i+2)
    world.add_object(7, 6, 'star', 1)
    world.add_pick_obj_goal(7, 6, 'star', 1)
    
    for i in range(3):
        world.add_flag(i +4,6)
    world.add_object(3, 6, 'star', 1)
    world.add_pick_obj_goal(3, 6, 'star', 1)
    for i in range(2):
        world.add_flag(3,i+4)
    world.add_object(3, 3, 'star', 1)
    world.add_pick_obj_goal(3, 3, 'star', 1)
    world.add_object(5, 3, 'star', 1)
    world.add_pick_obj_goal(5, 3, 'star', 1)
    world.add_flag(4,3)
    world.add_flag_count_goal(15)

def triangle_5(world):
    for x in range(1,6):
        for i in range(x):
            world.add_flag(i+1,x+1)
        world.add_object(x+1, x+1, 'star', 1 )
        world.add_pick_obj_goal(x+1, x+1, 'star', 1 )
    world.add_flag_count_goal(15)

def triangle_odd(world):
    for x in range(1,11,2):
        world.add_object(x+2, x+2, 'star', 1 )
        world.add_pick_obj_goal(x+2, x+2, 'star', 1 )
        
def take_5_and_put_5(world):
    for x in range(5):
        world.add_object(x+2, 1, 'star',1)
    world.add_drop_obj_goal(7, 1, 'star',5)    

def take_loop(world):
    for x in range(5):
        world.add_object(x+2, 1, 'star',x+1)
    world.add_drop_obj_goal(7, 1, 'star',15) 
    

def take_odd(world):
    for x in range(5, 11):
        world.add_object(x-3, 1, 'star',x)
    world.add_drop_obj_goal(8, 1, 'star',45) 

get_robo = get_robo_builder(levels={
    'around_the_room': around_the_room,
    'jump_loop': jump_loop,
    'move_i': move_i,
    'move_spiral': move_spiral,
    'triangle_5': triangle_5,
    'triangle_odd': triangle_odd,
    'take_5_and_put_5': take_5_and_put_5,
    'take_loop': take_loop,
    'take_odd': take_odd
})