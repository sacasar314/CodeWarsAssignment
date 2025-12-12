# Solution: Even or Odd number
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
# Solution: Convert a number to a string
def number_to_string(num):
    return str(num)

# Solution: Remove spaces from a string
def no_space(x):
    return x.replace(" ", "")

# Solution: Count the number of vowels in a string
# Input string will only consist of lower case letters and/or spaces
def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count