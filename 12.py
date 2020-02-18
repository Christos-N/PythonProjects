import datetime
InputDate = input("Ημερομηνία:")
InputDate = datetime.datetime.strptime(InputDate, "%d/%m/%Y")
CurrentDate = datetime.datetime.now()
if CurrentDate>InputDate:
    d = abs((CurrentDate - InputDate).days) #πόσες μέρες απέχουν
    h = abs((CurrentDate - InputDate).seconds)//3600 #ώρες
    s = int(abs(((CurrentDate - InputDate).seconds)/3600-abs((CurrentDate - InputDate).seconds)//3600)*3600) #δευτερόλεπτα
elif CurrentDate<InputDate:
    d = abs((CurrentDate - InputDate).days)-1
    h = 23-abs((CurrentDate - InputDate).seconds)//3600
    s = 3600-int(abs(((CurrentDate - InputDate).seconds)/3600-abs((CurrentDate - InputDate).seconds)//3600)*3600)
else:
    d = 0
    h = 0
    s = 0
if d == 1 and h == 1 and s == 1:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρα,",h,"ώρα και",s,"δευτερόλεπτο από την τρέχουσα.\n")
elif d == 1 and h == 1:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρα,",h,"ώρα και",s,"δευτερόλεπτα από την τρέχουσα.\n")
elif d == 1 and s == 1:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρα,",h,"ώρες και",s,"δευτερόλεπτο από την τρέχουσα.\n")
elif d == 1:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρα,",h,"ώρες και",s,"δευτερόλεπτα από την τρέχουσα.\n")
elif h == 1 and s == 1:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρες,",h,"ώρα και",s,"δευτερόλεπτο από την τρέχουσα.\n")
elif h == 1:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρες,",h,"ώρα και",s,"δευτερόλεπτα από την τρέχουσα.\n")
elif s == 1:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρες,",h,"ώρες και",s,"δευτερόλεπτο από την τρέχουσα.\n")
else:
    print("Η ημερομηνία που δώσατε απέχει",d,"μέρες,",h,"ώρες και",s,"δευτερόλεπτα από την τρέχουσα.\n")
month = InputDate.month
year = InputDate.year
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("Ο μήνας της ημερομηνίας που δώσατε έχει 31 μέρες.")
elif month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print ("Ο μήνας της ημερομηνίας που δώσατε έχει 29 μέρες.") #leap year
    else:
        print("Ο μήνας της ημερομηνίας που δώσατε έχει 28 μέρες.") #not leap
else:
    print ("Ο μήνας της ημερομηνίας που δώσατε έχει 30 μέρες.")
