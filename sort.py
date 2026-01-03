import random

def generate_random_count(from_count, to_count):
    random_number = random.randint(from_count, to_count)
    return random_number

def generate_random_list(min_count, max_count, list_length):
    arr = [generate_random_count(min_count, max_count) for i in range(list_length)]
    return arr

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    arr_length = len(arr)
    for i in range(arr_length):
        min_idx = i
        for j in range(i + 1, arr_length):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return arr, comparisons, swaps


def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(0, arr_length - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, comparisons, swaps


def insertion_sort(arr):
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                swaps += 1
                j -= 1
            else:
                break
        arr[j + 1] = key

    return arr, comparisons, swaps


def draw_table(selection_comparisons, bubble_comparisons, insertion_comparisons,selection_swaps, bubble_swaps, insertion_swaps):
    print()
    header = f"{'Метод сортировки':<20} | "f"{'Сравнений':<12} | "f"{'Перестановок':<15}"
    separator = '-' * len(header)
    print(separator)
    print(header)
    print(separator)


    print(f"{'Selection Sort':<20} | "f"{selection_comparisons:<12} | "f"{selection_swaps:<15}")
    print(f"{'Bubble Sort':<20} | "f"{bubble_comparisons:<12} | "f"{bubble_swaps:<15}")
    print(f"{'Insertion Sort':<20} | " f"{insertion_comparisons:<12} | "f"{insertion_swaps:<15}")

    print(separator)
    print()


def demo_mode():
    print("введите длинну массива")
    input_line = input()
    if input_line.isdigit():
        arr_length = int(input_line)

        arr = generate_random_list(0, 99,arr_length)
        print("созданный массив:")
        print(*arr)
        selection_arr,selection_comparisons,selection_swaps = selection_sort(arr.copy())
        bubble_arr,bubble_comparisons,bubble_swaps = bubble_sort(arr.copy())
        insertion_arr,insertion_comparisons,insertion_swaps = insertion_sort(arr.copy())


        draw_table(selection_comparisons, bubble_comparisons, insertion_comparisons,selection_swaps, bubble_swaps, insertion_swaps)

    else:
        print("ошибка, введите число")


def input_array():
    print("введите числа массива через пробел")
    try:
        arr = list(map(int, input().split()))
        return arr
    except ValueError:
        print("ошибка в типах элементов массива!")
        return []

def edit_array(array):
    print(array)
    print("для изменения введите измененный массив")
    print("сохранить исходный - ок")
    input_line = input().split()
    if input_line[0].lower() == "ок":
        return array
    try:
        edited_arr = list(map(int, input_line))
        return edited_arr
    except ValueError:
        return array

def interactive_mode():
    print("1 - создать массив")
    print("2 - сгенерировать массив")
    array = []

    input_line = input().split()
    try:
        if len(input_line) != 1:
            raise ValueError("Некорректное количество вводимых данных")
        choice = int(input_line[0])
        if choice == 1:
            array = input_array()

        elif choice == 2:
            print("введите параметры через пробел:")
            print("мин.значение макс.значение длина")
            try:
                min_value, max_value, array_length = map(int, input().split())
                if array_length < 1:
                    print("ошибка длинны массива")
                    return

                if min_value > max_value:
                    print("меньшее значение больше большего")
                    return
                array = generate_random_list(min_value, max_value, array_length)
                array = edit_array(array)
            except ValueError:
                print("ошибка ввода")
                return
        else:
            print("Некорректный выбор")
            return

        print("выберите вариант сортировки")
        print("1 - выборочная")
        print("2 - пузырьковая")
        print("3 - вставочная")

        try:
            selection = int(input())
            if selection == 1:
                sorted_array, comparisons, swaps = selection_sort(array)
            elif selection == 2:
                sorted_array, comparisons, swaps = bubble_sort(array)
            elif selection == 3:
                sorted_array, comparisons, swaps = insertion_sort(array)
            else:
                print("Некорректный выбор сортировки")
                return
        except ValueError:
            print("ошибка ввода")
            return

        print("оригинальный массив:")
        print(*array)
        print("-" * 20)
        print("отсортированный массив:")
        print(*sorted_array)
        print()
        print("сравнения:", comparisons, "перестановки:", swaps)
        print("=" * 20)
    except ValueError:
        print("ошибка ввода")
        return



def main():
    global_run = True
    '''menu'''
    while global_run:
        print("1 - демонстрация")
        print("2 - интерактивный")
        print("3 - выход")

        input_line = input().split()
        if len(input_line) == 1:
            tmp = input_line[0]
            if tmp.isdigit():
                tmp = int(tmp)

                if tmp == 1:
                    demo_mode()
                elif tmp == 2:
                    interactive_mode()
                else:
                    global_run = False
            else:
                print("Некорректный ввод")
        else:
            print("Некорректный ввод")



if __name__ == "__main__":
    main()


