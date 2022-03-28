from ottopy import get_robo_builder
import random
import math

def flowers(world):
    m = random.choice([6,8])
    items = random.sample([[3,1], [1,2], [3,3], [4,3] , [5,2], [7,1], [6,6]], random.randint(3, 6))

    n = m // 2
    world.set_dimensions(m+1, m+1)
    for s in range(n):
        for x in range(s,m-s):
            world.add_wall(x+1, s+1, "north")
        for x in range(s+1,m-s):
            world.add_wall(m-s, x+1, "east")
        for x in range(s+1,m-s):
            world.add_wall(x+1, m-s, "north")
        for x in range(s+2,m-s):
            world.add_wall(s+1, x+1, "east")
        world.add_wall(n+1,n+1, "north")
    world.add_home_goal(n+1, n+1)

    for y in items:
        world.add_object(y[0], y[1],'daisy' ,1)
        world.add_pick_obj_goal(y[0], y[1],'daisy' ,1)


def only(world):
    m = random.choice([6,8])

    n = m // 2
    world.set_dimensions(m+1, m+1)
    for s in range(n):
        for x in range(s,m-s):
            world.add_wall(x+1, s+1, "north")
        for x in range(s+1,m-s):
            world.add_wall(m-s, x+1, "east")
        for x in range(s+1,m-s):
            world.add_wall(x+1, m-s, "north")
        for x in range(s+2,m-s):
            world.add_wall(s+1, x+1, "east")
        world.add_wall(n+1,n+1, "north")
    world.add_home_goal(n+1, n+1)

    for a in range(2, m+1): 
        for b in range(2,m+1):
            if a == n+1 and b == n+1: 
                continue
            else:
                flip = random.randint(0,1)
                flip2 = random.randint(0,1)
                if  flip and flip2:
                    world.add_object(a, b,'apple' ,1)
                    world.add_pick_obj_goal(a, b,'apple' ,1)
                if flip and not flip2:
                     world.add_object(a, b,'daisy' ,1)


def c_path(world):
    world.add_wall(9,9,'east')
    world.add_wall(9,2,'east')
    world.add_home_goal(9,9)
    for x in range(2,10):
        world.add_wall(1, x, 'east')
        world.add_wall(x, 2, 'south')
        world.add_wall(x, 9, 'north')
        if x > 2:
            if x < 9:
                world.add_wall(2, x, 'east')
            world.add_wall(x, 3, 'south')
            world.add_wall(x, 8, 'north')


def s_path(world):
    world.add_home_goal(2,9)
    for x in range(2,6):
        world.add_wall(1, x, 'east')
    for x in range(2,10):
        world.add_wall(x,1, 'north')
        world.add_wall(x, 9,'north')
        if x != 2:
            world.add_wall(x,2, 'north')
            world.add_wall(x,4, 'north')
        if x != 9:
            world.add_wall(x,5, 'north')
            world.add_wall(x,8, 'north')
    world.add_wall(9, 2, 'east')
    world.add_wall(2, 3, 'east')
    world.add_wall(2, 4, 'east')
    world.add_wall(2, 9, 'west')
    for x in range(5,10):
        world.add_wall(9, x, 'east')
        if x > 5 and x < 9:
            world.add_wall(8, x, 'east')
            




def paths(world):
    path = random.choice([c_path, s_path])
    path(world)



get_robo = get_robo_builder(levels={
    'flowers': flowers,
    'only': only,
    'paths':paths
})