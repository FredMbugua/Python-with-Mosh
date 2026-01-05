# phone = int(input('Phone: '))
# numbers = {
#     1 : 'One',
#     2 : 'Two',
#     3 : 'Three',
#     4 : 'Four'
# }
# i = 1
# for number in numbers:
#     print(f'{numbers[i]}')
#     i += 1
phone = input('Phone: ')
numbers = {
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four'
}
output = ""
for number in phone:
    output +=  numbers.get(number, "!") + " "
print(output)