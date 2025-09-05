import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [random.randint(1, 100) for _ in range(100)] #генерируем список из 100 случайных чисел

print('Отсортированный список:', selection_sort(arr))