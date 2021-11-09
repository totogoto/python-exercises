from ttgtcanvas2 import get_robo_builder
import random

fruits = ["strawberry", "banana", "orange", "apple", "carrot"]
flowers = ["leaf", "dandelion", "tulip", "daisy", "star"]

def storm(world):
    row = random.randint(5, 8)
    col = random.randint(5, 8)
    world.set_dimensions(row,col)
    
    cell_x = random.randint(3,col -2)
    cell_y = random.randint(3, row -2)
    
    world.add_wall(cell_x, cell_y, 'north')
    world.add_wall(cell_x, cell_y, 'south')
    world.add_wall(cell_x, cell_y, 'east')
    world.add_wall(cell_x, cell_y, 'west')
    
    for x in range(row):
        for y in range(col):
            if y + 1== cell_x and x + 1 == cell_y:
                world.add_tile(y +1 ,x +1, 'water')
            else:
                world.add_tile(y +1 , x+1,  'grass')
                if random.randint(0,2) == 1:
                    val = random.randint(1,4)
                    world.add_object(y + 1,x + 1, 'leaf', val)
                    world.add_pick_obj_goal(y + 1,x + 1, 'leaf', val)
                    
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
    world.add_repoter_goal(f"Picked {count} fruits")

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
    world.add_repoter_goal(f"Picked {count} fruits")

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
    world.add_repoter_goal(f"Picked {count} fruits")
        

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
    world.add_repoter_goal(f"Picked {count} fruits")
    
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
    world.add_repoter_goal(f"Picked {m} leaves")

def leaves_after(world):
    c = 0
    items=[]
    for _ in range(random.randint(3,5)):
        items.extend(random.choice([['fire','leaf'], ['fire', 'star'],['star','leaf'],['leaf','leaf']]))
    items.extend(['star','leaf',''])

    
    for i in range(len(items)):
        if items[i]:
            world.add_object(2+i, 1, items[i], 1)
            if items[i]=='leaf' and i>0 and items[i-1]=='fire' :
                c=c+1
                world.add_pick_obj_goal(2+i, 1,'leaf',1)
                
    world.add_repoter_goal(f"Picked {c} leaves")

    
def leaves_around(world):
    c = 0
    items=[]
    for _ in range(random.randint(3,5)):
        items.extend(random.choice([['fire','leaf'], ['fire', 'star'],['star','leaf'],['leaf','leaf']]))
    items.extend(['star','leaf',''])

    
    for i in range(len(items)):
        if items[i]:
            world.add_object(2+i, 1, items[i], 1)
            if items[i]=='leaf' and ( (i>0 and items[i-1]=='fire') or items[i+1]=='fire'):
                c=c+1
                world.add_pick_obj_goal(2+i, 1,'leaf',1)
                
    world.add_repoter_goal(f"Picked {c} leaves")
  
get_robo = get_robo_builder(levels = {
    'selecting_fruits': selecting_fruits,
    'pick_multiple': pick_multiple,
    'not_star': not_star,
    'not_in': not_in,
    'only_x': only_x,
    'storm': storm,
    'simple_and': leaves_after,
    'leaves_around': leaves_around
},
robo_fn = {
    'only_x': only_x_bot
})