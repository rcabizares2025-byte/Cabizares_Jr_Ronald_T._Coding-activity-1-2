input_1 = "Hello"
input_2 = "World"
input_3 = "Dog"
input_4 = ""

index_1 = 1
index_2 = 3
index_3 = 15
index_4 = 2

def remove_character_at_index(string, index):
    if string == "":
        return '""'
    elif index < 0 or index >= len(string):
        return string
    else:
        return string[:index] + string[index + 1:]
    
print(remove_character_at_index(input_1, index_1))  
print(remove_character_at_index(input_2, index_2))  
print(remove_character_at_index(input_3, index_3))   
print(remove_character_at_index(input_4, index_4))  