from ttgtcanvas2 import get_robo_builder
import random
import math

def reverse_number(world):
    n = random.choice([12345, 97653, 23453,3533,6457,686323,64234,23534,88453,76543,234723,57423])
    world.add_msg(1,1, n)
    rev = 0
    while(n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    world.add_repoter_goal(rev)

def swap(world):
    cols = world.cols
    for x in range(cols - 2):
        world.add_object(x + 2,1, 'apple', 1)
        world.add_object(x + 2,2, 'banana', 1)
    world.add_home_goal(1,2)


def circle(world):
    cord = random.choice([7,9,11])
    world.set_dimensions(cord, cord)
    center = radius = ((cord - 1)//2)
    world.add_object(1,1,'star', 100)
    for x in range(cord):
        for y in range(cord):
            if math.dist([x,y], [center,center]) <= radius:
                world.add_drop_obj_goal(x+1,y+1, 'star', 1)

def choose_fruit():
    choice = random.randint(1,3)
    if choice == 1:
        return 'apple'
    elif choice == 2:
        return 'banana'
    else:
        return 'strawberry'

def diamond(world):
    dim = random.choice([7,9,11,13,15])
    world.set_dimensions(dim,dim)
    size = dim//2 + 1
    dimond_size = dim - 2
    stars = 0
    for y in range(0, size -1):
        for x in range(0,y +1):
            world.add_drop_obj_goal(size+x, y+2,  'star', 1)
            stars +=1
            
    for y in range(1, size -1):
        for x in range(1,y +1):
            world.add_drop_obj_goal(size-x, y+2,  'star', 1)
            stars +=1

    for y in range(size -2, 0 ,-1):
        for x in range(0,y):
            world.add_drop_obj_goal(size+x, dimond_size - y+2,  'star', 1)
            stars +=1

    for y in range(size -2, 0 ,-1):
        for x in range(1,y):
            world.add_drop_obj_goal(size-x, dimond_size - y+2,  'star', 1)
            stars +=1
    world.add_object(1,1,'star', stars)
            
    
def pick_fruits(world):
    dim = random.randint(9,15)
    world.set_dimensions(dim,dim)
    f = choose_fruit() 
    world.add_object(2,1, f, 1)
    for x in range(dim):
        for y in range(dim):
            world.add_tile(x + 1,y + 1, 'grass')
    #Fruit to pick
    for x in range(3, dim-2):
        world.add_wall(2, x,'west')
        world.add_wall(x, dim-2,'north')
        world.add_wall(dim -2, x,'east')

        for y in range(3,dim-2):
            fruit = choose_fruit()
            world.add_tile(x,y , 'pale_grass')
            world.add_object(x,y, fruit, 1)
            if f == fruit :
                world.add_pick_obj_goal(x,y, fruit, 1)
        world.add_wall(2, dim-2,'west')
        world.add_wall(2, dim-2,'north')
        world.add_wall(dim -2, dim-2,'east')
        world.add_wall(dim -2, dim-2,'north')

def upper_triangle(world):
    dim = random.choice([7,9,11,13,15])
    world.set_dimensions(dim//2+1,dim)
    size = dim//2 + 1
    dimond_size = dim - 2
    stars = 0

    for y in range(size -2, 0 ,-1):
        for x in range(0,y):
            world.add_drop_obj_goal(size+x, dimond_size - y+3 - size,  'star', 1)
            stars +=1

    for y in range(size -2, 0 ,-1):
        for x in range(1,y):
            world.add_drop_obj_goal(size-x, dimond_size - y+3 - size,  'star', 1)
            stars +=1
    world.add_object(1,1,'star', stars)
    
    
def lower_triangle(world):
    dim = random.choice([7,9,11,13,15])
    world.set_dimensions(dim//2+2,dim)
    size = dim//2 + 1
    dimond_size = dim - 2
    stars = 0
    for y in range(0, size -1):
        for x in range(0,y +1):
            world.add_drop_obj_goal(size+x, y+2,  'star', 1)
            stars +=1
            
    for y in range(1, size -1):
        for x in range(1,y +1):
            world.add_drop_obj_goal(size-x, y+2,  'star', 1)
            stars +=1
    world.add_object(1,1,'star', stars)

    
def swap_bot(bot):
    bot.max_capacity = 1


get_robo = get_robo_builder(levels={
    'reverse_number': reverse_number,
    'swap': swap,
    'circle': circle,
    'pick_fruits': pick_fruits,
    'diamond': diamond,
    'lower_triangle': lower_triangle,
    'upper_triangle': upper_triangle
}, robo_fn = {
   'swap': swap_bot
})