def leap_year(year):
    if year % 100 == 0:
        leap = year % 400 == 0
    else:
        leap = year % 4 == 0
    return leap
