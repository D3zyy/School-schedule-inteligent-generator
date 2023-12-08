import multiprocessing 
from WatchDog.Watchdog import WatchDog

#An object that sets the amount of time  of the program
wd = WatchDog(10)



#Variable to check whether program is still running through the whole project
still_running = multiprocessing.Value('b',True)
     
def get_still_running():
            return still_running


