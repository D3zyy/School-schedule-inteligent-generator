
class Teacher:
    def __init__(self, first_name, last_name):
            try:
                self.first_name = self.check_validity(first_name)
                self.last_name = self.check_validity(last_name)
            except ValueError as e:
                print(e)
            except:
                 print("An Error occured")

        

    # first_name getter
    def get_first_name(self):
            return self.first_name
        
        

    # first_name setter
    def set_first_name(self, value):
        self.first_name = self.check_validity(value)
        

    # last_name getter
    def get_last_name(self):
            return self.last_name
        

    # last_name setter
    def set_last_name(self, value):
        self.last_name = self.check_validity(value)
        

    # Func that checks validity of inputs
    def check_validity(self,value):

       if type(value) == str and 3 < len(value) < 15:
            return value
       else:
            raise ValueError(f"It has an inappropriative style.")






    


