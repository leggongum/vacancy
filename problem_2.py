'''
2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) 
и возвращает список всех простых чисел в заданном диапазоне.
'''

def sieve(start, end) -> list[int]:
    # Решение через решето Эратосфена за время O(n log n) и дополнительную память O(n)
    arr = [True] * (end + 1)
    arr[0] = arr[1] = False
    for i in range(2, int(end ** .5)):
        if arr[i]:
            for j in range(i + i, end+1, i):
                arr[j] = False
    return [num for num in range(start, end+1) if arr[num]]
