import random

def generate_random_count(from_count, to_count):
    random_number = random.randint(from_count, to_count)
    return random_number

def generate_random_list(min_count, max_count, list_length):
    arr = [random.randint(min_count, max_count) for i in range(list_length)]
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
    header = (
        f"{'Метод сортировки':<20} | "
        f"{'Сравнений':<12} | "
        f"{'Перестановок':<15}"
    )
    separator = '-' * len(header)
    print(separator)
    print(header)
    print(separator)

    # Строки с данными
    print(
        f"{'Selection Sort':<20} | "
        f"{selection_comparisons:<12} | "
        f"{selection_swaps:<15}"
    )
    print(
        f"{'Bubble Sort':<20} | "
        f"{bubble_comparisons:<12} | "
        f"{bubble_swaps:<15}"
    )
    print(
        f"{'Insertion Sort':<20} | "
        f"{insertion_comparisons:<12} | "
        f"{insertion_swaps:<15}"
    )
    print(separator)


def demo_mode():
    print("введите длинну массива")
    input_line = input()
    if input_line.isdigit():
        arr_length = int(input_line)

        arr = generate_random_list(0, 99,arr_length)
        print("созданный массив:")
        print(*arr)
        selection_arr,selection_comparisons,selection_swaps = selection_sort(arr)
        bubble_arr,bubble_comparisons,bubble_swaps = bubble_sort(arr)
        insertion_arr,insertion_comparisons,insertion_swaps = insertion_sort(arr)

        print()

        draw_table(selection_comparisons, bubble_comparisons, insertion_comparisons,selection_swaps, bubble_swaps, insertion_swaps)
    else:
        print("ошибка")



def interactive_mode():
    print("")
    input_line = input().split()
    if len(input_line) == 3:
        if input_line[0].isdigit() and input_line[1].isdigit()and input_line[2].isdigit():
            min_count = int(input_line[0])
            max_count = int(input_line[1])
            arr_length = int(input_line[2])


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
                print("ошибка!")




if __name__ == "__main__":
    main()


