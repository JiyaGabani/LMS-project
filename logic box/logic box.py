# Logic Box

while True:
    print("welcome to the pattern Genrator and Numbers analyzer!")

    print("1. Genrate a pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
         while True:
             print("Choose a pattern typr: ")
             print("1. Right-angle Triangle")
             print("2. Pyramid")
             print("3. Left-angle triangle")

             pattern_choice = input("Enter your choice: ")

             rows = int(input("Enter the number of rows for the pattern: "))

             print("\n pattern:")

             if pattern_choice == "1":

                 # Right-angle Triangle

                 for i in range(1, rows + 1):
                     print("*" * i)

                    elif pattern_choice == "2":

                        #Pyramid
                        for i in range(1, rows + 1):
                            print(" " * (rows-i) , end=" ")

                            print("*" * (2 * i - 1)):

                    elif patter_choice == "3":

                        # Left-angle Triangle
                         for i in range(1, rows + 1):
                             print("  " * (rows-i) + "*" * i)

               elif choice =="2":

                       strat = int(input("Enter start number: "))
                       end = int(input("Enter end number: "))

                      total = 0
                      print()

                      for num in range(start, end+1):
                          if num%2==0:
                              print(num, "is even")
                        else:
                            primt(num, "is odd")

                        total = total + num

                    print("\n sum = " , total)
                    
            elif chioce == "3":
                print("program end")
            else:
                print("invalid choice")
            
                          

               
