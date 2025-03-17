from multiprocessing import Process, Array

def f(n, a):
    a[n] = n * 2

if __name__ == '__main__':
    num_processes = 4
    arr = Array('i', range(num_processes))

    processes = []
    for i in range(num_processes):
        p = Process(target=f, args=(i, arr))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    print(arr[:]) 