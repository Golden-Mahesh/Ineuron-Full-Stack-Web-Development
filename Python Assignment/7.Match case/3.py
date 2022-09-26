print("1.Check Isosceles Triangle","2.Check Right Angle Triangle","3.Equilateral Triangle","4.Exit",sep='\n')
a=1
while a:
    a=int(input("Enter Your choice"))
    match a:
      case 1:
         x=int(input("Enter Three sides"))
         y=int(input())
         z=int(input())
         if x*x==y*y+z*z or y*y==x*x+z*z or z*z==x*x+y*y:
           print("The Given Triangle is Right Angle Triangle")
         else:
          print("The Given Triangle is not Right Angle Triangle")
       
      case 2:
         x=int(input("Enter Three sides"))
         y=int(input())
         z=int(input())
         if x==y or x==z or y==z:
            print("The Given Triangle is Isosceles ")
         else:
            print("The Given Triangle is not Isosceles")
      case 3:
         x=int(input("Enter Three sides"))
         y=int(input())
         z=int(input())
         if x==y and y==z:
            print("The Given Triangle is Equilateral Triangle")
         else:
            print("The Given Triangle is not Equailateral Triangle")
      case 4:
        exit()
      case _:
        print("Invalic choice")