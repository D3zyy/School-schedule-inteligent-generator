import time


class WatchDog:
    def __init__(self,timeout):
        if  isinstance(timeout,int) and 0 < timeout <= 6000:
            self.time_out = timeout
        else:
            raise ValueError("Wrong input (must be an intiger between 0 - 1000 second)")
    def activate_Timer(self,run):
        start_time = time.time()
        
        while time.time() - start_time < self.time_out:
            pass
        run.value = False
    def set_timeout(self,value):
        if  isinstance(value,int) and 0 < value <= 6000:
            self.time_out = value
        else:
            raise ValueError("Wrong input (must be an intiger between 0 - 1000 second)")
    def get_time(self):
        return self.time_out

    