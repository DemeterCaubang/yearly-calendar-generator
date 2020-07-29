#this method returns values for a monthly caledar
#this method utilizes arrays to display days for each day
class calendarMonth:
    def __init__(self, year, month, lastday):
        self.monthDict = {'Jan':31, 'Feb':28, 'Mar':31, 'Apr':30, 'May': 31, 'Jun':30, 'Jul':31, 'Aug':31,'Sep':30, 'Oct':31, 'Nov':30, 'Dec':31}
        
        #days of the week
        self.days = {'Sun':[], 'Mon':[], 'Tue':[], 'Wed':[], 'Thu':[], 'Fri':[], 'Sat':[]}
        
        #first day provides index for the first row of values that are not 1
        self.firstDay = lastday + 1
        if self.firstDay == 7:
            self.firstDay = 0
        self.month = month
        self.lastDay = 0

        #if the calendar is a leap year
        if year % 4 == 0:
            self.monthDict['Feb'] = 29

    def calendarMatrix(self):
        
        #loop that increments values for calendar days
        for i in range(35):

            #statement that denotes empty cells in calendar
            if i < self.firstDay or day > self.monthDict[self.month]:
                day = 0
            if i %7 == 0 or i == 0:
                self.days['Sun'].append(day)
            elif i %7 == 1 or i == 1:
                self.days['Mon'].append(day)
            elif i %7 == 2 or i == 2:
                self.days['Tue'].append(day)
            elif i %7 == 3 or i == 3:
                self.days['Wed'].append(day)
            elif i %7 == 4 or i == 4:
                self.days['Thu'].append(day)
            elif i %7 == 5 or i == 5:
                self.days['Fri'].append(day)
            elif i %7 == 6 or i == 6:
                self.days['Sat'].append(day)

            #statement gets the day of the week of the last day of the calendar month 
            if day == self.monthDict[self.month]:
                self.lastDay = i%7

            day += 1

    #method to get the day of the week for the last day of the calendar month
    def getLastDay(self):
        return self.lastDay

#test code
c = calendarMonth('Jul', 2)
c.calendarMatrix()
print(c.days['Sun'])
print(c.days['Mon'])
print(c.days['Tue'])
print(c.days['Wed'])
print(c.days['Thu'])
print(c.days['Fri'])
print(c.days['Sat'])
print(c.getLastDay())
