from ttgtcanvas2 import get_robo_builder
import random

def nested_get(dic, key):
    k = key.split('.')
    for x in k:
        if dic is not None:
            dic = dic.get(x, None)
        else:
            return None
    return dic

        
def nested_keys(world):
    my_dict = {
        'fruits': {
            'red': {'round': 'apple', 'small': 'strawberry', 'long': 'carrot'},
            'yellow': 'banana'
        },
        'flowers': {
            'white': 'daisy',
            'red': 'tulip'
        },
        'shiny': 'star'
    }
    keys = ['fruits.yellow', 'fruits.red.long', 'flowers.red', 'flowers.white', 'fruits.red.small', 'fruits.red.round','shiny']
    e = random.sample(keys, random.randint(2,4))
    vals = [nested_get(my_dict,x) for x in e]
    allx= ['apple', 'strawberry', 'carrot', 'banana', 'tulip', 'daisy','star']
    for x in range(len(allx)):
        if allx[x] in vals:
            world.add_pick_obj_goal(x+1, 2, allx[x], 1)
        world.add_object(x+1,2,allx[x], 1)
    for y in range(len(e)):
        world.add_msg(y+2, 1, e[y])
    
def using_zip(world):
    keys = ["carrot", "banana", "apple", "strawberry", "tulip", "star", "leaf"]
    values = [random.randint(2,4), random.randint(2,10), random.randint(2,10), random.randint(2,10), random.randint(2,10), random.randint(2,10), random.randint(2,10)]
    dic = dict(zip(keys, values))
    test = random.sample(keys, random.randint(3,5))
    s = sum(dic[x] for x in test)
    for x in range(len(keys)):
        world.add_object(x+2, 1, keys[x], 1)
        world.add_msg(x+2, 2, values[x])
    for x in range(len(test)):
        world.add_object(x+1,3,test[x],1)
    world.add_repoter_goal(f"Total Cost: {s}")

def enc(secret, msg):
    ret = ''
    for c in msg:
        if c.islower():
            ret += secret.get(c, c)
        elif c.isupper():
            c = c.lower()
            ret += secret.get(c, c).upper()
        else:
            ret += c  
    return ret

def encryption(world):
    msg = "abcdefghijklmnopqrstuvwxyz"
    secret=list(msg)
    random.shuffle(secret)
    secret = "".join(secret)
    world.add_msg(1,1, msg)
    world.add_msg(2,1, secret)
    msgs = [
        "Beautiful is better than ugly",
        "Explicit is better than implicit",
        "Simple is better than complex",
        "Complex is better than complicated",
        "Flat is better than nested",
        "Sparse is better than dense",
        "Readability counts",
        "Special cases aren't special enough to break the rules",
        "Practicality beats purity",
        "Errors should never pass silently",
        "Errors should never pass silently unless explicitly silenced",
        "In the face of ambiguity, refuse the temptation to guess"
    ]
    
    enc_secret = dict(zip(msg,secret))
    msg1, msg2 = random.sample(msgs,2)
    world.add_msg(3,1, msg1)
    world.add_repoter_goal(enc(enc_secret, msg1))

    world.add_msg(4,1, enc(enc_secret,msg2))
    world.add_repoter_goal(msg2)



def decryption(world):
    rot13 = {'a':'n', 'b':'o', 'c':'p',
             'd':'q', 'e':'r', 'f':'s',
             'g':'t','h':'u','i':'v',
             'j':'w', 'k':'x','l':'y',
             'm':'z','n':'a','o':'b',
             'p':'c','q':'d','r':'e',
             's':'f','t':'g','u':'h',
             'v':'i', 'w':'j','x':'k',
             'y':'l','z':'m'}


    msgs = [
        "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Never let the fear of striking out keep you from playing the game."
    ]
    
    msg1 = random.choice(msgs)
    world.add_msg(1,1, enc(rot13, msg1))
    world.add_repoter_goal(msg1)

get_robo=get_robo_builder(levels = {
        "nested_keys": nested_keys,
        "using_zip": using_zip,
        "encryption":encryption,
        "decryption": decryption
})