#Цель: вывести числа с уникальными значениями
# 1, 1, 2, 2, 3, 4, 5, 5, 6, 6 -> 1, 2, 3, 4, 5, 6,

def unique(numbers): 
    if numbers is None or len(numbers) < 1:
        return []
    unique_values = list()
    for number in numbers: 
        if numbers.count(number) < 2: 
            unique_values.append(number)
        elif not unique_values.count(number):
            unique_values.append(number)
    return unique_values


def unique(numbers): 
    if numbers is None or len(numbers) < 1:
        return []
    elif len(numbers) == 1:
        return numbers
    return list(set(numbers))

exaple_1 = [1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 7, 8, 9]
exaple_2 = [1]
exaple_3 = []
print(unique(exaple_1))
print(unique(exaple_2))
print(unique(exaple_3))
