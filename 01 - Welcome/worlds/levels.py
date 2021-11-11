from ottopy import get_robo_builder
import random

def explore(world):
    world.add_home_goal(7,5)
    world.add_object(5, 1, 'apple', 1)
    world.add_pick_obj_goal(5,1, 'apple', 1)
    
    world.add_object(5, 5, 'banana', 1)
    world.add_pick_obj_goal(5,5, 'banana', 1)
    
    world.add_object(2, 5, 'strawberry', 1)
    world.add_pick_obj_goal(2,5, 'strawberry', 1)
    
def warm_up(world):
    world.add_home_goal(2,5)
    world.add_object(5, 1, 'apple', 1)
    world.add_pick_obj_goal(5,1, 'apple', 1)
    
    world.add_object(5, 5, 'banana', 1)
    world.add_pick_obj_goal(5,5, 'banana', 1)
    

def lets_turn(world):
    world.add_home_goal(8,3)
    world.add_object(7, 1, 'apple', 1)
    world.add_pick_obj_goal(7,1, 'apple', 1)

def i_can_pick(world):
    world.add_home_goal(10,1)
    world.add_object(6, 1, 'apple', 1)
    world.add_pick_obj_goal(6,1, 'apple', 1)

def say_hello(world):
    world.add_home_goal(10,1)


get_robo = get_robo_builder(levels={
    "explore": explore,
    "warm_up": warm_up,
    "lets_turn": lets_turn,
    "i_can_pick": i_can_pick,
    "say_hello": say_hello
})