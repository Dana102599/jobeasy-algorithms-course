#Find the biggest number in the list (divide and rule)
def biggest_nr(list):
    max = list[0]

    for x in list:
        if x > max:
            max = x

    return max

list = [60, 2, 4, 75, 319]
print("Biggest number is:", biggest_nr(list))


