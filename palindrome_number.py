def int_to_string(int):
    # converts an integer into a string
    converted_num = str(int)
    return converted_num

def reverse_string(string):
    # reverses a string
    return string[::-1]

def is_num_palindrome(num):
    # checks if a number is a palindrome

    # turns the number into a string
    num_as_string = int_to_string(num)

    # reverses the number after it has been turned into a string
    reversed_num_as_string = reverse_string(num_as_string)

    # checks if the original number and the reverse are the same    
    if num_as_string == reversed_num_as_string:
        return True
    else:
        return False
