import random

import multiprocessing
import random
import time
from threading import current_thread

import reactivex
from reactivex.scheduler import ThreadPoolScheduler
from reactivex import operators as op


'''
Code for creating pool_scheduler from https://rxpy.readthedocs.io/en/latest/get_started.html#operators-and-chaining
'''
optimal_thread_count = multiprocessing.cpu_count()
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

def createUserName():

    return random.choice(nouns) + str(random.randint(0, 999)) + random.choice(nouns)


def simulatewait(x):

    time.sleep(random.randint(5, 15) * 0.1)
    return x


def noBadWords():
    pass


def noPrimeNumbers():
    pass


'''
Activity 1:

This Activity is done for you, use this as a guide for the others
'''
reactivex.range(0, 100).pipe(
    op.map(lambda b: simulatewait(b)), op.subscribe_on(pool_scheduler)
).subscribe( 
    on_next = lambda a: print("Activity 2: " + str(a)),
    on_error = lambda e: print(e),
    on_completed = lambda: print("Done")
)

'''
Activity 2:


'''
reactivex.range(0, 100).pipe(
    op.map(lambda b: simulatewait(b)), op.subscribe_on(pool_scheduler)
).subscribe( 
    on_next = lambda a: print("Activity 2: " + str(a)),
    on_error = lambda e: print(e),
    on_completed = lambda: print("Done")
)

def fizzBuzz(num):

    if num % 3 == 0 and num % 5 == 0:
        return "Fizzbuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

    
'''
Activity 3: Fizzbuzz



'''
reactivex.range(0, 100).pipe(
    op.map(lambda a: fizzBuzz(a)), op.map(lambda b: simulatewait(b)), op.subscribe_on(pool_scheduler)
).subscribe(
    on_next = lambda a: print("Activity 3: " + str(a)),
    on_error = lambda e: print(e),
    on_completed = lambda: print("Done")
)


'''
Activity 4: Username Filtering

'''

nouns = [
    "apple", "ball", "cat", "dog", "elephant", "flower", "guitar", "hat", "igloo", "jacket",
    "kite", "lemon", "mountain", "notebook", "ocean", "pencil", "quilt", "rabbit", "sun", "tree",
    "umbrella", "violin", "watermelon", "xylophone", "yacht", "zebra", "ant", "bear", "car", "desk",
    "elephant", "fish", "garden", "house", "ice cream", "jellyfish", "key", "lion", "map", "nest",
    "orange", "penguin", "quokka", "rose", "shark", "turtle", "unicorn", "volcano", "wagon", "xylophone",
    "yogurt", "zeppelin", "astronaut", "butterfly", "cloud", "dolphin", "eagle", "fire", "giraffe", "helicopter",
    "island", "jungle", "koala", "lighthouse", "moon", "narwhal", "octopus", "panda", "quill", "rocket",
    "sailboat", "tiger", "ufo", "vase", "whale", "xylophone", "yeti", "zebra", "airplane", "banana",
    "computer", "dragon", "earth", "forest", "globe", "hammer", "iceberg", "jigsaw", "kangaroo", "laptop",
    "mushroom", "necklace", "ostrich", "palm tree", "quiver", "rainbow", "seahorse", "tornado", "umbrella", "volleyball",
    "waffle", "xylophone", "yarn", "zeppelin", "alligator", "bicycle", "candle", "diamond", "eiffel tower", "flamingo",
    "guitar", "hamburger", "ice cream", "jellyfish", "kangaroo", "leopard", "monkey", "ninja", "octopus", "penguin",
    "quokka", "raccoon", "starfish", "tiger", "unicorn", "volcano", "walrus", "xylophone", "yak", "zebra",
    "apricot", "butterfly", "caterpillar", "dandelion", "elephant", "fireworks", "giraffe", "hedgehog", "igloo", "jackal",
    "kite", "lemur", "mushroom", "narwhal", "ostrich", "panda", "quill", "rhinoceros", "sloth", "toucan", "umbrella",
    "vulture", "walnut", "xylophone", "yacht", "zeppelin",
    "blue sky", "coffee cup", "rainbow bridge", "bookshelf", "moonlight", "ocean breeze",
    "mountain peak", "firefighter", "flower garden", "chocolate cake", "beach ball", "sunflower field",
    "waterfall", "laptop computer", "beehive", "candlestick", "picnic basket", "pineapple juice",
    "coffee beans", "sailing boat", "swimming pool", "dragonfly", "paper airplane", "secret key",
    "baby elephant", "night sky", "fireworks display", "butterfly wings", "jungle safari",
    "palm tree", "desert sand", "mountain lion", "campfire", "starfish beach", "singing bird",
    "umbrella handle", "panda bear", "rocket launch", "snowy owl", "chocolate chip", "iceberg lettuce",
    "rainbow fish", "blue whale", "jigsaw puzzle", "hot air balloon", "sunrise view", "snowy mountain",
    "campfire smoke", "watermelon slice", "yarn ball", "zeppelin airship", "eagle eye", "raindrop"
]

bad_words = ["umbrella", "xylophone", "narwhal", "hammer", "flamingo", "quill", "waffle", "mushroom", "bicycle"]


user_names = []


reactivex.range(0, 100).pipe(
    op.map(lambda a: createUserName()), op.map(lambda b: simulatewait(b)), op.subscribe_on(pool_scheduler)
).subscribe( 
    on_next = lambda a: print("Activity 4: Accepted Username " + a),
    on_error = lambda e: print(e),
    on_completed = lambda: print("Done")
)



