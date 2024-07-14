import concurrent.futures
import time


def heavy_computation(x):
    time.sleep(1)  # Simulate a time-consuming computation
    return x * x

if __name__ == '__main__':
    inputs = list(range(8))
    tic = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(heavy_computation, inputs))
    print(time.time()-tic)
    print(results)
