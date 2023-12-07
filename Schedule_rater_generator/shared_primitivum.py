import multiprocessing 

#Variable to check whether program is still running through the whole project
still_running = multiprocessing.Value('b',True)

def get_still_running():
      return still_running

