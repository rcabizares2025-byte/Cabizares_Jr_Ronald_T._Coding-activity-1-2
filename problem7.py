lst = [3, 4, 5, 6]
input_lst = ["a", "b", "c"]

def print_elements_on_single_line(lst, input_lst):
    print(*lst, sep=" ")
    print(" ".join(input_lst))

print_elements_on_single_line(lst, input_lst)