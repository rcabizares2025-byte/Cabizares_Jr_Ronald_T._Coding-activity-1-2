Work = "Coding"
Food = "Pizza"
Programming_language = "Python"
Letter = "A"
Blank = ""

def filter_even_indices(text):
    if len(text) <= 1:
        return text
    return text[1::2]

print(filter_even_indices(Work))
print(filter_even_indices(Food))
print(filter_even_indices(Programming_language))
print(filter_even_indices(Letter))

if Blank == "":
    print('""')
else:
    print(filter_even_indices(Blank))