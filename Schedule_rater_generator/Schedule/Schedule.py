import multiprocessing
from .avaible_classes import classes
from .avaible_teachers import teachers
from .Class import Class
from .Teacher import Teacher
from .Subject import Subject

class Schedule(multiprocessing.Process):
    def __init__(self):
    # Dictionary to store the schedule for each day of the week
        self.schedule = {
            'monday': [],
            'tuesday': [],
            'wednesday': [],
            'thursday': [],
            'friday': []
        }
        self.rating = 30000
    def set_rating(self,value):
        self.rating = value
    def get_rating(self):
        return self.rating
    def get_day_items(self,day : str):
        monday_schedule = self.schedule.get(day, [])
        formatted_items = []

        for item in monday_schedule:
            formatted_item = {
                'hour': item.get('hour'),
                'class': item.get('class').get_id(),
                'teacher': item.get('teacher').get_last_name(),
                'subject': item.get('subject').get_name(),
                'location' : item.get('class').get_location()
            }
            formatted_items.append(formatted_item)
            

        return formatted_items
        
   #Check valid inputs 
    def check_hour(self, value):
        if isinstance(value, int) and 0 < value <= 10:
            return value
        else:
            raise ValueError("Hour must be an integer and between 1-10!")

    #Check valid inputs from class object
    def check_class_id(self,value):
        if  isinstance(value, Class) and 0 < value.get_id():

            return value
        else:
            raise ValueError("class id must be higher than 0")
    #check valid inputs from teacher object
    def check_teacher_name(self,value):
        if isinstance(value,Teacher) and value.get_first_name is not None and value.get_last_name is not None:
            return value
        else:
            raise ValueError("Either it is not a teacher object or name has not been set.")
    def check_subject(self,value):
        if isinstance(value,Subject) and value.get_name is not None:
            return value
        else:
            raise ValueError("Either it is not a subject object or name has not been set.")
    def add_class(self, day, hour, class_id, teacher_name, subject_name):
        # Add a lesson to the schedule
        # Each method check valid inputs
        verified_hour = self.check_hour(hour)
        verified_class_id = self.check_class_id(class_id)
        verified_teacher_name = self.check_teacher_name(teacher_name)
        verified_subject = self.check_subject(subject_name)


        self.schedule[day].append({
            'hour': verified_hour,
            'class': verified_class_id,
            'teacher': verified_teacher_name,
            'subject': verified_subject
        })

    def display_schedule(self):
        # Display the entire schedule
        for day, lessons in self.schedule.items():
            print(f'{day.capitalize()}:')
            for number in range(1,11):
                found = False
                for lesson in lessons:
                    
                    if lesson['hour'] == number:
                        print(f"{lesson['hour']}. hour  Class: {lesson['class'].get_id()}, Teacher: {lesson['teacher'].get_first_name()} {lesson['teacher'].get_last_name()}, Subject: {lesson['subject'].get_name()}")
                        found = True
                        break
                
                if not found:
                    print(f"{number}. hour  Volno")
                
                





