from ottopy import get_robo_builder
import random

def jump(world):
    world.add_flag_count_goal(2)

def corners(world):
    world.add_flag_count_goal(3)

def hoops(world):
    for x in range(4,8):
        world.add_wall(3, x, "west")
        world.add_wall(8, x, "east")
        world.add_wall(x, 8, "north")
        world.add_wall(x, 3, "south")
    world.add_flag_count_goal(7)

def beepers_on_rise(world):
    for x in range(1, 10):
        for y in range(2,12):
            world.add_wall(x,y,"east")

def flags_at_random(world):
    for x in range(1, 10):
        for y in range(2,10):
            world.add_wall(x,y,"east")

def beepers_at_random(world):
    for x in range(1, 10):
        for y in range(2,10):
            world.add_wall(x,y,"east")

def random_pick(world):
    l = [3,2,4,1,5]
    items = ["apple", "banana", "daisy", "carrot", "strawberry"]
    for i in range(len(l)):
        world.add_object(i+2, 1, items[i], l[i])
        world.add_pick_obj_goal(i+2, 1, items[i], l[i])
        
def random_location(world):
    for x in range(1, 10):
        for y in range(2,10):
            world.add_wall(x,y,"east")

def snake(world):
    for x in range(1, 10):
        for y in range(2,10):
            world.add_wall(x,y,"east")
    for x in range(1, 8, 2):
        world.add_wall(x,1,"east")
        world.add_wall(x+1,10,"east")

def double_list(world):
    pass

def spiral(world):
    for s in range(4):
        for x in range(s,9-s):
            world.add_wall(x+1, s+1, "north")
        for x in range(s+1,9-s):
            world.add_wall(9-s, x+1, "east")
        for x in range(s+1,9-s):
            world.add_wall(x+1, 9-s, "north")
        for x in range(s+2,9-s):
            world.add_wall(s+1, x+1, "east")
        world.add_wall(5,5, "north")
    
get_robo = get_robo_builder(levels={
    'jump': jump,
    'corners': corners,
    "hoops": hoops,
    "beepers_on_rise": beepers_on_rise,
    "flags_at_random": flags_at_random,
    "beepers_at_random": beepers_at_random,
    "spiral": spiral,
    "random_pick": random_pick,
    "random_location": random_location,
    "snake": snake
    
},
                            
robo_fn={
})