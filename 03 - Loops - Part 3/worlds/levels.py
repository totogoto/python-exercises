from ottopy import get_robo_builder
import random

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

    world.add_pick_obj_goal(1,2, 'beeper', 1)
    world.add_pick_obj_goal(2,3, 'beeper', 1)
    world.add_pick_obj_goal(3,4, 'beeper', 1)
    world.add_pick_obj_goal(4,5, 'beeper', 1)
    world.add_pick_obj_goal(5,6, 'beeper', 1)
    world.add_pick_obj_goal(6,7, 'beeper', 1)
    world.add_pick_obj_goal(7,8, 'beeper', 1)
    world.add_pick_obj_goal(8,9, 'beeper', 1)
    world.add_pick_obj_goal(9,10, 'beeper', 1)
    world.add_pick_obj_goal(10, 11, 'beeper', 1)

def flags_at_random(world):
    for x in range(1, 10):
        for y in range(2,10):
            world.add_wall(x,y,"east")

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
    world.add_flag_count_goal(18)
    
get_robo = get_robo_builder(levels={
    'corners': corners,
    "hoops": hoops,
    "beepers_on_rise": beepers_on_rise,
    "flags_at_random": flags_at_random,
    "spiral": spiral
},
                            
robo_fn={
})