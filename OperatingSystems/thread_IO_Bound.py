import threading
import requests
import time
import psutil
import os
import math

urls = [
    'https://www.w3schools.com/',
    'https://www.youtube.com',
    'https://www.github.com',
    'https://www.udemy.com/',
    'https://www.geeksforgeeks.org/'
]

def downloadURL(url):
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
    print(f"CPU Usage after thread: {cpuAfter:.4f}%")
    print(f"Memory Usage after thread: {memAfter:.4f} MB\n")

cpu = []
memory = []
def main():
    threads = []
    startTime = time.time()

    for url in urls:
        thread = threading.Thread(target=downloadURL, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    endTime = time.time()
    executionTime = endTime - startTime
    print("\nAll Threads Completed")
    print(f"Total Execution Time: {executionTime:.4f} seconds")
    print(f"Average CPU usage after threads: {sum(cpu) / len(cpu):.4f}%")
    print(f"Average memory usage after threads: {sum(memory) / len(memory):.4f} MB\n")

if __name__ == "__main__":
    main()
