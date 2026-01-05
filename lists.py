# numbers = [1, 0, 10, 22, 11, 15, 19]
# largest_number = numbers[0]
# for number in numbers:
#         if number > largest_number:
#             largest_number = number
# print(largest_number)
numbers =  [1, 3, 9, 0, 3, 3, 5, 9]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)

