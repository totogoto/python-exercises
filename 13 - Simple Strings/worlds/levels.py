from ottopy import get_robo_builder
import random

def read_message(world):
    x = random.randint(2,10)
    l =["love", "like", "code", "dream"]
    y = random.choice(l)
    msg = f"I {y} python"
    world.add_msg(x, 1, msg)
    world.add_repoter_goal(msg)

def stats(world):
    x = random.randint(2,10)
    l = ["apple", "banana", "tulip", "carrot"]
    y = random.choice(l)
    world.add_object(x, 1, y, 1)
    world.add_repoter_goal(f"Length of the {y.capitalize()} is {len(y)}.")

def replace(world):
    x = random.randint(2,5)
    x2 = random.randint(6,10)
    l = ["banana", "tulip", "carrot"]
    mss = ["I love apple.", "I found apple.", "I like apple." ]
    y = random.choice(l)

    ms = random.choice(mss)
    world.add_msg(x2,1, ms)
    world.add_object(x, 1, y, 1)
    world.add_repoter_goal(ms.replace("apple", y))
    

def reverse(world):
    l =["love", "like", "code", "dream"]
    y = random.choice(l)
    ms = f"I {y} python"
    x = random.randint(2,10)
    world.add_msg(x, 1, ms[::-1])
    world.add_repoter_goal(ms)

def slice_2(world):
    l =["lmorvwe", "lriekce", "ccosdwe"]
    y = random.choice(l)
    ms = f"I {y} python"
    me = ms[2:9]
    
    x = random.randint(2,10)
    world.add_msg(x, 1, ms)
    world.add_repoter_goal(ms.replace(me, me[0::2]))
    
def slice_1(world):
    l =["love", "like", "hate"]
    y = random.choice(l)
    m = random.choice(["apple", "banana", "tulip", "carrot", "python"])
    ms = f"I {y} {m}"
    x = random.randint(2,10)
    world.add_msg(x, 1, ms)
    world.add_repoter_goal(f"{ms[2:6]}, {ms[7:]}")
    
    
    

def is_palindrom(s):
    return s == s[::-1]

def palindrome(world):
    mss = ["wow", "apple", "radar", "level", "banana", "tulip" ]
    ms = random.choice(mss)
    x = random.randint(2,10)
    world.add_msg(x, 1, ms[::-1])
    world.add_repoter_goal("Palindrome" if is_palindrom(ms) else "Not Palindrome")

def find(world):
    l = ["apple", "banana", "tulip", "carrot"]
    l1 = []
    for x in l:
        i = random.randint(1,3)
        for m in range(i):
            l1.append(x)
    random.shuffle(l1)
    l2 = ",".join(l1)
    choice = random.choice(l)
    index = l2.count(choice)
    pos = random.randint(3,10)
    world.add_msg(pos,1, l2)
    world.add_object(pos-1,1, choice,1)
    world.add_repoter_goal(f"Count of {choice} is: {index}")

def ascii_sum(world):
    l = ["apple", "banana", "tulip", "carrot"]
    choice = random.choice(l)
    pos = random.randint(3,10)
    world.add_object(pos,1, choice,1)
    cost = sum(map(ord, choice))
    world.add_repoter_goal(f"Total Cost: {cost}")

def cipher(world):
    message = ["apple", "banana", "tulip", "carrot"]
    choice = random.choice(message)
    pos = random.randint(3,10)
    key = random.choice(message)
    e_msg = "".join([chr(ord(x) + len(key)) for x in choice])
    world.add_msg(pos ,1, e_msg)
    world.add_object(pos -1 ,1, key,1)
    world.add_repoter_goal(choice)
    

def instructions(world):
    l = [
        ["M2T1", "M5T3", "M1T0"],
        ["M3T1", "M4T3", "M3T0"],
        ["M3T1", "M2T3", "M2T0"],
        ["M4T1", "M3T3", "M4T0"]
    ]
    
    choice = random.choice(l)
    d = {"x": 2, "y": 1}
    current = 'x'
    for x in choice:
        m,p,t,q =x
        world.add_msg(d["x"], d["y"], x)
        d[current] += int(p)
        if t == "T" and q == "1":
            current = "y"
        if t == "T" and q == "3":
            current = "x"

    world.add_home_goal(d["x"], d["y"])
        

get_robo = get_robo_builder(levels = {
    "read_message": read_message,
    "stats": stats,
    "replace": replace,
    "reverse": reverse,
    "palindrome":palindrome,
    "find": find,
    "ascii_sum": ascii_sum,
    "cipher": cipher,
    "instructions": instructions,
    "slice": slice_2,
    "middle": slice_1
    
})

