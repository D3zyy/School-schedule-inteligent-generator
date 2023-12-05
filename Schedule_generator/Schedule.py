from avaible_classes import classes
from avaible_teachers import teachers
from Class import Class
from Teacher import Teacher

class Schedule:
    def __init__(self):
    # Dictionary to store the schedule for each day of the week
        self.schedule = {
            'monday': [],
            'tuesday': [],
            'wednesday': [],
            'thursday': [],
            'friday': []
        }
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

    def add_class(self, day, hour, class_id, teacher_name, subject_name):
        # Add a lesson to the schedule
        # Each method check valid inputs
        verified_hour = self.check_hour(hour)
        verified_class_id = self.check_class_id(class_id)
        verified_teacher_name = self.check_teacher_name(teacher_name)



        self.schedule[day].append({
            'hour': verified_hour,
            'class': verified_class_id,
            'teacher': verified_teacher_name,
            'subject': subject_name
        })

    def display_schedule(self):
        # Display the entire schedule
        for day, lessons in self.schedule.items():
            print(f'{day.capitalize()}:')
            for lesson in lessons:
                print(f"{lesson['hour']}. hour  Class: {lesson['class'].get_id()}, Teacher: {lesson['teacher'].get_first_name()} { lesson['teacher'].get_last_name()}, Subject: {lesson['subject']}")
            print()

# Example usage:

schedule = Schedule()
tt = Teacher("Milada", "Horáková")
c = Class("First floor", 12, "aagg")

# Add some classes to the schedule
schedule.add_class('monday', 4, c, tt, 'Mathematics')
schedule.add_class('monday', 6, c, tt, 'Physics')
schedule.add_class('tuesday', 2, c, tt, 'Chemistry')

# Display the schedule
schedule.display_schedule()


