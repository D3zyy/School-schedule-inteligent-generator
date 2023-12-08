import time
from set_up_schedule import generate_schedule
from multiprocessing import Lock
from Schedule.avaible_classes import classes
from Schedule.avaible_teachers import teachers
from Schedule.avaible_subjects import subjects
from Schedule.Schedule import Schedule
import multiprocessing 
from multiprocessing import Lock
from shared_primitivum import get_still_running, WatchDog,wd
from Schedule_rater.rater import Rater

if __name__ == '__main__':
      try:
            #Amount of second to run the whole programm
            
            
            manager = multiprocessing.Manager()
            #Queue to store all the generated schedules
            generated_schedules = manager.Queue()
            lock = manager.Lock()
            score_of_rated_schedules = manager.list()
            rat = Rater()
            lock = Lock()
         
            #A variable that checks whether program is still running
            running = get_still_running()
            #Array to store all the processes
            processes = []
            #Process to active timer of the program
            wd_process = multiprocessing.Process(target=wd.activate_Timer, args=(running,))
            processes.append(wd_process)
            wd_process.start()
            while running.value == True:
                  number_of_processes = 3
                  #Starting x procceses to generate and rate the schedule 
                  
                  for y in range(number_of_processes):
                              process = multiprocessing.Process(target=generate_schedule, args=(generated_schedules,running,lock))

                              processes.append(process)
                              process.start()
                              time.sleep(0.005)
                              process_rating = multiprocessing.Process(target=rat.rate_Positions, args=(generated_schedules,running,score_of_rated_schedules,lock))
                              processes.append(process_rating)
                              
                              process_rating.start()
      
                              
                              
                        
                        

                  #Waiting for all processes to finish
                  for process in processes:
                              process.join()
                              print(f"Proces s PID {process.pid} skončil.")
            
            best_score = -999
            best_schedule = 1
            for schedule in score_of_rated_schedules:
                  if schedule.get_rating() > best_score and schedule is not None:
                   best_score = schedule.get_rating()
                   best_schedule = schedule
            print(f"Nejlepší score :{best_score}")
            print(best_schedule.display_schedule())
            print(f"Počet vygenerovaných rozvrhů : {generated_schedules.qsize()+len(score_of_rated_schedules)}")
            print(f"Počet ohodnocenených rozvrhů  : {len(score_of_rated_schedules)}")
            print(f"Počet  spuštěných procesů : {len(processes)}")
          
            
            
            
            
                      
                  

      except ValueError as e:
             print(e)
      except Exception as e:
             print(e)


    
        





