import random
from random import randint

arr1 = [randint(0, 100000) for _ in range(10)]
arr2 = [randint(0, 100000) for _ in range(10)]
print(arr1)
print()
print(arr2)
print()

array_with_min_max_elements = []

#список, содержащий элементы обоих списков
for joined_list in arr1, arr2:
    joined_list = arr1 + arr2
    
#щас понял, что можно было проще: array_with_arr1_arr2 = arr1 + arr2
    
    
print(joined_list)
print()

#список, содержащий элементы обоих списков без повторений
for joined_list in arr1, arr2:
    joined_list = arr1 + arr2
    joined_list_without_repeat = list(set(joined_list))
    
print(joined_list_without_repeat)
print()

#список, содержащий элементы общие для двух списков
array_with_general_elements = list(set(arr1).intersection(arr2))
print(array_with_general_elements)
print()

#список, содержащий только уникальные элементы каждого из списков
#может быть я не до конца понял, но это самое что и общие элементы из двух списков

#список, содержащий только минимальное и максимальное значение каждого из списков
for max_min_elements in arr1, arr2:
    max_element_in_arr1 = max(arr1)
    min_element_in_arr1 = min(arr1)
    
    max_element_in_arr2 = max(arr2)
    min_element_in_arr2 = min(arr2)
    
    max_min_elements = (
        f"Максимальное значение первого массива:{max_element_in_arr1} Максимальное значение второго массива:{max_element_in_arr2}"
        f" Минимальное значение первого массива:{min_element_in_arr1} Минимальное значение второго массива:{min_element_in_arr2}"
    )
    
print(max_min_elements)