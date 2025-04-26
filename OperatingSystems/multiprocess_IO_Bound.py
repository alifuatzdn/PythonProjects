import multiprocessing
import requests
import time
import psutil
import os
import math
from multiprocessing import Process, Manager

urls = [
    'https://www.w3schools.com/',
    'https://www.youtube.com',
    'https://www.github.com',
    'https://www.udemy.com/',
    'https://www.geeksforgeeks.org/'
]

def downloadURL(url, cpu, memory):
    process = psutil.Process(os.getpid())
    psutil.cpu_percent(interval=None)
    local_start = time.time()

    response = requests.get(url)
    download_size = len(response.content)

    duration = time.time() - local_start
    cpuAfter = psutil.cpu_percent(interval=None)
    memAfter = process.memory_info().rss / math.pow(1024, 2)
    cpu.append(cpuAfter)
    memory.append(memAfter)

    print(f"\nDownloaded {url} ({download_size} bytes)")
    print(f"Time elapsed: {duration:.4f} seconds")
    print(f"CPU Usage after process: {cpuAfter:.4f}%")
    print(f"Memory Usage after process: {memAfter:.4f} MB\n")

def main():
    processes = []
    startTime = time.time()

    manager = Manager()
    cpu = manager.list()
    memory = manager.list()

    for url in urls:
        process = multiprocessing.Process(target=downloadURL, args=(url, cpu, memory))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    endTime = time.time()
    executionTime = endTime - startTime
    print("\nAll Processes Completed")
    print(f"Total Execution Time: {executionTime:.4} seconds")
    print(f"Average CPU usage after processes: {sum(cpu) / len(cpu):.4f}%")
    print(f"Average memory usage after processes: {sum(memory) / len(memory):.4f} MB\n")

if __name__ == "__main__":
    main()
