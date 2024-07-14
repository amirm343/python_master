import concurrent.futures
import time

def heavy_computation(n):

    time.sleep(1)  
    return n * n

inputs = list(range(12))

tic = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(heavy_computation, inputs))

print(time.time()-tic)

print(results)