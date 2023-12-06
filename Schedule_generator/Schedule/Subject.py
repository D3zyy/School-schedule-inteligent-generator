class Subject:
    def __init__(self,name):
        self.name = self.check_validity(name)

    def get_name(self):
        return self.name
    def set_name(self,value):
        self.value = self.check_validity(value)
        

    #Validator for inputs
    def check_validity(self,value):

       if type(value) == str and 4 < len(value) < 35:
            return value
       else:
            raise ValueError(f"It has an inappropriative style.")
    
        