'''
4. Написать программу, которая сортирует список строк по длине, 
сначала по возрастанию, а затем по убыванию.
'''

def sort_by_length(arr: list[str]) -> tuple[list[str]]:
    sorted_arr = arr.sort(key=lambda x: len(x))
    return sorted_arr, sorted_arr[::-1]