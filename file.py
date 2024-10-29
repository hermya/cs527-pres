from collections import deque
from my_collections.my_deque import Deque as myDeque
my_cache = deque()

my_cache.append(1)
my_cache.append(2)
my_cache.append(3)

my_cache.appendleft(-1) 
my_cache.appendleft(-2) 
my_cache.appendleft(-3)

print(my_cache)

my_cache = myDeque()
my_cache.addRight(Node(1))
my_cache.addRight(Node(2))
my_cache.addRight(Node(3))

my_cache.addLeft(Node(-1))
my_cache.addLeft(Node(-2))
my_cache.addLeft(Node(-3))

my_cache.print()