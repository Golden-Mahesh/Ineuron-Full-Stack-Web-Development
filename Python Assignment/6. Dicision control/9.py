x=int(input("Enter year"))
if x%100==0:
    if x%400==0:
        print("Lear year")
    else:
        print("Not a Lear year")
else :
    if x%4==0:
        print("Lear year")
    else:
        print("Not a Leap year")