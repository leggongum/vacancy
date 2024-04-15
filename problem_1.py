'''
1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, 
содержащий только уникальные элементы из исходного списка.
'''

def remove_dublicates(arr: list[int]) -> list[int]:
    #Решение за время O(n), в случае если не важен порядок элементов
    return list(set(arr))


def remove_dublicates_v2(arr: list[int]) -> list[int]:
    #Решение за время O(n), в случае если порядок элементов важен
    new_arr = []
    seen = set()
    for num in arr:
        if num not in seen:
            new_arr.append(num)
            seen.add(num)
    return new_arr
