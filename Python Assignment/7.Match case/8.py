x=input("Enter First string")
y=input("Enter Second String")
match (x,y):
        case (x,y) if x==y:
           print("Identical")
        case (x,y) if x>y:
            print("{} string comes before {}".format(y,x))
        case (x,y) if x<y:
            print("{} string comes before{}".format(x,y))