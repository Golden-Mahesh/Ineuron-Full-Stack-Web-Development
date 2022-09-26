x=int(input("Enter a number"))
match x:
    case  x if x>0:
        print("Positive")
    case x if x<0:
        print("Negative")
    case x:
        print("Zero")