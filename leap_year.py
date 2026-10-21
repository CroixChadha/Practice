def is_leap_year(year):
    # Write your code here.    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

    

    # Don't change the function name.

is_leap_year(1700)
