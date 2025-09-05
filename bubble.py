import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [random.randint(1, 100) for _ in range(100)] #генерируем список из 100 случайных чисел

print('Отсортированный список:', bubble_sort(arr))