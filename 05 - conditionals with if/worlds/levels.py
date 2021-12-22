from ottopy import get_robo_builder
import random

# def piece_of_cake(world):
#     nb_carrot = 0
#     nb_daisy = 0
#     h = 6
#     w = 6

#     for x in range(2, w + 1):
#         choice = random.randint(1,3)
#         if choice == 1:
#             world.add_object(x, 1, "carrot", 1)
#             nb_carrot += 1
#         elif choice == 2:
#             world.add_object(x, 1,"daisy", 1)
#             nb_daisy += 1
    
#     for y in range(2, h + 1):
#         choice = random.randint(1,3)
#         if choice == 1:
#             world.add_object(w, y, "carrot", 1)
#             nb_carrot += 1
#         elif choice == 2:
#             world.add_object(w, y,"daisy", 1)
#             nb_daisy += 1

#     for x in range(w - 1, 1, -1):
#         choice = random.randint(1,3)
#         if choice == 1:
#             world.add_object(x, h, "carrot", 1)
#             nb_carrot += 1
#         elif choice == 2:
#             world.add_object(x, h,"daisy", 1)
#             nb_daisy += 1
    
#     for y in range(h - 1, 2, -1):
#         choice = random.randint(1,3)
#         if choice == 1:
#             world.add_object(1, y, "carrot", 1)
#             nb_carrot += 1
#         elif choice == 2:
#             world.add_object(1, y, "daisy", 1)
#             nb_daisy += 1
    
#     world.add_repoter_goal("I counted {} carrots".format(nb_carrot))

# def rain(world):
#     flip = random.randint(0,1)
#     left=4; right=10; bottom=3; top=7
    
#     tx1 = random.randint(left  + 1 ,right - 1)
#     tx2 = random.randint(left + 1,right -1)
#     ry1 = random.randint(bottom + 1,top - 1)
    
#     world.remove_wall(tx1, top, "north")
#     world.add_goal_wall(tx1, top, "north")
    
#     world.remove_wall(tx2, bottom, "south")
#     world.add_goal_wall(tx2, bottom, "south")
    
#     world.remove_wall(right, ry1, "east")
#     world.add_goal_wall(right, ry1, "east")

# def apple_and_carrots(world):
#     nb_carrot = 0
#     nb_apple = 0
#     h = 12
#     w = 12
#     for x in range(2, w + 1):
#         choice = random.randint(1,3)
#         if choice == 1:
#             world.add_object(x, 1, "carrot", 1)
#             nb_carrot += 1
#         elif choice == 2:
#             world.add_object(x, 1,"apple", 1)
#             nb_apple += 1
    
#     for y in range(2, h + 1):
#         choice = random.randint(1,3)
#         if choice == 1:
#             world.add_object(w, y, "carrot", 1)
#             nb_carrot += 1
#         elif choice == 2:
#             world.add_object(w, y,"apple", 1)
#             nb_apple += 1

#     for x in range(w - 1, 1, -1):
#         choice = random.randint(1,3)
#         if choice == 1:
#             world.add_object(x, h, "carrot", 1)
#             nb_carrot += 1
#         elif choice == 2:
#             world.add_object(x, h,"apple", 1)
#             nb_apple += 1
    
# def around_the_lake(world):
#     r = random.randint(3,10)
#     c = random.randint(3,10)
#     world.set_dimensions(r,c)
    
#     for x in range(2,c):
#         for y in range(2, r):
#             world.add_tile(x, y, 'water')
    
#     for x in range(1,c + 1):
#         world.add_tile(x, 1, 'grass')
#         world.add_tile(x, r, 'grass')

#     for y in range(1,r + 1):
#         world.add_tile(1, y, 'grass')
#         world.add_tile(c, y, 'grass')
    
#     for y in range(2,r):
#         world.add_wall(1, y, "east")
#         world.add_wall(c - 1, y, "east")

#     for x in range(2,c):
#         world.add_wall(x, 1, "north")
#         world.add_wall(x, r -1, "north")
     
