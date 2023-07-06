import random
import time





def decorator(func: function):
    def wrapper(*params, kwargs):
        start_time = time.time():
        result = func(*params, **kwargs)
        end_time = time.time()
        print(f'{func.__name__} was running for{end_time=start_time}')
    
    return(wrapper)

def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)

        return cache[args]
    wrapper



@time_measure_decorator
def hard_compulation_function(n):
    time.sleep(n)
    print('function done')
def main():
hard_compulation_function()

if __name__ = '__main__':
    main()