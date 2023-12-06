import multiprocessing 
#Module to check whether program is still running
still_running = multiprocessing.Value('b',True)

def get_still_running():
      return still_running
