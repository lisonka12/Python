from functools import reduce

def my_func(prev_element, element):
    return element * prev_element

print(f'Even numbers: {[element for element in range(99, 1001) if element % 2 == 0]}')
print(f'Multiplication result: {reduce(my_func, [element for element in range(99, 1001) if element % 2 == 0])}')