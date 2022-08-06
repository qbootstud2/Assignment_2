#!/usr/bin/env python
"""
Generate random numbers
"""
import random

def exercise_random(num: int) -> None:
    """ exercise methods in Python module random"""
    print("\nUse system clock as seed to generate floats")
    print(random.random())
    print(random.random())
    random_float_list = [random.random() for _ in range(num)]
    print(f"Random floats: {random_float_list}")
    
    random.seed() # uses system clock as seed
    print("\nUse system clock as seed to generate floats")
    print(random.random())
    print(random.random())
    random_float_list = [random.random() for _ in range(num)]
    print(f"Random floats: {random_float_list}")
    
    random.seed(17) # use number as seed
    print("\nUse number 17 as seed")
    print(random.random())
    print(random.random())
    random_float_list = [random.random() for _ in range(num)]
    print(f"Random floats: {random_float_list}")

    print("\nGenerate ints in range -31 to +31 -- 32 not included")
    print("random.randrange(start, stop, step)")
    print(random.randrange(-31, 32))
    print(random.randrange(-31, 32, 2))
    random_int_list = [random.randrange(-31, 32) for _ in range(num)]
    print(f"Random ints: {random_int_list}")
    
    print("\nGenerate ints in range -31 to +32 -- last one included")
    print("random.randint(start, stop)")
    print(random.randint(-31, 32))
    print(random.randint(-31, 32))
    random_int_list = [random.randint(-31, 32) for _ in range(num)]
    print(f"Random ints: {random_int_list}")

if __name__ == "__main__":
    print(__doc__)
    exercise_random(5)





