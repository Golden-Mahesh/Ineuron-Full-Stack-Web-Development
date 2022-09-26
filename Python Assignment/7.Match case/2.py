print("1. Addition","2.Subtraction","3.Multiplication","4.Division","Enter Choice",sep='\n')
x=int(input())
match x:
    case 1:
        x=int(input("Enter a and b"))
        y=int(input())
        print(x+y)
    case 2:
        x=int(input("Enter a and b"))
        y=int(input())
        print(x+y)
    case 3:
        x=int(input("Enter a and b "))
        y=int(input())
        print(x*y)
    case 4:
        x=int(input("Enter a and b"))
        y=int(input())
        print(x/y)