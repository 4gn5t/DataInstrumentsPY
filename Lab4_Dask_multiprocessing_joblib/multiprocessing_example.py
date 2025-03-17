from multiprocessing import Pool

def square(x):
    return x * x

if __name__ == "__main__":
    pool = Pool(processes=4)
    results = pool.map(square, [1, 2, 3, 4])
    print(results)