#EX1. Rewrite code, which will return only needed element of Fib sequence
def fib(n):
      if n == 1:
          return 0
      elif n == 2:
          return 1
      else:
          return fib(n-2) + fib(n-1)

n = int(input("Enter number: "))
print(fib(n))


#EX2.Zeros not for Heroes.

def remove_zeroes(n):
     n = str(n)
     if n == "0":
         return 0
     if n[-1] == "0":
         return remove_zeroes(int(n[:-1]))
     else:
         return n

n = int(input("Enter a number: "))
print(remove_zeroes(n))

#EX3.Digital root is the recursive sum of all the digits in a number.
#Given n,take the sum of the digits of n. If that value has more than one digit,continue
#in this way until a single_digit number is produced.
#This is only applicable to the natural numbers.

def digital_root(n):
     if (n<10):
         return n
     n=n%10+digital_root(n//10)
     return digital_root(n)

n = int(input("Enter number of digits: "))
print(digital_root(n))

#CodeWars.take 2 strings s1 and s2 including only letters from ato z. return a new sorted string,
#the longest possible,containing distinct letters - each taken only once - coming from s1 or s2.
def longest(s1, s2):
     z = s1 + s2
     result = []
     for i in z:
         if i not in result:
             result.append(i)
     result.sort()
     return "".join(result)

s1 = "dtgkggg"
s2 = "rfknoii"
print(longest(s1, s2))

