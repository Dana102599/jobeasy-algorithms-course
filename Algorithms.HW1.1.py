#Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where User enter n manually. n > 0


def getSum(n):
    sum = 0


    while (n > 0):
        sum += int(n % 10)
        n = int(n / 10)

    return sum

n = int(input('Input a number'))
print(getSum(n))


#Find max number from 3 values, entered manually from a keyboard
# method a
max_number = input("Input 3 numbers")

print(max(max_number))
# method b

def max_mum(x, y, z):
    if (x >= y) and (x >= z):
        largest = x

    elif (y >= x) and (y >= z):
        largest = y
    else:
        largest = z

    return largest

x = input("Input number")
y = input("Input number")
z = input("Input number")
print(max(x, y, z))



#Count odd and even numbers.  Count odd and even digits of the whole number.


def countEvenOdd(n):
    even_count = 0
    odd_count = 0
    while (n > 0):
        rem = n % 10
        if (rem % 2 == 0):
            even_count += 1
        else:
            odd_count += 1

        n = int(n / 10)

    print("Even count : ", even_count)
    print("Odd count : ", odd_count)


n = int(input('Input number'))
a = countEvenOdd(n);



