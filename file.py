from collections import deque

my_cache = deque()

my_cache.append(1)
my_cache.append(2)
my_cache.append(3)

my_cache.appendleft(-1) 
my_cache.appendleft(-2) 
my_cache.appendleft(-3)

print(my_cache)
