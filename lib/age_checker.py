from datetime import datetime, date
# from dateutil.relativedelta import *

def age_checker(dob):
    """
    function denies underage users access and grants access to users of age
    """
    # parameters - date_of_birth (str - "YYYY-MM-DD")
    # returns a message (str - if underage "access denied", if of age "access granted")
    # side effects - none

    date_of_birth = datetime.strptime(dob, "%Y-%m-%d").date()
    current_day = date.today()
    # delta = relativedelta.relativedelta(current_day, date_of_birth)
    # print(delta)

    age = current_day.year - date_of_birth.year

    if (current_day.month, current_day.day) < (date_of_birth.month, date_of_birth.day):
        age = age - 1
        
    print(age)
