import joblib
from joblib import Parallel, delayed
from multiprocessing import cpu_count
from multiprocessing import Pool
import time 
import random
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

def compute_intensive_task_normal_dist(n):
    numbers = generate_random_numbers_normal(n)
    for _ in range(20):  
        numbers.sort()
        numbers = numbers[::-1]
        numbers = [math.sin(x) * math.cos(x) / (abs(x) + 0.01) for x in numbers]
        # numbers = [math.exp(abs(x) % 1) * math.log(abs(x) + 1.1) for x in numbers]
    return numbers

def compute_intensive_task_rand_dist(n):
    numbers = generate_random_numbers(n)
    for _ in range(20):  
        numbers.sort()
        numbers = numbers[::-1]
        numbers = [math.sin(x) * math.cos(x) / (abs(x) + 0.01) for x in numbers]
        # numbers = [math.exp(abs(x) % 1) * math.log(abs(x) + 1.1) for x in numbers]
    return numbers

def run_both_tasks(n):
    normal_result = compute_intensive_task_normal_dist(n)
    rand_result = compute_intensive_task_rand_dist(n)
    return normal_result, rand_result

if __name__ == "__main__":
    num_cores = cpu_count()
    print(f"Number of CPU cores: {num_cores}")
    n = 200_000
    num_tasks = 4
    start = time.time()
    serial_results = [run_both_tasks(n) for _ in range(num_tasks)]
    end = time.time()
    serial_time = end - start
    print(f'Serial (both distributions): {serial_time:.2f} sec')
    start = time.time()
    joblib_results = Parallel(n_jobs=num_cores)(
        delayed(run_both_tasks)(n) for _ in range(num_tasks)
    )
    end = time.time()
    joblib_time = end - start
    print(f'Joblib (both distributions): {joblib_time:.2f} sec')
    pool = Pool(processes=num_cores)
    start = time.time()
    mp_results = pool.map(run_both_tasks, [n] * num_tasks)
    end = time.time()
    mp_time = end - start
    print(f'Multiprocessing (both distributions): {mp_time:.2f} sec')
    pool.close()
    pool.join()
