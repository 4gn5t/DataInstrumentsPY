from joblib import Parallel, delayed

def square(x):
    return x * x

def cube(x):
    return x ** 3

if __name__ == '__main__':
    results = Parallel(n_jobs=4)(delayed(square)(i) if i % 2 == 0 else delayed(cube)(i) for i in range(10))
    print(results)