word = "Hello"
numbers = "4567"
mixed = "Hello59"
blank = ""

def contains_only_digits(s):
    return s.isdigit()

print(contains_only_digits(word))    
print(contains_only_digits(numbers))  
print(contains_only_digits(mixed))   
print(contains_only_digits(blank))   