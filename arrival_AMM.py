#Anthony Miklos
#July 11,2017
#COP2002.C01
#travel calculator


from datetime import datetime, timedelta
import math as m

def main():  
    init_display()    
    choice = "y"
    while choice.lower()== "y":
        dep_date = get_est_dep_date()
        dep_time = get_est_dep_time()
        miles = get_miles()
        mph = get_mph()
        time = get_time(miles,mph)
        hours = get_hour(time)
        minutes = get_minutes(time, hours)
        get_est_arr_datetime(dep_date, dep_time, hours, minutes)
        choice = input("Continue? (y/n): ")
        print()
        
def init_display():    
    print ("Arrival Time Estimator")
    print()

def get_est_arr_datetime(dep_date, dep_time, hours, minutes):
    start_datetime = datetime.combine(dep_date, dep_time.time())
    end_datetime = start_datetime + timedelta(hours=hours, minutes=minutes)
    end_date = end_datetime.date()
    end_time = end_datetime.time()
    print("Estimated date of arrival: ", end_date)
    print("Estimated time of arrival: ", end_time.strftime("%I:%M %p"))
    print()

def get_est_dep_date():
    while True:
        date_str = input("Estimated date of departure (YYYY-MM-DD): ")
        try:
            dep_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try Again.")
            continue
        now = datetime.now()
        if dep_date <= now:
            print ("Departure date must be today or later, try again")
            continue
        else:
            return dep_date

def get_est_dep_time():
    
    while True:
        date_str = input("Estimated time of departure (HH:MM AM/PM): ")
        try:
            dep_time = datetime.strptime(date_str, "%H:%M %p")
        except ValueError:
            print("Invalid time format. Try Again.")
            continue
        return dep_time

def get_miles():
    miles = (input("Enter miles: "))
    return miles

def get_mph():
    mph = (input("Enter miles per hour: "))
    print()
    return mph

def get_time(miles, mph):
    time = int(miles) / int(mph)
    return time

def get_hour(time):
    print ("Estimated Travel Time")
    hours = int(time)
    print ("Hours: " + str(hours))
    return hours

def get_minutes(time, hours):
    minutes = round((time - hours) * 60)
    print ("Minutes: " + str(minutes))
    return minutes


            
if __name__ == "__main__":
    main()

