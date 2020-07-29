
#this method gets the index for what day of the week January 1 is of a given year
#this method utilizes year %7 to identify the days of the week
#there is an offset value to the index when a leap year is encountered
def getJanOne(year):

    #array to access days of the week
    days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday']
    
    #starting year of algorithm
    baseYear = 2024

    #the method considers leap years
    leapYear = year
    
    #if the year is not a leap year
    if year % 4 != 0:

        #statement gets the next leap year relative to the original year passed
        leapYear = year + (4-(year%4))
    
    #offset is the value that is added or subtracted from index due to leap years from baseyear
    if year < baseYear:
        offset = int((baseYear - leapYear)/4)
        dayIndex = (year %7) - offset
    else:
        offset = int((leapYear - baseYear)/4)
        dayIndex = (year %7) + offset
    
    if dayIndex < 0:
        dayIndex = 7 + dayIndex
    
    return days[dayIndex]

#method has limited range, needs to be improved

print(getJanOne(int(input("Input year: "))))