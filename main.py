def input_set():
    # Функція для введення множини користувачем з клавіатури
    elements = input("Введіть елементи множини, розділені пробілами: ")
    return set(map(int, elements.split()))

a = {1, 7, 6, 5, 2}
# a = {10}

b = {2, 1, 7, 8, 3, 4}

def int_to_binary_string(number):
    if number == 0:
        return '0'

    binary_string = ''
    while number > 0:
        remainder = number % 2
        binary_string = str(remainder) + binary_string
        number //= 2

    return binary_string

def set_to_binary_string(input_set):
    elements = list(input_set)     
    
    return ''.join(int_to_binary_string(element) for element in elements)

def union_of_sets(set1, set2):
    return     set1 | set2


# print(set_to_binary_string(a))
print(union_of_sets(a,b))
