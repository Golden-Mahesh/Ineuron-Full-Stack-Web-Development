x=input("Enter String")
x.strip()
match x:
    case x if ' ' in x:
        print("Multiwords string")
    case x if ' ' not in x:
        print("Single word string")
