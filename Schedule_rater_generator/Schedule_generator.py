import time
from set_up_schedule import generate_schedule
from multiprocessing import Lock
from Schedule.avaible_classes import classes
from Schedule.avaible_teachers import teachers
from Schedule.avaible_subjects import subjects
from Schedule.Schedule import Schedule
import multiprocessing 
from multiprocessing import Lock
from shared_primitivum import get_still_running, WatchDog,wd,number_of_rated_schedules,best_scored_schedule,better_than_act_schedule
from Schedule_rater.rater import Rater

if __name__ == '__main__':

      #This is for compiler for .exe file for windows 
      multiprocessing.freeze_support()

      try:
            
                  while True:
                        try:
                              
                              time_to_run = int(input("Na jakou dobu chcete spustit generování a hodnocení: (1-6000 sekund) "))
                              if  1 <= time_to_run <= 6000:
                                    wd.set_timeout(time_to_run)
                                    break
                              else:
                                    print("Zadávejte číslo v rozmezí 1-6000.")
                        except:
                              print("Špatný input")
                  while True:
                        try:
                              
                              number_of_processes = str(input("Jak moc chcete zatížit procesor [A = slabě] [B = středně] [C = silně] "))
                              if number_of_processes == "A":
                                    number_of_processes = 2
                                    break
                              elif number_of_processes == "B":
                                     number_of_processes = 5
                                     break
                              elif number_of_processes == "C":
                                     number_of_processes = 23
                                     break
                              else:
                                    print("Zadávejte číslice A,B nebo C .")
                        except:
                              print("Špatný input")
                  


                  
                  
                  
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
                        
                        
                        #Starting x procceses to generate and rate the schedule 
                        
                        for y in range(number_of_processes):
                                    process = multiprocessing.Process(target=generate_schedule, args=(generated_schedules,running,lock))
                                    
                                    processes.append(process)

                                    process.start()
                                
                                    time.sleep(0.05)
                                    if wd_process.is_alive():
                                         


                                          process_rating = multiprocessing.Process(target=rat.rate_Positions, args=(generated_schedules,running,score_of_rated_schedules,lock,number_of_rated_schedules,best_scored_schedule,better_than_act_schedule))
                                          processes.append(process_rating)
                                          
                                          process_rating.start()
            
                                    
                                    
                              
                              

                        #Waiting for all processes to finish
                        for process in processes:
                                    process.join()
                                    
                  
                  best_score = float('-inf')
                  best_schedule = None

                  for schedule in score_of_rated_schedules:
                        
                        if schedule is not None:
                              if schedule.get_rating() > best_score:
                                    best_score = schedule.get_rating()
                                    
                                    best_schedule = schedule

                  # Now, best_schedule contains the schedule with the highest rating
                  # and best_score contains the corresponding rating.
                  
                  
                  print(best_schedule.display_schedule())
                  print(f"Počet vygenerovaných rozvrhů : {generated_schedules.qsize()+number_of_rated_schedules.value}")
                  print(f"Počet ohodnocenených rozvrhů  : {number_of_rated_schedules.value}")
                  print(f"Nejlepší score :{best_scored_schedule.value }")
                  print(f"Rozvrhů lepších než původně zadaný rozvrh : {better_than_act_schedule.value }")
                  end = input("Pro ukončení stistkněte jakoukoliv klávesu")
                  
            
                  
                  
                  
                  
                        
                        

      except ValueError as e:
            print(e)
      except Exception as e:
            print(e)
      except:
            print("Error")