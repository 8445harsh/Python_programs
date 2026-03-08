AIRTHMETIC OPERATORS:

1.Write a program to add,subtract,multiply and divide two numbers.
a=70
b=7
print("add:",a+b,"subtract:",a-b,"multiply:",a*b,"divide:",a/b)

2.Find the remainder when a numberis divided by 7.
num=87
print("remainder:",num%7)

3.Calculate square and cube of a number using **.
print("square:",8**2)

print("cube:",5**3)

4.Convert total days into years ,months and remaining days usisng airthmetic operators.
TD=756
Y=TD//365
Rd=TD%365
M=Rd//30
Rdays=Rd%30
print("Total days:",TD,"Years:",Y,"Remaining days:",Rd,"Months:",M,
      "Final remaining days:",Rdays)

5.Swap two numbers without using a third variable (use airthmetic operators).
a=45
b=18
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)

6.Find the last digit of a number using%.
num=889
print("last digit of the number:",num%880)

7.Reverse a 3 digit number using airthmeric operators only.
a=867
b=99
print("number:",a,
      "reverse of this number:",a-b)

8.Find the sum of digits of a number using % and//.
num=98765
sum=0

while num>0:
    digit=num%10
    sum+=digit
    num=num//10

    print(sum)
    
RELATIONAL OPERATORs:  

9.Write a program to check if two numbers are equal.
a=789
b=987
print("Is these two numbers are equal:",a==b)

10.Check whether a number is greater than 100.
a=425
print("Is these number is greater than 100:",a>100)

11.Compare two numbers and print the greater one.
a=765
b=975
print("Greater number is:",b, b>a)

12.Check if a number lies between 10 and 50.
num=int(input("Enter a number:"))
print(10<=num<=50)

13.Check whether a number is positive,negative, or zero.
a=int(input("Enter a number:"))
print("Positive:",a>0)
print("Negative:",a<0)
print("Zero:",a==0)

LOGICAL OPERATORS:
    
14.Check whether a number is between 20 and 50.
num=input("enter a number:")
print(20<num and num<50)

15.Check if a student passed (marks≥40) and attendance≥75%.                          
M=int(input("Enter marks:")) 
A=float(input("Enter attendence:")) 
print("Passed:",M>40 and A>75) 

16.Check if a number is divisible by both 3 and 5.
a= int(input("Enter a number:")) 
print(a%3==0 and a%5==0) 

 
17.Check if a number is divisible by 3 or 7.
a= int(input("Enter a number:")) 
print(a%3==0 or a%7==0) 

  
18.Write a program using not to reverse a boolean condition.
a=True 
print(not a)

ASSIGNMENT OPERATORS:


19.Take a number and increase it by 10 using+=. 
a=88
a+=12 
print(a) 


20.Multiply a number by using*=.
a=9
a*=3 
print(a) 

21.Reduce a number by 20 using-=.
a=70
a-=45 
print(a)


22.Square a number using**=
a=9 
a**=6
print(a) 

23. Divide a number by 3 using/=.
a=66 
a/=6
print(a) 

BITWISE OPERATORS:
    
24.Perform bitwise AND on two numbers.  
a=45
b=18
print(a & b) 


25.Perform bitwise OR on two numbers. 
a=75 
b=33
print(a | b) 


26.Perform bitwise XOR on two numbers. 
a=81
b=9
print(a ^ b) 


27.Leftshift a number by 2 positions. 
print(6<<2) 

28.Righrshift a number by 1 position.
print(9>>1) 

29.Find complement of a number by using~.
a=36
print(~a+6) 

30.Check if a number is even using bitwise operator.
a = 256
print("Even:",a%2==0 & a%2==0)

MEMBERSHIP OPERATORS:
    
31.Check whether a number exists in a list.
a= {2,6,9} 
print(2 in a) 

32.Check whether a character exists in a string.
a= "Harsh" 
print("ars" in a) 

33.Check whether a word exists in a sentence.  
a= "Python is a easy language" 
print("easy" in a) 

34.Check whether a key exists in a dictionary.  
d={"key1:11","key266"} 
print("key2:66" in d) 

IDENTIFY OPERATORS:
    
35.Compare two variable using is.
a=467
b=764
print(a is b) 

36.Check if two lists are pointing to the same memory location. 
List1=[4,6,8] 
List2=[4,6,8] 
print(List1 == List2) 

print(List1 is List2) 

37.Create two identical lists and compare using ==and is.
List1=[8,4,5] 
List2=List1 
print(List1 is List2)

38.Explain the difference between is and == using a program.
the == operator checks for value equality, while the is operator
checks for object identity (whether two variables point to the same
object in memory). The program below illustrates this difference
using both mutable and immutable


