import threading
import time
import math
import psutil
import os

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def countPrimes(start, end):
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
    print(f"CPU Usage after thread: {cpuAfter:.4f}%")
    print(f"Memory Usage after thread: {memAfter:.4f} MB\n")

cpu = []
memory = []
def main():
    startTime = time.time()

    threads = [
        threading.Thread(target=countPrimes, args=(0, 100000)),
        threading.Thread(target=countPrimes, args=(0, 200000)),
        threading.Thread(target=countPrimes, args=(0, 300000)),
        threading.Thread(target=countPrimes, args=(0, 400000)),
        threading.Thread(target=countPrimes, args=(0, 500000)),
    ]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    endTime = time.time()
    executionTime = endTime - startTime
    print("\nAll Threads Completed")
    print(f"Total Execution Time: {executionTime:.4f} seconds")
    print(f"Average CPU usage after threads: {sum(cpu) / len(cpu):.4f}%")
    print(f"Average memory usage after threads: {sum(memory) / len(memory):.4f} MB\n")

if __name__ == "__main__":
    main()
