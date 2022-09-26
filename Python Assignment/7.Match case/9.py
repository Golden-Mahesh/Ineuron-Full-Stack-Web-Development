x=int(input("Enter year"))
match x:
    case x if x%100 and x%4==0:
        print("Non Centuary Leap Year")
    case x if x%100==0 and x%400==0:
        print("Centuary Leap year")
    case x if x%100 and x%4:
        print("Non Century Non leap year")
    case x if x%100==0 and x%400:
        print("Centuray non leap year")