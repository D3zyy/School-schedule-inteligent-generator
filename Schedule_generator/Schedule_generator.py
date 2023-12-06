from Schedule.set_up_schedule import generate_schedule
from multiprocessing import Lock
from Schedule.avaible_classes import classes
from Schedule.avaible_teachers import teachers
from Schedule.avaible_subjects import subjects
from Schedule.Schedule import Schedule
import random
import multiprocessing 
from multiprocessing import Lock
import time
from WatchDog.Watchdog import WatchDog



if __name__ == '__main__':
    manager = multiprocessing.Manager()
    generated_schedules = manager.Queue()
    
    processes = []
    
    
    for i in range(1):
            process = multiprocessing.Process(target=generate_schedule, args=(generated_schedules,))
            processes.append(process)
            process.start()
    for process in processes:
            process.join()
            print(f"Proces s PID {process.pid} skončil.")
    
    

    print(f"Počet vygenerovaných rozvrhů : {generated_schedules.qsize()}")
    print(f"Počet (nejspíše) zatížených jader : {len(processes)}")
    
        


    

    
        





