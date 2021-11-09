from ttgtcanvas2 import get_robo_builder
import random

fruits = ["strawberry", "banana", "orange", "apple", "carrot"]
flowers = ["leaf", "dandelion", "tulip", "daisy", "star"]


def selecting_fruits(world, x=["banana", "apple"], row = 1):
    count = 0
    for i in range(9):
        world.add_tile(i + 1, row, 'grass')
        if i == 0:
            continue
        choice = random.randint(0, 1)
        if choice == 1:
            selected = random.choice(x)
            world.add_object(i + 1, row, selected, 1)
            count+=1
        else:
            world.add_object(i + 1, row, random.choice(flowers), 1)
    world.add_repoter_goal(f"Picked {count} fruits.")

def pick_multiple(world):
    for i in range(10):
        world.add_tile(i + 1, 1, 'grass')
    x = random.sample(fruits,3)
    count = 0
    row = 2
    for i in range(9):
        world.add_tile(i + 2, row, 'grass')
        if i == 0:
            continue
        choice = random.randint(0, 1)
        if choice == 1:
            selected = random.choice(x)
            world.add_object(i + 1, row, selected, 1)
            count+=1
        else:
            world.add_object(i + 1, row, random.choice(flowers), 1)
            
    for i in range(3):
        world.add_object(i+4, 1, x[i], 1)
    world.add_repoter_goal(f"Picked {count} fruits.")

def not_star(world):
    count = 0
    for i in range(9):
        world.add_tile(i + 1, 1, 'grass')
        if i == 0:
            continue
        choice = random.randint(0, 1)
        if choice == 1:
            world.add_object(i + 1, 1, 'star', 1)
        else:
            world.add_object(i + 1, 1, random.choice(fruits), 1)
            count+=1
    world.add_repoter_goal(f"Picked {count} fruits.")
        

def not_in(world):
    for i in range(10):
        world.add_tile(i + 1, 1, 'grass')
    x = random.sample(flowers,3)
    count = 0
    row = 2
    for i in range(9):
        world.add_tile(i + 2, row, 'grass')
        if i == 0:
            continue
        choice = random.randint(0, 1)
        if choice == 1:
            selected = random.choice(x)
            world.add_object(i + 1, row, selected, 1)
            
        else:
            world.add_object(i + 1, row, random.choice(fruits), 1)
            count+=1
    for i in range(3):
        world.add_object(i+4, 1, x[i], 1)
    world.add_repoter_goal(f"Picked {count} fruits.")
    
def only_x(world):
    x = random.randint(1,4)
    for i in range(3*x + 1):
        world.add_object(i+2, 1, 'apple', 1)

def only_x_bot(bot):
    bot.max_capacity = 3

def simple_and(world):
    m = 0
    for i in range(2,14, 2):
        x = random.choice(['fire', 'fire', 'star'])
        world.add_object(i, 1, x, 1)
        choice = random.randint(1,3)
        if x == 'fire':
            if choice == 1:
                world.add_object(i+1, 1, 'leaf', 1)
                m +=1
            else:
                world.add_object(i+1, 1, 'token', 1)
        else:
            world.add_object(i+1, 1, 'leaf', 1)
    world.add_repoter_goal(f"Picked {m} leafs.")
    
get_robo = get_robo_builder(levels = {
    'selecting_fruits': selecting_fruits,
    'pick_multiple': pick_multiple,
    'not_star': not_star,
    'not_in': not_in,
    'only_x': only_x,
    'simple_and': simple_and
},
robo_fn = {
    'only_x': only_x_bot
})