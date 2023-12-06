from avaible_classes import classes
from avaible_teachers import teachers
from avaible_subjects import subjects
from Schedule import Schedule
import random

def generateMonday(schedule):
    for i in range(10):
        #Generating random number for hour,subject,class,teacher
        random_hour = random.randint(1, 10)
        random_subject = random.randint(0, len(subjects)-1)
        random_class = random.randint(0, len(classes)- 1)
        random_teacher = random.randint(0, len(teachers) - 1)
            
        while any(item.get('hour') == random_hour for item in schedule.schedule['monday']):
                random_hour = random.randint(1, 10)
                random_number_none = random.randint(0, len(subjects))
                if random_number_none == len(subjects):
                    break
        else:
                schedule.add_class("monday", random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])

def generateTuesday(schedule):
    for i in range(10):
        #Generating random number for hour,subject,class,teacher
        random_hour = random.randint(1, 10)
        random_subject = random.randint(0, len(subjects)-1)
        random_class = random.randint(0, len(classes)- 1)
        random_teacher = random.randint(0, len(teachers) - 1)
            
        while any(item.get('hour') == random_hour for item in schedule.schedule['tuesday']):
                random_hour = random.randint(1, 10)
                random_number_none = random.randint(0, len(subjects))
                if random_number_none == len(subjects):
                    break
        else:
                schedule.add_class("tuesday", random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])
def generateWednesday(schedule):
    for i in range(10):
        #Generating random number for hour,subject,class,teacher
        random_hour = random.randint(1, 10)
        random_subject = random.randint(0, len(subjects)-1)
        random_class = random.randint(0, len(classes)- 1)
        random_teacher = random.randint(0, len(teachers) - 1)
            
        while any(item.get('hour') == random_hour for item in schedule.schedule['wednesday']):
                random_hour = random.randint(1, 10)
                random_number_none = random.randint(0, len(subjects))
                if random_number_none == len(subjects):
                    break
        else:
                schedule.add_class("wednesday", random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])
def generateThursday(schedule):
    for i in range(10):
        #Generating random number for hour,subject,class,teacher
        random_hour = random.randint(1, 10)
        random_subject = random.randint(0, len(subjects)-1)
        random_class = random.randint(0, len(classes)- 1)
        random_teacher = random.randint(0, len(teachers) - 1)
            
        while any(item.get('hour') == random_hour for item in schedule.schedule['thursday']):
                random_hour = random.randint(1, 10)
                random_number_none = random.randint(0, len(subjects))
                if random_number_none == len(subjects):
                    break
        else:
                schedule.add_class("thursday", random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])

def generateFriday(schedule):
    for i in range(10):
        #Generating random number for hour,subject,class,teacher
        random_hour = random.randint(1, 10)
        random_subject = random.randint(0, len(subjects)-1)
        random_class = random.randint(0, len(classes)- 1)
        random_teacher = random.randint(0, len(teachers) - 1)
            
        while any(item.get('hour') == random_hour for item in schedule.schedule['friday']):
                random_hour = random.randint(1, 10)
                random_number_none = random.randint(0, len(subjects))
                if random_number_none == len(subjects):
                    break
        else:
                schedule.add_class("friday", random_hour, classes[random_class], teachers[random_teacher], subjects[random_subject])


s1 = Schedule()

generateTuesday(s1)
generateMonday(s1)
generateWednesday(s1)
generateThursday(s1)
generateFriday(s1)
s1.display_schedule()


def generateSchedule(self):

    s = Schedule()
    






