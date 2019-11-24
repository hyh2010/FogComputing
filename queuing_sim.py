import psutil
from subprocess import Popen
import threading
import time
import numpy as np

# First simulate a M/M/1 Queue. Arrival rate 1 customer/ 2 minute mean service time 1 minute
lambd = 1/60
mu = 1/45

user_count = 0

def user_join():
    global user_count
    user_count += 1
    logfile = 'user_data/' + 'user' + str(user_count) + '_data.csv'
    p = Popen(['python', 'client_for_phone.py', logfile])
    print("user joins", logfile)
    service_time = np.random.exponential(1/mu)
    time.sleep(service_time)
    psutil.Process(p.pid).terminate()
    print("user leaves", logfile)


while True:
    interarrival = np.random.exponential(1/lambd)
    time.sleep(interarrival)
    threading.Thread(target=user_join).start()

