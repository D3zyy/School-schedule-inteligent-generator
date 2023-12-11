import multiprocessing 
from WatchDog.Watchdog import WatchDog

#An object that sets the amount of time  of the program
wd = WatchDog(1)



#Variable to check whether program is still running through the whole project
still_running = multiprocessing.Value('b',True)
number_of_rated_schedules = multiprocessing.Value('i',0)
best_scored_schedule = multiprocessing.Value('i',-90000)
better_than_act_schedule = multiprocessing.Value('i',0)
def get_still_running():
            return still_running


