class Rater:
    def __init__(self):
        self.rating = 0
    def get_rating(self):
        return self.rating
    def rate_Positionss(self,queue,running,scored_array,l):
        while running.value == True:
            try:
                    #Lock the locker so we do not mess up the queue
                    l.acquire()
                    print(queue.qsize())
                    #Days to check
                    days = ["monday","tuesday","wednesday","thursday","friday"]
                    specific_schedule =  queue.get()
                    
                    for day in days:
                            print(day)
                            specific_schedule_day = specific_schedule.get_day_items(day)
                            print(specific_schedule.get_rating())
                            print(specific_schedule_day)
                           
                            for lesson in specific_schedule_day:
                                
                                #Mondays rating
                                if day == "monday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        
                                        #1. hodina
                                        case 1:
                                            self.rating -= 6.5
                                        #2. hodina
                                        case 2:
                                            self.rating += 1
                                        #3. hodina
                                        case 3:
                                            self.rating += 1
                                        #4. hodina    
                                        case 4:
                                            self.rating += 1
                                        #5. hodina
                                        case 5:
                                            self.rating += 1
                                        #5. hodina
                                        case 6:
                                            self.rating += 1
                                        #7. hodina
                                        case 7:
                                            self.rating -= 2
                                        #8. hodina
                                        case 8:
                                            self.rating -= 5
                                        #9. hodina    
                                        case 9:
                                            self.rating -= 10
                                        #10. hodina
                                        case 10:
                                            self.rating -= 15
                           
                            specific_schedule.set_rating(self.rating)
                            print(f"Ohodnoceno na konci : {specific_schedule.get_rating()}") 
                                

                            



            finally:
                l.release()
    # 1 rating
    def rate_Positions(self,queue,running,scored_array,l):
       print("uplne nahore")
       print(queue.qsize())
       while running.value == True:
         print("tady nahore")
         while queue.qsize() != 0:
            print("tady")
            l.acquire()
            try:
                
                
                    
                days = ["monday","tuesday","wednesday","thursday","friday"]
                    
                
                specific_schedule = queue.get()
                for day in days:
                        
                            
                            print(specific_schedule)
                            formatted_items =  specific_schedule.get_day_items(day)
                            print(formatted_items)
                            for lesson in formatted_items:
                                    
                                #Mondays rating
                                if day == "monday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            self.rating -= 6.5
                                        #2. hodina
                                        case 2:
                                            self.rating += 1
                                        #3. hodina
                                        case 3:
                                            self.rating += 1
                                        #4. hodina    
                                        case 4:
                                            self.rating += 1
                                        #5. hodina
                                        case 5:
                                            self.rating += 1
                                        #5. hodina
                                        case 6:
                                            self.rating += 1
                                        #7. hodina
                                        case 7:
                                            self.rating -= 2
                                        #8. hodina
                                        case 8:
                                            self.rating -= 5
                                        #9. hodina    
                                        case 9:
                                            self.rating -= 10
                                        #10. hodina
                                        case 10:
                                            self.rating -= 15
                                #Tuesdays rating
                                elif day == "tuesday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            self.rating -= 5
                                        #2. hodina
                                        case 2:
                                            self.rating += 1
                                        #3. hodina
                                        case 3:
                                            self.rating += 1
                                        #4. hodina    
                                        case 4:
                                            self.rating += 1
                                        #5. hodina
                                        case 5:
                                            self.rating += 1
                                        #5. hodina
                                        case 6:
                                            self.rating += 1
                                        #7. hodina
                                        case 7:
                                            self.rating -= 2
                                        #8. hodina
                                        case 8:
                                            self.rating -= 5
                                        #9. hodina    
                                        case 9:
                                            self.rating -= 10
                                        #10. hodina
                                        case 10:
                                            self.rating -= 15
                                #Tuesdays rating
                                elif day == "wednesday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            self.rating -= 5
                                        #2. hodina
                                        case 2:
                                            self.rating += 1
                                        #3. hodina
                                        case 3:
                                            self.rating += 1
                                        #4. hodina    
                                        case 4:
                                            self.rating += 1
                                        #5. hodina
                                        case 5:
                                            self.rating += 1
                                        #5. hodina
                                        case 6:
                                            self.rating += 1
                                        #7. hodina
                                        case 7:
                                            self.rating -= 2
                                        #8. hodina
                                        case 8:
                                            self.rating -= 5
                                        #9. hodina    
                                        case 9:
                                            self.rating -= 10
                                        #10. hodina
                                        case 10:
                                            self.rating -= 15
                                #Tuesdays rating
                                elif day == "thursday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            self.rating -= 5
                                        #2. hodina
                                        case 2:
                                            self.rating += 1
                                        #3. hodina
                                        case 3:
                                            self.rating += 1
                                        #4. hodina    
                                        case 4:
                                            self.rating += 1
                                        #5. hodina
                                        case 5:
                                            self.rating += 1
                                        #5. hodina
                                        case 6:
                                            self.rating += 1
                                        #7. hodina
                                        case 7:
                                            self.rating -= 2
                                        #8. hodina
                                        case 8:
                                            self.rating -= 5
                                        #9. hodina    
                                        case 9:
                                            self.rating -= 10
                                        #10. hodina
                                        case 10:
                                            self.rating -= 15
                                #Tuesdays rating
                                elif day == "friday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        #1. hodina
                                        case 1:
                                            self.rating -= 5
                                        #2. hodina
                                        case 2:
                                            self.rating += 1
                                        #3. hodina
                                        case 3:
                                            self.rating += 1
                                        #4. hodina    
                                        case 4:
                                            self.rating += 1
                                        #5. hodina
                                        case 5:
                                            self.rating += 1
                                        #5. hodina
                                        case 6:
                                            self.rating += 1
                                        #7. hodina
                                        case 7:
                                            self.rating -= 2
                                        #8. hodina
                                        case 8:
                                            self.rating -= 10
                                        #9. hodina    
                                        case 9:
                                            self.rating -= 20
                                        #10. hodina
                                        case 10:
                                            self.rating -= 25
                            specific_schedule.set_rating(self.get_rating())
                            print(specific_schedule.get_rating())
                            scored_array.append(specific_schedule)
                            
            finally:
                l.release()
