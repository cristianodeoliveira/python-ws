def mutipleof (num):
    my_mult = [3,5,7,11,13,17]
    index = 0
    msg = ''
    while index < len(my_mult):
        result = num%my_mult [index]
        if (result == 0 and index == 0): # Multiple of 3
            msg = 'Buzz'
        if (result == 0 and index == 1): # Multiple of 5
            msg = msg + 'Bizz'
        if (result == 0 and index == 2): # Multiple of 7
            msg = msg + 'Bang'
        if (result == 0 and index == 3): # Multiple of 11
            msg = msg + 'Bong'
        if (result == 0 and index == 4): # Multiple of 13
            msg = msg + 'Fezz'
        if (result == 0 and index == 5): # Multiple of 17
            msg = msg + 'Fizz'
#        if (result != 0 and len(msg) > 0):
#            return 1
        index = index + 1
    return msg

counter = 0
# This is a comment
my_numbers_list = []
my_numbers = int(input ("How many numbers? "))
index = 0
# Build the list of numbers, in this
while index < my_numbers:
    my_numbers_list.append (index + 1)
    index = index + 1
index = 0
while index < my_numbers:
    msg = mutipleof (my_numbers_list[index])
    index = index + 1
    if len(msg) > 0:
        print (msg)
    else:
        print (index)