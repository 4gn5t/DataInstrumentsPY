from joblib import Parallel, delayed, dump, load

def my_function(x):
    return x ** 5
    return result

results = Parallel(n_jobs=4)(delayed(my_function)(i) for i in range(10))
print(f'results: {results}')
dump(results, 'results.pkl')

loaded_results = load('results.pkl')
print(f'loaded results: {loaded_results}')