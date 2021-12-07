year = int(input("enter the year to be determined\n"))
det_1 = year%4
det_2 = year%100
det_3 = year%400
if det_1 != 0:
    print(f"{year} is not a leap year")
elif det_2 !=0:
    print(f"{year} is a leap year")
elif det_3 != 0:
    print(f"{year} is not a leap year")
else:
    print(f"{year} is a leap year")
 