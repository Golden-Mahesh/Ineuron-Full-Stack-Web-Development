x=int(input("Enrer month Number"))
match x:
    case x if x in(1,3,5,7,8,10,12):
        print("31")
    case x if x in (4,6,9,11):
        print("30")
    case 2:
        print("28")
    case _:
        print("Invalid Month Number")