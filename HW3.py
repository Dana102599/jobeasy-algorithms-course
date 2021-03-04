#Recursion for fibonacci

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fib(n-2) + fib(n-1)
for n in range(1,10):
 print(n)

#Recursion for factorial

def fact(n):
    if n == 0:
        return 1

    return n * fact(n-1)

n = int(input("Enter a number: "))
print(fact(n))

#Recursion for digital root

def digital_root(n):
 if n<10:
     return n
 n= n%10 + digital_root(n//10)
 return digital_root(n)

n = int(input("Enter a numer: "))
print(digital_root(n))

#* Write a function to check if a number is a Perfect or not

def perfect_number(n):
    sum = 0
    for i in range(2, n):
        if n % i == 0:
            sum += i
    return sum == n

n = int(input(" Please Enter any Number: "))
print(perfect_number(n))




#Amicable numbers from slides
def amicable_numbers(x,y):
    sum1 = 0
    sum2 = 0
    for i in range(1, x):
        if x % i == 0:
            sum1 += i
    for j in range(1, y):
        if y % j == 0:
            sum2 += j
    if(sum1==y and sum2==x):
        return True
    else:
        return False

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(amicable_numbers(x,y))


#Codewars. Credit Card Mask

def maskify(cc):
    if len(cc) < 4:
        return cc
    return "#" * (len(cc)-4) + cc[-4:]

cc = input("Enter CC number")
print(maskify(cc))


