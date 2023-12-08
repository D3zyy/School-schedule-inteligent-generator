
from Schedule.avaible_teachers import teachers
from Schedule.avaible_subjects import subjects
from Schedule.avaible_classes import classes
from Schedule.Schedule import Schedule
import random
import multiprocessing 
from multiprocessing import Lock
import time
from shared_primitivum import get_still_running
def generate_day(schedule, day):
    
    for i in range(10):
            random_number = random.randint(1,len(subjects))
            random_hour = random.randint(1, 10)
            random_class = random.randint(0, len(classes) - 1)
            random_teacher = random.randint(0, len(teachers) - 1)
            
            random_subject = random.randint(0, len(teachers[random_teacher].subjects) - 1)
            if random_number != len(subjects):
                while any(item.get('hour') == random_hour for item in schedule.schedule[day]):
                    random_hour = random.randint(1, 10)
                
                schedule.add_class(day, random_hour, classes[random_class], teachers[random_teacher], teachers[random_teacher].subjects[random_subject])
            else:
                 continue
def generate_schedule(queue,running,l):

     while running.value == True:
        l.acquire()
        try:
            s = Schedule()
            generate_day(s, "monday")
            generate_day(s, "tuesday")
            generate_day(s, "wednesday")
            generate_day(s, "thursday")
            generate_day(s, "friday")
            
            queue.put(s)
        finally:
             l.release()
        
