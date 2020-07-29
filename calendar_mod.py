#main calendar class
#unfinished and erroneous
class Calendar:
    def __init__(self, year):
        self.months=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug','Sep', 'Oct', 'Nov', 'Dec']
        self.year = year
        self.calendar = {}
        
    # derrived from getJanOne()
    def getFirstDay(self, monthIndex):
        if self.months[monthIndex] == 'Jan':
            baseYear = 2024
            leapYear = self.year
            
            if self.year % 4 != 0:
                leapYear = self.year + (4-(self.year%4))
            
            if self.year < baseYear:
                offset = int((baseYear - leapYear)/4)
                dayIndex = (self.year %7) - offset
            else:
                offset = int((leapYear - baseYear)/4)
                dayIndex = (self.year %7) + offset
            
            if dayIndex < 0:
                dayIndex = 7 + dayIndex
            
            return dayIndex - 1
        
        else:
            return self.calendar[self.months[monthIndex-1]].getLastDay()

    #method for generating whole calendar
    def finalCalender(self):
        for i in range(12):
            self.calendar[self.months[i]] = calendarMonth(year, self.months[i], getFirstDay(i))
        return self.calendar

c = Calendar(2020)

print(c.calendar)