#     world.add_wall(1, 1, "north")
#     world.add_object(1,2,"carrot", 1)



def count_carrots(world):
    nb_carrot = 0
    nb_carrot = 0
    nb_apple = 0
    h = 12
    w = 12
    for x in range(3, 9):
        choice = random.randint(1,2)
        if choice == 1:
            world.add_object(x, 1, "carrot", 1)
            nb_carrot += 1
    if(nb_carrot == 0):
        world.add_object(random.randint(3,9), 1, "carrot", 1)
        nb_carrot += 1
    
    world.add_repoter_goal("I counted {} carrots".format(nb_carrot))



    for y in range(h - 1, 2, -1):
        choice = random.randint(1,3)
        if choice == 1:
            world.add_object(1, y, "carrot", 1)
            nb_carrot += 1
        elif choice == 2:
            world.add_object(1, y, "apple", 1)
            nb_apple += 1
    
    world.add_repoter_goal("I counted {} carrots and {} apples".format(nb_carrot, nb_apple))

def wall_street(world):
    choice = random.randint(4,9)
    top = choice + 1
    world.add_wall(2,1, "west")
    for i in range(2, choice):
        world.add_wall(i,1, "north")
    world.add_wall(choice - 1, 1, "east")
    world.add_wall(top, 2, "west")
    for y in range(top, 11):
        world.add_wall(y,2, "south")

def choose_fruit():
    choice = random.randint(1,3)
    if choice == 1:
        return 'apple'
    elif choice == 2:
        return 'banana'
    else:
        return 'strawberry'

def pick_fruits(world):
    cfruit = 0
    #Fruit to pick
    fruit = choose_fruit()
    world.add_object(3,1, fruit, 1)
    for x in range(3, 9):
        for y in range(3,9):
            f = choose_fruit()
            world.add_object(x,y, f, 1)
            if f == fruit:
                cfruit +=1

    world.add_repoter_goal("I counted {} {}".format(cfruit, fruit))


def multiple(world):
    nb_carrot = 0
    nb_tomato = 0
    for x in range(3, 9):
        choice = random.randint(1,3)
        if choice == 1:
            world.add_object(x, 1, "carrot", 1)
            nb_carrot += 1
        elif choice == 2:
            world.add_object(x, 1, "apple", 1)
            nb_tomato += 1
            
    if(nb_carrot == 0):
        world.add_object(random.randint(3,9), 1, "carrot", 1)
        nb_carrot += 1

    world.add_repoter_goal("I counted {} carrots, {} apples".format(nb_carrot,nb_tomato ))



def flags(world):
    for x in range(1,10):
        if random.randrange(2):
            world.add_object( x+1, 1,'beeper', 1)
            world.add_pick_obj_goal( x+1, 1, 'beeper',1)
        else:
            world.add_flag(x+1, 1)


def flowers(world):
    world.add_object(2, 1,'strawberry', 10)
    for x in range(3,9, 2):
        if random.randrange(2):
            world.add_object( x+1, 1,'daisy', 1)
            world.add_drop_obj_goal( x+2, 1, 'strawberry',1)
            
    

def multi_flowers(world):
    world.add_object(2, 1,'strawberry', 20)
    count = 0
    for x in range(3,12,3):
        if random.randrange(2):
            count+=1
            world.add_object( x+1, 1,'daisy', 1)
            world.add_drop_obj_goal( x+2, 1, 'strawberry',1)
            world.add_drop_obj_goal( x+3, 1, 'strawberry',1)
    if count == 0:
            x = random.choice([3,6,9])
            world.add_object( x+1, 1,'daisy', 1)
            world.add_drop_obj_goal( x+2, 1, 'strawberry',1)
            world.add_drop_obj_goal( x+3, 1, 'strawberry',1)

            

get_robo = get_robo_builder(levels={
    "count_carrots": count_carrots,
    "wall_street": wall_street,
    "pick_fruits": pick_fruits,
    "multiple": multiple,
    "flags": flags,
    "flowers": flowers,
    "multi_flowers": multi_flowers   
})


