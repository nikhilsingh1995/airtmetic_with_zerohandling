# Assignment1.
# Question:Write Script.Run it.Share .py file for evaluation  and
# write down the result you have got in the description Arithmetic Operations:
#- Should handle divisible by 0 case - Should output decimal whenever required.

#All the basic airthmetic operations in python with example.

n=int(input("Please enter num1:"))
m=int(input("please enter num2 :"))#these two statement take input from the user in variables n & m.Here both values should be integers.

# Addition operator +
a= n+m
print("Addition of given input=",a)

# Subtraction operator -
b=n-m
print("Subtraction of given input=",b)

# Multiplication operator *
c=n*m
print("Multiplication of given input=",float(c))

# Division operator /  that returns float
if m!=0:
    d=n/m
    print("Division of given input=",float(d))
else:
    print("Division of given input=",0)
    
# Modulus operator % that returns remainder
if m!=0:
    e=n%m
    print("modulus of given input=",float(e))
else:
    print("modulus of given input=",0)

# Floor division operator // that returns quotient
if m!=0:
    f=n//m
    print("Floor division of given input=",float(f))
else:
    print("Floor division of given input=",0)
    

# Exponent operator **
g=n**m
print("Exponent of given input=",float(g))

#-------------------------------------------end-----------------------------------------------------------------





