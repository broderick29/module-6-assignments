import multiprocessing
import time
import random
from datetime import datetime

def print_time():
    wait_time = random. random()
    time.sleep(wait_time)
    print(f"Process woke up after {wait_time:.3f} seconds at {datetime.now().strftime('%H:%M:%S.%f')}")

if __name__ == '__main__':
    process = []

    for i in range (3):
        p = multiprocessing.Process(target=print_time)
        process.append(p)
        p.start()

    for p in process:
        p.join()

    print("Process completed")