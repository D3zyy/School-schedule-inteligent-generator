from avaible_classes import classes
from avaible_teachers import teachers
from avaible_subjects import subjects
from Schedule import Schedule
import random
import multiprocessing
import time

def generate_day(schedule, day):
    for i in range(10):
        random_hour = random.randint(1, 10)
        random_subject = random.randint(0, len(subjects) - 1)
        random_class = random.randint(0, len(classes) - 1)
        random_teacher = random.randint(0, len(teachers) - 1)

        while any(item.get('hour') == random_hour for item in schedule.schedule[day]):
            random_hour = random.randint(1, 10)

        schedule.add_class(day, random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])

def generate_schedule():
    s = Schedule()
    generate_day(s, "monday")
    generate_day(s, "tuesday")
    generate_day(s, "wednesday")
    generate_day(s, "thursday")
    generate_day(s, "friday")
    s.display_schedule()
    

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    generated_schedules = manager.list()

    processes = []

    for i in range(5000):
        process = multiprocessing.Process(target=generate_schedule)
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    
        


    

    
        





