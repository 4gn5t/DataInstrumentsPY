from joblib import Parallel, delayed

def square(x):
    return x * x

if __name__ == '__main__':
    results = Parallel(n_jobs=4)(delayed(square)(i) for i in range(10))
    print(results)