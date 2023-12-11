class Rater:
    def __init__(self):
        self.rating = 0
    def get_rating(self):
        return self.rating
    def rate_Positions(self,queue,running,rated_array,l,number_of_rated_schedules,best_scored_schedule,better_than_act_schedule):   

    


        while running.value == True:
            try:
                    #Lock the locker so we do not mess up the queue
                    l.acquire()
                    
                    #Days to check
                    days = ["monday","tuesday","wednesday","thursday","friday"]
                    specific_schedule =  queue.get()
                    
                    
                    for day in days:
                            #Loaded a specific day fro the queue
                            specific_schedule_day = specific_schedule.get_day_items(day)
                            
                            

                            count_hour_5_to_8 = 0
                            for lesson in specific_schedule_day:
                                #10. rule if first lesson is Tělocvik + 100 points
                                if lesson["subject"] == "Tělesná výchova" and lesson["hour"] == 1:
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 100)
                                #9. rule if subject is Programové vybavení + 20 points
                                if lesson["subject"] == "Programové vybavení":
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 20)

                                #8. rule if  lesson teaches Mandik + 20 points
                                if lesson["teacher"] == "Mandík":
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 20)


                                #7. rule math cannot be first lesson nor after lunch break and not Profilové předměty
                                if lesson["subject"] == "Matematika" and lesson["hour"] == 1 or lesson["subject"] == "Databázové systémy" and lesson["hour"] == 1 or lesson["subject"] == "Programmové vybavení" and lesson["hour"] == 1 or lesson["subject"] == "Počítačové systémy a sítě" and lesson["hour"] == 1 or lesson["subject"] == "Webové aplikace" and lesson["hour"] == 1 :
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 50)
                                
              

                                #5. rule max lessons 
                                if len(specific_schedule_day) == 10:
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 10000)
                                elif len(specific_schedule_day)  == 9: 
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 3000)
                                elif len(specific_schedule_day)  == 8:
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 200)
                                elif len(specific_schedule_day)  == 7:
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 100)
                                elif len(specific_schedule_day)  < 4:
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 900) 
                                elif  4 <len(specific_schedule_day)  <= 6:
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 500)     
                                #4. rule checking if one of 5-8 hour is  empty for a lunch (grading at the end of whole week)
                                                           
                                if 5 <= lesson["hour"] <= 8:
                                    count_hour_5_to_8 += 1
                                #3. rule checking classes number if you have to change floor or not

                                subject_dict = {}
                                classroom_dict  = {}
                                current_loc = None
                                current_classroom = lesson['class']
                                current_hour = lesson['hour']
                                location = lesson["location"]

                                if current_classroom in classroom_dict:

                                    prev_hour = classroom_dict[current_classroom]
                                    
                                    #Checking if two classes number are equal
                                    if current_hour == prev_hour + 1:
                                        #same classroom 
                                        specific_schedule.set_rating(specific_schedule.get_rating() + 30)
                                    else:
                                       
                                        if current_loc is not None and location != current_loc:
                                         #Different classroom different floor
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 10)
                                        else:
                                            #Same floor different classroom 
                                           specific_schedule.set_rating(specific_schedule.get_rating() - 5)
                                         
                                        
                                    
                                else:
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 0)

                                classroom_dict[current_classroom] = current_hour
                                current_loc = location
                                        



                            #Rule 2. and 6.  Rating if two subjects are next to each other or not and the same subject 3 times in a day two next to each other and one not
                            
                                current_subject = lesson['subject']
                                current_hour = lesson['hour']

                                if current_subject in subject_dict:
                                    prev_hour = subject_dict[current_subject]

                                    if current_hour == prev_hour + 1:
                                        specific_schedule.set_rating(specific_schedule.get_rating() + 10)
                                    else:
                                        specific_schedule.set_rating(specific_schedule.get_rating() - 3)
                                    #  same subject 3 times in a day two next to each other and one not
                                    if specific_schedule_day.count(lesson) == 3 and current_hour == prev_hour + 1 and current_hour != prev_hour - 1:
                                        specific_schedule.set_rating(specific_schedule.get_rating() + 13)
                                       
                                    elif specific_schedule_day.count(lesson) > 3:
                                        specific_schedule.set_rating(specific_schedule.get_rating() - 18)
                                else:
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 0)

                                subject_dict[current_subject] = current_hour
                                

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
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 50)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating() - 10000)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
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
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 50)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
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
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 50)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
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
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 50)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
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
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 50)
                                        #9. hodina    
                                        case 9:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
                                        #10. hodina
                                        case 10:
                                            specific_schedule.set_rating(specific_schedule.get_rating()  - 10000)
                            

                            # Give points for empty hours
                            if count_hour_5_to_8 == 1:
                                    specific_schedule.set_rating(specific_schedule.get_rating() + 10000)
                            elif count_hour_5_to_8 == 2:
                                   specific_schedule.set_rating(specific_schedule.get_rating() - 500)
                            elif count_hour_5_to_8 == 3:
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 10)
                            elif count_hour_5_to_8 == 4:
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 20)
                            elif count_hour_5_to_8 == 0:
                                    specific_schedule.set_rating(specific_schedule.get_rating() - 500)

                    print(f"Hodnocení rozvrhu : {specific_schedule.get_rating()}")
                    print(f"Zatím nejlepší hodnocení rozvrhu : {best_scored_schedule.value}")
                    if specific_schedule.get_rating() >= best_scored_schedule.value:   
                        specific_schedule.set_rating(specific_schedule.get_rating())
                        rated_array.append(specific_schedule)
                        best_scored_schedule.value = specific_schedule.get_rating() 
                    if  specific_schedule.get_rating() > -2403:
                        better_than_act_schedule.value += 1
                    del specific_schedule
                    number_of_rated_schedules.value += 1
                    print(f"Rozvrhů ohodnoceno : {number_of_rated_schedules.value}")
                    
                                

                            



            finally:
                l.release()