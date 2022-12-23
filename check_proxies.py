import threading
import queue
import time
import requests

# get the start time
st = time.time()

q = queue.Queue()
valid_proxies = []

with open("proxies.txt", "r") as f:
    proxies = f.read().split("/n")
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("https://ipinfo.io/json",
                                proxies = {"http:": proxy,"https:": proxy}, timeout = 3)
        except:
            continue
        if res.status_code == 200:
            print(proxy)
            time.sleep(0.5)
            

for _ in range(20):
    threading.Thread(target=check_proxies).start()

et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

