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
                            
                            subject_dict = {}
                            
                        # 2# Rating if two subjects are next to each other or not and the same subject 3 times in a day two next to each other and one not
                            for lesson in specific_schedule_day:
                                current_subject = lesson['subject']
                                current_hour = lesson['hour']

                                if current_subject in subject_dict:
                                    prev_hour = subject_dict[current_subject]

                                    if current_hour == prev_hour + 1:
                                        specific_schedule.set_rating(specific_schedule.get_rating() + 20)
                                    else:
                                        specific_schedule.set_rating(specific_schedule.get_rating() - 5)
                                    #  same subject 3 times in a day two next to each other and one not
                                    if specific_schedule_day.count(lesson) == 3 and current_hour == prev_hour + 1:
                                        specific_schedule.set_rating(specific_schedule.get_rating() + 15)
                                        print(f'{current_subject} je 3x v jednom dni, 2x za sebou a jednou není zasebou')  
                                    elif specific_schedule_day.count(lesson) > 3:
                                        specific_schedule.set_rating(specific_schedule.get_rating() - 25)
                                else:
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 0)

                                subject_dict[current_subject] = current_hour
                                prev_subject = current_subject

                            # #1 Rating every single position in the schedule and giving it points
                                #Mondays rating
                                if day == "monday":
                                    #Checking whether the hour is occupied or not
                                    #Giving some amount of points if is occupied or not
                                    match lesson['hour']:
                                        
                                        #1. hodina
                                        case 1:
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 8)
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
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 5)
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
                            


                           
                    rated_array.append(specific_schedule)
                           
                    
                                

                            



            finally:
                l.release()



    