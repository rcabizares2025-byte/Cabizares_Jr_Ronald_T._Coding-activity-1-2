def count_elements_greater_than_three(numbers):
    count = 0
    for number in numbers:
        if number > 3:
            count += 1
    return count

numbers = []
print(count_elements_greater_than_three(numbers))