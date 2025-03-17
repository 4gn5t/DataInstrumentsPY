from multiprocessing import Pool
from multiprocessing import cpu_count
import random
import time
import multiprocessing as mp
import math

def generate_random_numbers(n):
    return [random.random() for _ in range(n)]

def generate_random_numbers_normal(n):
    result = []
    for _ in range(n):
        u1 = random.random()
        u2 = random.random()
        z0 = math.sqrt(-2 * math.log(u1)) * math.cos(2 * math.pi * u2)
        result.append(z0)
    return result

def compute_intensive_task(n):
    numbers = generate_random_numbers_normal(n)
    for _ in range(20):  
        numbers.sort()
        numbers = numbers[::-1]
        numbers = [math.sin(x) * math.cos(x) / (abs(x) + 0.01) for x in numbers]
        numbers = [math.exp(abs(x) % 1) * math.log(abs(x) + 1.1) for x in numbers]
    return numbers

if __name__ == "__main__":
    print(cpu_count())
    mp.set_start_method('spawn', force=True)
    n = 400000  
    start = time.time()
    seq_results = [compute_intensive_task(n) for _ in range(cpu_count())]
    end = time.time()
    sequential_time = end - start
    print(f'Sequential {sequential_time} sec')
    pool = Pool(processes=cpu_count())
    start = time.time()
    results = pool.map(compute_intensive_task, [n] * cpu_count())
    end = time.time()
    parallel_time = end - start
    print(f'Parallel {parallel_time} sec')
    pool.close()
    pool.join()
    