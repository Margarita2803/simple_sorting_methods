import time
import random
import matplotlib.pyplot as plt

# 1. Сортировка пузырьком
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

# 2. Сортировка выбором
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# 3. Сортировка вставками (для сравнения)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Функция замера времени сортировки
def measure_time(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr)
    end = time.perf_counter()
    return end - start

# Основной код измерения и построения графика
sizes = [100, 200, 400, 800, 1600]

times_bubble = []
times_selection = []
times_insertion = []

for size in sizes:
    test_list = [random.randint(0, 10000) for _ in range(size)]
    times_bubble.append(measure_time(bubble_sort, test_list))
    times_selection.append(measure_time(selection_sort, test_list))
    times_insertion.append(measure_time(insertion_sort, test_list))

plt.plot(sizes, times_bubble, label='Пузырьковая сортировка')
plt.plot(sizes, times_selection, label='Сортировка выбором')
plt.plot(sizes, times_insertion, label='Сортировка вставками')
plt.xlabel('Размер списка')
plt.ylabel('Время выполнения (сек)')
plt.title('Сравнение времени выполнения алгоритмов сортировки')
plt.legend()
plt.grid(True)
plt.show()