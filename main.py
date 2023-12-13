def input_set():
    # Функція для введення множини користувачем з клавіатури
    elements = input("Введіть елементи множини, розділені пробілами: ")
    return set(map(int, elements.split()))

U = {1, 2, 3, 4, 5, 6, 7, 8} 
#множини з четвертого варіанту
a = {1, 2, 5, 3, 7}
b = {4, 7, 3, 1, 6, 2}
#ручний ввід множин
# a = input_set()
# b = input_set()


def union_of_sets(set1, set2):
    return     set1 | set2

def intersection_of_sets(set1, set2):
    return set1 & set2

def set_difference(set1, set2):
    return  set1 - set2

def set_complement(set):
    return U - set

def symmetric_difference_of_sets(set1, set2):
    return set1 ^ set2

def cartesian_product(set1, set2):
    result_set = {(a, b) for a in set1 for b in set2}
    return result_set

def are_sets_equal(set1, set2):
    return set1 == set2

def is_subset(set1, set2):
    return all(element in set2 for element in set1)

def convert_to_bitstring(set):
    result_array = [1 if elem in set else 0 for elem in U]

    return result_array

def convert_to_plural(bitstring):
    result_set = {index + 1 for index, value in enumerate(bitstring) if value}
    return result_set


def plural_OR(set1, set2):
    array1 = convert_to_bitstring(set1)
    array2 = convert_to_bitstring(set2)
    result_array = [1 if a | b  else 0 for a, b in zip(array1, array2)]
    return convert_to_plural(result_array)

def plural_AND(set1, set2):
    array1 = convert_to_bitstring(set1)
    array2 = convert_to_bitstring(set2)
    result_array = [1 if a & b  else 0 for a, b in zip(array1, array2)]
    return convert_to_plural(result_array)

def plural_XOR(set1, set2):
    array1 = convert_to_bitstring(set1)
    array2 = convert_to_bitstring(set2)
    result_array = [1 if a ^ b  else 0 for a, b in zip(array1, array2)]
    return convert_to_plural(result_array)

def plural_NOT(set):
    array = convert_to_bitstring(set)
    result_array = [0 if a else 1 for a in array]
    return convert_to_plural(result_array)

# print(intersection_of_sets(a,b))
# print(set_complement(a,b))
# print(symmetric_difference_of_sets(a, b))
# print(cartesian_product(a, b))
# print(set_complement(a))


# print(plural_AND(a, b))
# print(plural_OR(a, b))
# print(plural_XOR(a, b))