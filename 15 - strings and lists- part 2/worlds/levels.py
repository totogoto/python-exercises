from ottopy import get_robo_builder
import random

def count_words(world):
    items = ["apple", "strawberry", "carrot",  "daisy", "banana"]
    y = random.randint(1,4)
    rand_items = random.sample(items, y)
    msg = ','.join(rand_items)
    world.add_msg(1, 1, msg)
    random.shuffle(items)
    
    for x in range(len(items)):
        if items[x] in rand_items:
            world.add_object(x+2,1, items[x], 1)
            world.add_pick_obj_goal(x+2, 1, items[x], 1)
        else:
            world.add_object(x+2,1, items[x], 1)

def join_words(world):
    items = ["apple", "strawberry", "carrot",  "daisy", "banana"]
    x = random.sample(items, random.randint(3, len(items)))
    for i in range(len(x)):
        world.add_object(i+2,1, x[i],1)
    world.add_repoter_goal(f"Found {','.join(x[0:-1])} and {x[-1]}.")

def complete_the_sentence(world):
    msg1 = random.choice(["I", "Otto", "We"])
    msg2 = random.choice(["loves", "enjoys", "like", "codes"])
    msg3 = "Python."
    world.add_msg(2, 1, msg1)
    world.add_msg(3, 1, msg2)
    world.add_msg(4, 1, msg3)
    world.add_repoter_goal(f"{msg1} {msg2} {msg3}")

def complete_the_sentence_2(world):
    msg = random.choice(["Otto loves to garden", "Otto loves python", "we love to code", "coding in python is fun"])
    words = msg.split(" ")
    for i in range(len(words)):
        world.add_msg(i+2,1,words[i])
    world.add_repoter_goal(msg)

    
def even_word(world):
    msg1 = random.choice(["Otto", "We", "Bot", "Robot"])
    msg2 = random.choice(["loves", "enjoys", "likes", "codes", "writes"])
    msg3 = "Python"
    gb = ["blah", "foo", "aa", "vehicula", "dolor", "ipsum"]
    random.shuffle(gb)
    msg = f"{gb[0]}  {msg1}  {gb[1]}  {msg2}  {gb[2]}  {msg3}  {gb[3]}"
    li = msg.split()
    world.add_msg(1, 1, msg)
    world.add_repoter_goal(' '.join(li[1::2]))
        
    

def nutrients(world):
    pass

def count_a(world):
    val = random.randint(3,9)
    l = ["a", "b", "c"]
    random.shuffle(l)
    msg = l[0]*val+l[1]*random.randint(3,9)+l[2]*random.randint(3,9)
    world.add_msg(1, 1, msg)
    world.add_repoter_goal(f"{l[0]}{val}")

def run_length(world):
    q= ["a","b","d","m"]
    q2= [ "a", "b", "d"]
    random.shuffle(q2)
    q = q + q2
    a = ""
    op = ""
    for x in range(6):
        val = random.randint(3,9)
        a += q[x]*val
        op +=f"{q[x]}{val}"
    world.add_msg(1, 1, a)
    world.add_repoter_goal(f"{op}")
    
def decode(world):
    q=["a","b","d","m"]
    random.shuffle(q)
    r = [random.randint(3,9) for x in range(4)]
    a = [f"{q[x]}{r[x]}" for x in range(4)]
    world.add_msg(1, 1, ''.join(a))
    world.add_repoter_goal(''.join([f"{q[x]*r[x]}" for x in range(4)]))
    

def str2dict(world):
    num_dict = {"one": "1", "two":"2", "three":"3", "four":"4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10"}
    world.add_repoter_goal(num_dict)

def str2num(world):
    num_dict = {"one": 1, "two":2, "three":3, "four":4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
    k = num_dict.keys()
    x = random.sample(k,random.randint(3,6))
    world.add_msg(1, 1, ' + '.join(x))
    world.add_repoter_goal(f"Total: {sum([num_dict[t] for t in x])}")
    
def operations(world):
    pass

get_robo=get_robo_builder(levels = {
        'count_words': count_words,
        'join_words': join_words,
        'complete_the_sentence': complete_the_sentence_2,
        'even_words': even_word,
        'nutrients': nutrients,
        'count_a': count_a,
        'run_length': run_length,
        'str2num':str2num,
        'str2dict': str2dict,
        'decode': decode,
        'operations': operations
})