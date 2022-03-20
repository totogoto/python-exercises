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


get_robo = get_robo_builder(levels={
    'flowers': flowers
})