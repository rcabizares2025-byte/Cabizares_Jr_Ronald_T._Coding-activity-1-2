def multiply_list_items(lst, factor):
    return [x * factor for x in lst]

lst = ["a", "b", "c"]
factor = 5

result = multiply_list_items(lst, factor)
print(result)