import threading
import time
import requests
import concurrent.futures

def sleeping():
    time.sleep(1)
    print('zzzzzzzzzzzzz')
    return 'hello'

with concurrent.futures.ThreadPoolExecutor() as TPE:
    task_1 = TPE.submit(sleeping)
    task_2 = TPE.submit(sleeping)
    print(task_1.result())
    print(task_2.result())

#threads = []

#for i in range(4):
    #thread = threading.Thread(target=sleeping)
    #thread.start()
   # threads.append(thread)

#for thread in threads:
   # thread.join()

#print(threading.active_count())
print(time.perf_counter())
#print("All threads have finished.")
