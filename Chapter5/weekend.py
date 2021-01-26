import datetime

weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

now = datetime.date.today()

dayOfWeek = now.weekday()

today = weekDays[dayOfWeek]

daysToWeekend = 6-dayOfWeek
print("There are ", daysToWeekend-1, " days until the weekend.")

quotePrinted = "false"

for left in weekDays[dayOfWeek:daysToWeekend]:
    if today == "Sunday" and quotePrinted == "false":
            print(left, " Sundays are my favorite")
            quotePrinted = "true"
    elif (today == "Monday" or today == "Tuesday" or today == "Wednesday") and quotePrinted == "false":
        print(left, " Another great week ahead!")
        quotePrinted = "true"
    elif today == "Thursday" and quotePrinted == "false":
        print(left, " Nearly the weekend!")
        quotePrinted = "true"
    elif quotePrinted == "false":
        print(left, " The weekend has started!")
        quotePrinted = "true"
    else:
        print(left)