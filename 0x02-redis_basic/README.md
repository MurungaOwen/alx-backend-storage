# basic intro to redis cache system
a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

```
bob@dylan:~$ cat main.py
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

bob@dylan:~$ python3 main.py 
3a3e8231-b2f6-450d-8b0e-0f38f16e8ca2
b'hello'
bob@dylan:~$ 
```
In this tasks, we will implement a replay function to display the history of calls of a particular function.
Use keys generated in previous tasks to generate the following output:

## task 3
Familiarize yourself with redis commands RPUSH, LPUSH, LRANGE, etc.
In this task, we will define a call_history decorator to store the history of inputs and outputs for a particular function.
Everytime the original function will be called, we will add its input parameters to one list in redis, and store its output into another list.
In call_history, use the decorated function’s qualified name and append ":inputs" and ":outputs" to create input and output list keys, respectively.
call_history has a single parameter named method that is a Callable and returns a Callable.
In the new function that the decorator will return, use rpush to append the input arguments. Remember that Redis can only store strings, bytes and numbers. Therefore, we can simply use str(args) to normalize. We can ignore potential kwargs for now.
Execute the wrapped function to retrieve the output. Store the output using rpush in the "...:outputs" list, then return the output.
Decorate Cache.store with call_history.