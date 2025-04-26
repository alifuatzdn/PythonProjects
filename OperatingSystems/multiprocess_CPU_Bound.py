import time
import math
import psutil
import os
from multiprocessing import Process, Manager

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def countPrimes(start, end, cpu, memory):
    process = psutil.Process(os.getpid())
    psutil.cpu_percent(interval=None)
    local_start = time.time()

    cnt = 0
    for i in range(start, end):
        if isPrime(i):
            cnt += 1

    duration = time.time() - local_start
    cpuAfter = psutil.cpu_percent(interval=None)
    memAfter = process.memory_info().rss / math.pow(1024, 2)
    cpu.append(cpuAfter)
    memory.append(memAfter)

    print(f"\nTotal prime numbers in range({start}, {end}): {cnt}")
    print(f"Time elapsed: {duration:.4f} seconds")
    print(f"CPU Usage after process: {cpuAfter:.4f}%")
    print(f"Memory Usage after process: {memAfter:.4f} MB\n")

cpu = []
memory = []
def main():
    startTime = time.time()

    manager = Manager()
    cpu = manager.list()
    memory = manager.list()

    processes = [
        Process(target=countPrimes, args=(0, 100000, cpu, memory)),
        Process(target=countPrimes, args=(0, 200000, cpu, memory)),
        Process(target=countPrimes, args=(0, 300000, cpu, memory)),
        Process(target=countPrimes, args=(0, 400000, cpu, memory)),
        Process(target=countPrimes, args=(0, 500000, cpu, memory)),
    ]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    endTime = time.time()
    executionTime = endTime - startTime
    print("\nAll Processes Completed")
    print(f"Total Execution Time: {executionTime:.4} seconds")
    print(f"Average CPU usage after processes: {sum(cpu) / len(cpu):.4f}%")
    print(f"Average memory usage after processes: {sum(memory) / len(memory):.4f} MB\n")

if __name__ == "__main__":
    main()
