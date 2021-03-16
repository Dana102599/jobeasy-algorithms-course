
#EX1.When given a list, the program should return a list of all the elements
# that are below the arithmetical mean of the original list.
# The arithmetical mean is the sum of all elements divided by the number of elements.

def all_elements(list):
    return [x for x in list if x <sum(list) / len(list)]

list = [5, 78, 2, 9, 6]
print(all_elements(list))

#EX2,When given a list of elements find the two lowest elements.
# They can be equal to each other or different.

def two_lowest(list1):
    lowest = list1[1]
    lowest2 = [0]
    for item in list1[1:]:
        if item < lowest:
            lowest2 = lowest
            lowest = item
        elif lowest2 == [0] or lowest2 > item:
            lowest2 = item


    print("Smallest element is:", lowest)
    print("Second Smallest element is:", lowest2)

list1 = [11, 32, 4, 41, 51, 2, 9, 67, 4]
two_lowest(list1)

# def second_minimum(arr):
#     second = arr[1]
#     first = arr[0]
#
#     for n in arr:
#         if n < first:
#             first = n
#         if n > first and n < second:
#             second = n
#
#     return second
#
# arr = [9, 3, 89,]
# print(second_minimum(arr))




















