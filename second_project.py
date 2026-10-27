print("Welcome to  the Pattern Generator and Number Analyzer ")
print(50*"-")
while True:
 print("Select an option:")
 print("1.Generate a Pattern") 
 print("2.Analyze a Range  of Numbers")
 print("3.Exit")
 choice=int(input("Enter your choice:"))
 match choice:
        case 1:
            print("1. Right-angled Triangle")
            print("2. Pyramid")
            print("3. Left-angled Triangle")
            choice_sub=int(input("Enter your choice:"))
            match choice_sub :
                
                case 1:
                    rows_r=int(input("Enter the number of rows:"))
                    for i in range(1,rows_r+1):      # 4   
                
                        for j in range(rows_r-i,0,-1):     # 1
                            print(" ",end="")

                        for k in range(i):
                            print("*",end="")
                        print()
                case 2:
                   rows_p=int(input("Enter the number of level:"))
                   for i in range(1,rows_p+1):
                        for j in range(rows_p-i):
                            print(" ",end="") 
                        
                        for k in range(i):
                            print("*",end=" ")
                        print()
                case 3 :
                    row_l=int(input("Enter the number of rows:"))
                    for i in range(rows_l+1):
                        for j in range(i):
                            print("*",end=" ")
                        print()
                case _ :
                    print("Invalid Input")
            
            
        case 2:
            start=int(input("Enter the start of range:"))
            end=int(input("Enter the end of range:"))
            sum=0
            for i in range(start,end+1):
                if i%2==0:
                    print(f"Nummber {i} is even")
                else:
                    print(f"Number {i} is odd")
                sum=sum+i
            print(f"Sum of the all the numbers from {start} and  {end} : {sum}")


        case 3:
            print("See you again next time")
    
        case _:
            print("Your chices are over")
            break
                    
"""
                *                      *
               * *                   * * 
              * *`*                * * *
             * * * *             * * * *
                               * * * * * 
"""
