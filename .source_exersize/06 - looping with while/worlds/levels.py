from ottopy import get_robo_builder
import random

def reach_home(world):
    x = random.randint(3, 10)
    world.add_home_goal(x, 1)

def banana_fill(world):
    world.add_object(1,1,'banana', 15)
    
    x = random.randint(4, 10)
    world.add_object(x, 1, 'banana', 1)
    
    for i in range(2, x):
        world.add_drop_obj_goal(i,1,'banana',1)
    world.add_repoter_goal("Dropped {} bananas".format(x - 2))

def around_the_lake(world):
    r = random.randint(3,10)
    c = random.randint(3,10)
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
    world.add_pick_obj_goal(1,2,'carrot',1)
    
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


def hello_while(world):
    apples = random.randint(2,7)
    for i in range(apples):
        world.add_object(i+2, 1, 'apple',1)
    world.add_home_goal(apples + 2, 1)
    world.add_repoter_goal("Picked {} apples".format(apples))

def move_to_last(world):
    apples = random.randint(3,7)
    world.add_object(2, 1, 'banana', 1)
    for i in range(apples):
        world.add_object(i + 3, 1, 'apple',1)
    world.add_tile(apples + 3, 1, 'grass')
    world.add_drop_obj_goal(apples+3, 1, 'banana', 1)

get_robo = get_robo_builder(levels = {
    "reach_home": reach_home,
    "banana_fill": banana_fill,
    "hello_while": hello_while,
    "move_to_last": move_to_last,
    "rain": rain,
    "around_the_lake": around_the_lake
})