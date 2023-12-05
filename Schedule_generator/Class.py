class Class:
    ids = []
    
    def __init__(self,location,id,note = None):
        # Checking if id is unique and higher than 0
        if isinstance(id, int) and  id not in Class.ids and id > 0:
            self.id = id
            self.ids.append(id)
        else:
            print("nevyhovuje")
        if note is not None:
         self.note = self.check_validity(note)
        self.location = self.check_validity(location)

    def get_location(self):
        return self.location
    def set_location(self,value):
        if len(str(value)) < 25 and len(str(value)) > 3 and type(value) ==  str:
            self.location = value
        else:
            raise ValueError(f"{value} is not appropriate")
    def get_id(self):
        return self.id
    def set_id(self,value):
        # Setter for an id, check whether id is already in use or is negative
        if isinstance(value, int) and  value not in self.ids and value > 0:
            self.id = value
        else:
            raise ValueError(f"{value} was not set because it is already in use or is negative!")
    def get_note(self):
        return self.note
    def set_note(self,value):
        # Check whether note has appropriate style
        if len(str(value)) < 25 and len(str(value)) > 3 and type(value) ==  str:
            self.note = value
        else:
            raise ValueError(f"{value} is not appropriate")
        # Func that checks validity of inputs
    def check_validity(self,value):
       if type(value) == str and 3 < len(value) < 15:
            return value
       else:
            raise ValueError(f"It has an inappropriative style.")


