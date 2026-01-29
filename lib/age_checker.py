from datetime import datetime, date

def age_checker(dob):
    try:
        date_of_birth = datetime.strptime(dob, "%Y-%m-%d").date()
    except:
        raise Exception("invalid date format")

    current_day = date.today()
    age = current_day.year - date_of_birth.year
    if (current_day.month, current_day.day) < (date_of_birth.month, date_of_birth.day):
        age = age - 1
    
    if age < 16:
        return "access denied"
    else:
        return "access granted"