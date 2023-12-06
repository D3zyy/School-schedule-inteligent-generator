from set_up_schedule import generate_schedule
from multiprocessing import Lock
from Schedule.avaible_classes import classes
from Schedule.avaible_teachers import teachers
from Schedule.avaible_subjects import subjects
from Schedule.Schedule import Schedule
import multiprocessing 
from multiprocessing import Lock
from WatchDog.Watchdog import WatchDog
from WatchDog_checker import get_still_running


if __name__ == '__main__':
        #Amount of second to run the whole programm
        seconds = 3
        wd = WatchDog(seconds)
        manager = multiprocessing.Manager()
        #Queue to store all the generated schedules
        generated_schedules = manager.Queue()
        #A variable that checks whether program is still running
        running = get_still_running()
        #Array to store all the processes
        processes = []
        
        wd_process = multiprocessing.Process(target=wd.activate_Timer, args=(running,))
        wd_process.start()
        
    
        while running.value == True:
              

            for i in range(4):
                    process = multiprocessing.Process(target=generate_schedule, args=(generated_schedules,running))
                    processes.append(process)
                    process.start()
            
            for process in processes:
                        process.join()
                        print(f"Proces s PID {process.pid} skončil.")
        

        print(f"Počet vygenerovaných rozvrhů : {generated_schedules.qsize()}")
        print(f"Počet (nejspíše) zatížených jader : {len(processes)}")
    


    
        





