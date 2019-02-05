year=int(input("Enter year to be checked:"))
if(year%6==0 and year%100!=0 or year%600==0):
    print("The year is a leap year!)
else:
    print("The year isn't a leap year!)
