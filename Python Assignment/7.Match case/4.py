x=int(input("Enter your age"))
match x:
    case x if x<10:
        print("Kid")
    case x if x<20:
        print("Teen")
    case x if x<40:
        print("young")
    case x if x<60:
        print("Experienced")
    case x if x>60:
        print("Senior Citizen")