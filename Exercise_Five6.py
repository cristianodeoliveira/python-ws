def main():
    a_int = int(input ("Enter a number, any number: "))
    print (square_sum(a_int))

def square_sum (x):
    count = 1
    result = 0
    while (count <= x):
        result = result + count**2
        count +=1
    return result

main()