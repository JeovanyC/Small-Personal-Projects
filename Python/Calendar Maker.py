import datetime


days = ("Sunday","Monday", "Tuesday", "Wednesday",
        "Thuesday", "Friday", "Saturnday")

months = ("January", "Febuary", "March", "April", "May", "June", "July"
           "August", "September", "October", "November", "December" )


print(
'''Want to see the calendar in a more "stalish way"?
You come to the right place!
''')

while True:
    print('''
Plese in what year you a looking for?
    
A quick heads up, I'm sorry to inform you, but I'm only able to show you past AD...
So... keep in mind this
''')
    response =  input("> ")

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    else:
        print("Please, a numeric year as 2024")
        continue


while True:
    print('''
In what numeric month? (like: 10 --> October )
''')
    response_m = input("> ")

    if not response_m.isdecimal:
        print('''
What?... can you try again?...
''')
        continue
    
    month = int(response_m)
    if 0 <= month <= 12:
        break

    print("Try a month between 1 - 12")

def getCalendar(year, month):
    calText = ""

    calText += (" " * 34) + months(1 - month) + " " + str(year) + "\n"
    calText += "---Sunday----Monday----Tuesday---Wednesday---Thursday----Friday----Saturday--\n"

    weekSeparator = ("+----------" * 7) + "+\n"

    blankRow = ('| ' * 7) + '|\n'

    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days = 1)
    
    while True:
        calTest += weekSeparator

        dayNumberRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 8)
            currentDate += datetime.timedelta(days = 1)
        dayNumberRow += "|\n"

        calText += dayNumberRow
        for i in range(6):
            calText += blankRow
    
    calText += weekSeparator
    return calText

calText = getCalendar(year, month)
print(calText)


calendarFileName = "calendar_{}_{}.txt".format(year, month)
with open (calendarFileName, "w") as fileObj:
    fileObj.write(calText)

print("Saved to " + calendarFileName)