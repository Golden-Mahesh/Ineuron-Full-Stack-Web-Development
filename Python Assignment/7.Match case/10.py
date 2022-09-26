x=input("Enter your favorite colour")
match x:
    case x if "yellow" in x:
        print("Monday")
    case x if "blue" in x:
        print("Tuesday")
    case x if "orange" in x:
        print("Wednesday")
    case x if "white" in x:
        print("Thrusday")
    case x if "black" in x:
        print("Friday")
    case x if "red" in x:
        print("Saturday")
    case _:
        print("Sunday")