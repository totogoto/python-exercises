from ttgtcanvas2 import get_robo_builder
import random


def around_the_lake(world):
    if random.randint(0,1):
        r,c = 10,7
    else:
        r,c = 7,10
        
    world.set_dimensions(r,c)
    
    for x in range(2,c):
        for y in range(2, r):
            world.add_tile(x, y, 'water')
    
    for x in range(1,c + 1):
        world.add_tile(x, 1, 'grass')
        world.add_tile(x, r, 'grass')

    for y in range(1,r + 1):
        world.add_tile(1, y, 'grass')
        world.add_tile(c, y, 'grass')
    
    for y in range(2,r):
        world.add_wall(1, y, "east")
        world.add_wall(c - 1, y, "east")

    for x in range(2,c):
        world.add_wall(x, 1, "north")
        world.add_wall(x, r -1, "north")
     
    world.add_wall(1, 1, "north")
    world.add_object(1,2,"carrot", 1)
    


def rain(world):
    flip = random.randint(0,1)
    left=4; right=10; bottom=3; top=7
    
    tx1 = random.randint(left  + 1 ,right - 1)
    tx2 = random.randint(left + 1,right -1)
    ry1 = random.randint(bottom + 1,top - 1)
    
    world.remove_wall(tx1, top, "north")
    world.add_goal_wall(tx1, top, "north")
    
    world.remove_wall(tx2, bottom, "south")
    world.add_goal_wall(tx2, bottom, "south")
    
    world.remove_wall(right, ry1, "east")
    world.add_goal_wall(right, ry1, "east")


def pair(world):
    table = [
     ["apple", "banana", "orange"],
     ["apple", "leaf", "tulip"],
     ["star", "seed", "tulip"],
     ["star", "daisy", "orange"],
     ["leaf", "daisy", "dandelion"]
    ]
    x = random.choice(table)
    world.add_object(2,1, "orange",1)
    world.add_object(3,1, "tulip", 1)
    world.add_object(4,1, "dandelion",1)
    world.add_object(1,2, x[0],1)
    world.add_object(2,2, x[1],1)
    world.add_drop_obj_goal(3,2, x[2],1)


def pair_multi(world):
    table = [
     ["apple", "banana", "orange"],
     ["apple", "leaf", "tulip"],
     ["star", "seed", "tulip"],
     ["star", "daisy", "orange"],
     ["leaf", "daisy", "dandelion"]
    ]
    world.add_object(2,1, "orange",20)
    world.add_object(3,1, "tulip", 20)
    world.add_object(4,1, "dandelion",20)
    random.shuffle(table)
    for m in range(3):
        world.add_object(1,m+2, table[m][0],1)
        world.add_object(2,m+2, table[m][1],1)
        world.add_drop_obj_goal(3,m+2, table[m][2],1)
    
    
get_robo = get_robo_builder(levels = {
    "rain": rain,
    "around_the_lake": around_the_lake,
    "pair": pair,
    "pair_multi": pair_multi
})