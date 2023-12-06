import time


class WatchDog:
    def __init__(self,timeout):
        if  isinstance(timeout,int) and 0 < timeout < 600:
            self.time_out = timeout
        else:
            raise ValueError("Wrong input")
    def activete_Timer(self):
        start_time = time.time()
        while time.time() - start_time < 3:
            print()
        return False
    def set_timeout(self,value):
        if  isinstance(value,int) and 0 < value < 600:
            self.time_out = value
        else:
            raise ValueError("Wrong input")

    