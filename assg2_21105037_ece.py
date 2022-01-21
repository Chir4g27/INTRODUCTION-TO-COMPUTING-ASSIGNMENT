#question number 1


   
input_str = input("Enter the string : ")                                                                #Taking input from user
print("The length of the given string is : %s" % len(input_str))                                        #Printing the length of the string
reversed_str = input_str[ : : -1 ]                                                                      #Creating reversed string
print("The string in reverse would be : %s" % reversed_str)
new_str = input_str[10:26]                                                                              #Creating a new string              
print("The new string becomes : %s" % new_str)
new_str = "object oriented"                                                                             #Replacing the value
print("The replaced substring will be : %s" % new_str)
substr = "a"
indx = input_str.find(substr)                                                                           #Finding the index value of the given substring
if indx == -1:
    print("The given substring was not found in the inputted string")
else:
    print("The first occurence of the given substring \"%s\" is at index no. = %d" % (substr, indx))    #Printing the index value
no_white_spaces_str=input_str.replace(" ","")                                                           #Removing white spaces
print("The inputted strings with no white spaces will be \"%s\"\n" % no_white_spaces_str)



#question number 2

name = input("Enter your name : ")
sid = int(input("Enter your SID : "))
dept_name = input("Enter the name of your department : ").upper()
cgpa=float(input("Enter your CGPA : "))
#output
print("\nHey, \033 %s\033m Here!\nMy SID is \033 %d\033 \nI am from \033 %s\033 department and my CGPA is \033 %0.1f \033 \n" % (name, sid, dept_name, cgpa))

#question number 3


a=56
b=10
print("a & b=", (a & b))
print("a | b=", (a | b))
print("a ^ b=", (a ^ b))
print("Left shift both a and b with 2 bits : a=",a<<2, "b=", b<<2)
print("Right shift a with 2 bits and b with 4 bits : a=", a>>2, "b=", b>>4)


#question number 4



first_number = int(input("Enter first number : "))
second_number = int(input("Enter second number : "))
third_number = int(input("Enter third number : "))
if first_number >= second_number:
    if first_number >= third_number:
        print("The greatest number is %s\n" % first_number)
    else:
        print("The greatest number is %s\n" % third_number)
else:
    if second_number >= third_number:
        print("The greatest number is %s\n" % second_number)
    else:
        print("The greatest number is %s\n" % third_number)


#question number 5

if "name" in input("Enter the string : "):
    print("Yes\n")
else:
    print("No\n")


#question number 6


while True:
    sides = sorted(input("Enter the dimensions to check whether triangle possible or not : ").split())  #Sorting the inputted values in a list
    if len(sides) == 3:                                                                                 #Making sure only 3 values are entered
        break
    else:
        print("\nA triangle has only 3 sides!\nPlease enter only 3 values")
if int(sides[2]) > (int(sides[0]) + int(sides[1])):
    print("No\n")
else:
    print("Yes\n")
