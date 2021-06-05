
    
#print("1.General arthematic operation\n2.Square root")
 #      d = int(input("Please enter option number"))
  #      if (z == 1):
  #          number = int(input("enter a number: "))
  #          sqrt = number ** 0.5
  #          print("square root:", sqrt)
        


            # Function to add two numbers 
#def add(num1, num2):
 #   return num1 + num2
  
# Function to subtract two numbers 
#def subtract(num1, num2):
 #   return num1 - num2
  
# Function to multiply two numbers
#def multiply(num1, num2):
#    return num1 * num2
  
# Function to divide two numbers
#def divide(num1, num2):
 #   return num1 / num2
 # Python program for simple calculator
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
try:
    while(True):  
        #number_1 = float(input("Enter first number: "))  
        print("Please select operation -\n" \
                "1. Add\n" \
                "2. Subtract\n" \
                "3. Multiply\n" \
                "4. Divide\n" \
                "5. Power/Exponent\n" \
                "6. Square Root calculator\n" \
                "7. Quadratic equation calculator\n")
          
          
        # Take input from the user 
        select = int(input("Select operations form 1, 2, 3, 4, 5, 6, 7 :"))
          

        #number_2 = float(input("Enter second number: "))
          
        if select == 1:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            
            print(number_1, "+", number_2, "=",
                            (number_1 + number_2))
          
        elif select == 2:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            
            print(number_1, "-", number_2, "=",
                            (number_1 - number_2))
          
        elif select == 3:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            
            print(number_1, "*", number_2, "=",
                            (number_1 * number_2))
          
        elif select == 4:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            
            print(number_1, "/", number_2, "=",
                            (number_1 / number_2))
            
        elif select == 5:
            number_1 = float(input("Enter first number: "))
            number_2 = float(input("Enter second number: "))
            
            print(number_1, "^", number_2, "=",
                            (number_1 ** number_2))
            
        elif select == 6:
            number = int(input("enter a number: "))
            sqrt = number ** 0.5
            print("square root:", sqrt)


        elif select == 7:
            a = float(input("enter a"))
            b = float(input("enter b"))
            c = float(input("enter c"))

            dev = (b**2) - 4*a*c

            devs = dev ** 0.5

            x1 = (-b +devs)/(2*a)
            x2 = (-b -devs)/(2*a)

            #print( x1,x2)
            print("First answer is {0}\nSecond answer is {1}\n".format (x1,x2))
            print(type(x1))
            print (type (x2))
            
        else:
            print("Invalid input")      

except:
    pass
            
        
            
        
        

    
   
        
            
           


