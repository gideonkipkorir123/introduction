# numbers=[1,1,2,2,2,3,3,4,4,5,5,6,6]
# unique_numbers=list(set(numbers))
# print(unique_numbers)
numbers = [20, 20, 30, 30, 40]


def get_unique_numbers(numbers):
    unique = []

    for number in numbers:
        if number in unique:
            continue
        else:
            unique.append(number)
    return unique


print(get_unique_numbers(numbers))
# Result: [20, 30, 40]