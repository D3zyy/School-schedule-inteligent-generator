from avaible_classes import classes
from avaible_teachers import teachers
from avaible_subjects import subjects
from Schedule import Schedule
import random

def generateMonday(schedule):
    # Generate none lesson or normal lesson
    random_number_none = random.randint(1, len(subjects))

    if random_number_none == len(subjects):
        print("None")
    else:
        for i in range(10):
            #Generating random number for hour,subject,class,teacher
            random_hour = random.randint(1, 10)
            random_subject = random.randint(0, len(subjects)-1)
            random_class = random.randint(0, len(classes)- 1)
            random_teacher = random.randint(0, len(teachers) - 1)
            print(f"Random hour number: {random_hour}")
            
            if any(item.get('hour') == random_hour for item in schedule.schedule['monday']):
               print()
            else:
                schedule.add_class("monday", random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])
     
s1 = Schedule()
generateMonday(s1)
s1.display_schedule()


def generateSchedule(self):

    s = Schedule()
    






