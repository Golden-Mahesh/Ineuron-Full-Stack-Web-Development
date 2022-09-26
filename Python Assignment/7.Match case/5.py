x=int(input("Enter a Number"))
match x:
    case x if x%2==0:
        print("Saurabh Shukla")
    case x if x<0 and x%2:
        print("Prateek Jain")
    case x if x>0 and x%2:
        print("Aditya Chaudhary")