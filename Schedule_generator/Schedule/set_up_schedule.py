
from .avaible_teachers import teachers
from .avaible_subjects import subjects
from .avaible_classes import classes
from .Schedule import Schedule
import random
import multiprocessing 
from multiprocessing import Lock
import time
from WatchDog.Watchdog import WatchDog


def generate_day(schedule, day):
    for i in range(10):
        random_hour = random.randint(1, 10)
        random_subject = random.randint(0, len(subjects) - 1)
        random_class = random.randint(0, len(classes) - 1)
        random_teacher = random.randint(0, len(teachers) - 1)

        while any(item.get('hour') == random_hour for item in schedule.schedule[day]):
            random_hour = random.randint(1, 10)

        schedule.add_class(day, random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])

def generate_schedule(queue,seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
         
       
        s = Schedule()
        generate_day(s, "monday")
        generate_day(s, "tuesday")
        generate_day(s, "wednesday")
        generate_day(s, "thursday")
        generate_day(s, "friday")

        queue.put(s)
