from ttgtcanvas2 import get_robo_builder
import random

def pick_star(world):
    world.add_pick_obj_goal(6,1, "star", 10)

def pick_flowers(world):
    world.add_pick_obj_goal(2,1, "daisy", 10)
    world.add_pick_obj_goal(4,1, "daisy", 10)
    world.add_pick_obj_goal(3,1, "daisy", 10)
    world.add_pick_obj_goal(5,1, "daisy", 10)
    

def pick_fruit_inc(world):
    world.add_pick_obj_goal(2,1, "apple", 1)
    world.add_pick_obj_goal(3,1, "orange", 2)
    world.add_pick_obj_goal(4,1, "banana", 3)
    world.add_pick_obj_goal(5,1, "strawberry", 4)

def pick_fruit_dec(world):
    world.add_pick_obj_goal(2,1, "apple", 4)
    world.add_pick_obj_goal(3,1, "orange", 3)
    world.add_pick_obj_goal(4,1, "banana", 2)
    world.add_pick_obj_goal(5,1, "strawberry", 1)

get_robo = get_robo_builder(levels={
        "pick_star": pick_star,
        "pick_flowers": pick_flowers,
        "pick_fruit_inc": pick_fruit_inc,
        "pick_fruit_dec": pick_fruit_dec
})