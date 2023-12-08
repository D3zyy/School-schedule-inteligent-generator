class Rater:
    def __init__(self):
        self.rating = 0
    def get_rating(self):
        return self.rating
    def rate_Positions(self,queue,running,rated_array,l):
        while running.value == True:
            try:
                    #Lock the locker so we do not mess up the queue
                    l.acquire()
                    
                    #Days to check
                    days = ["monday","tuesday","wednesday","thursday","friday"]
                    specific_schedule =  queue.get()
                    
                    for day in days:
                            
                            specific_schedule_day = specific_schedule.get_day_items(day)
                            
                            
                           
                            for lesson in specific_schedule_day:
                                
                                #Mondays rating
                                if day == "monday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        
                                        #1. hodina
                                        case 1:
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 6.5)
                                        #2. hodina
                                        case 2:
                                            specific_schedule.set_rating(specific_schedule.get_rating() + 1)
                                        #3. hodina
                                        case 3:
                                            specific_schedule.set_rating(specific_schedule.get_rating() + 1)
                                        #4. hodina    
                                        case 4:
                                            specific_schedule.set_rating(specific_schedule.get_rating() + 1)
                                        #5. hodina
                                        case 5:
                                            specific_schedule.set_rating(specific_schedule.get_rating() + 1)
                                        #5. hodina
                                        case 6:
                                            specific_schedule.set_rating(specific_schedule.get_rating() + 1)
                                        #7. hodina
                                        case 7:
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 2)
                                        #8. hodina
                                        case 8:
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 5)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 10)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 15)
                                #Tuesdays rating
                                elif day == "tuesday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 6.5)
                                        #2. hodina
                                        case 2:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #3. hodina
                                        case 3:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #4. hodina    
                                        case 4:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 5:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 6:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #7. hodina
                                        case 7:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 2)
                                        #8. hodina
                                        case 8:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 5)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 15)
                                #Tuesdays rating
                                elif day == "wednesday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 5)
                                        #2. hodina
                                        case 2:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #3. hodina
                                        case 3:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #4. hodina    
                                        case 4:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 5:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 6:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #7. hodina
                                        case 7:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 2)
                                        #8. hodina
                                        case 8:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 5)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 15)
                                #Tuesdays rating
                                elif day == "thursday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 5)
                                        #2. hodina
                                        case 2:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #3. hodina
                                        case 3:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #4. hodina    
                                        case 4:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 5:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 6:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #7. hodina
                                        case 7:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 2)
                                        #8. hodina
                                        case 8:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 5)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 15)
                                #Tuesdays rating
                                elif day == "friday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 5)
                                        #2. hodina
                                        case 2:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #3. hodina
                                        case 3:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #4. hodina    
                                        case 4:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 5:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #5. hodina
                                        case 6:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  + 1)
                                        #7. hodina
                                        case 7:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 2)
                                        #8. hodina
                                        case 8:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 20)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 25)
                            
                            print(f"Ohodnoceno na konci : {specific_schedule.get_rating()}") 
                            rated_array.append(specific_schedule)
                            print(len(rated_array))
                           
                                

                            



            finally:
                l.release()
