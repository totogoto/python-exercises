import random
from ottopy import get_robo_builder

def smart_bot(world):
    world.add_object(10,1,'apple',1)
    world.add_pick_obj_goal(10,1,'apple',1)

def take_and_count(world):
    total  = 0
    for x in range(2,9):
        choice = random.randint(1,4)
        total = total + choice
        world.add_object(x, 1, 'apple', choice)
        world.add_pick_obj_goal(x,1,'apple', choice)
    world.add_repoter_goal(f"Picked {total} fruits.")

def advance_bot(world):
    total  = 0
    apple = 0
    orange  = 0
    for x in range(2,11):
        choice = random.randint(1,4)
        is_apple = random.randint(0,1)
        total = total + choice
        if is_apple == 1:
            apple = apple + choice
            world.add_object(x, 1, 'apple', choice)
            world.add_pick_obj_goal(x,1,'apple', choice)
        else:
            orange = orange + choice
            world.add_object(x, 1, 'orange', choice)
            world.add_pick_obj_goal(x,1,'orange', choice)

    world.add_repoter_goal(f"Picked {apple} apple.")
    world.add_repoter_goal(f"Picked {orange} orange.")


get_robo = get_robo_builder(levels={
    'smart_bot': smart_bot,
    'take_and_count': take_and_count,
    'advance_bot': advance_bot
})