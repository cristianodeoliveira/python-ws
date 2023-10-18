#This is the main function
def main():
    full_list = ['the mouse', 'some cats', 'a dog', 'people']
    result = find_strings_containing_a(full_list)
    print(result)

def find_strings_containing_a(full_list):
    result_list=[]
    for my_string in full_list:
        for character in my_string:
            if (character.upper() == 'A'):
                result_list.append(my_string)
    return result_list

main()