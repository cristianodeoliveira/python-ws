def return_middle (x):
    num_char = len(x)
    if (num_char%2 == 0):
        return None
    else:
        return x[(num_char//2)]

print (return_middle('123'))