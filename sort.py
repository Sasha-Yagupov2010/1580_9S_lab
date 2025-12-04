import random

def generate_random_count(from_count, to_count):
    random_number = random.randint(from_count, to_count)
    return random_number

def generate_random_list(min_count, max_count, list_length):
    arr = [generate_random_count(min_count, max_count) for i in range(list_length)]
    return arr

def selection_sort(arr):
    arr_copy = arr.copy()
    comparisons = 0
    swaps = 0
    arr_length = len(arr_copy)
    for i in range(arr_length):
        min_idx = i
        for j in range(i + 1, arr_length):
            comparisons += 1
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        if min_idx != i:
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
            swaps += 1
    return arr_copy, comparisons, swaps

def bubble_sort(arr):
    arr_copy = arr.copy()
    comparisons = 0
    swaps = 0
    arr_length = len(arr_copy)
    for i in range(arr_length):
        swapped = False
        for j in range(0, arr_length - i - 1):
            comparisons += 1
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr_copy, comparisons, swaps

def insertion_sort(arr):
    arr_copy = arr.copy()
    comparisons = 0
    swaps = 0

    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        
        # Считаем сравнения
        while j >= 0:
            comparisons += 1
            if arr_copy[j] > key:
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
            else:
                break
 
        if j != i - 1:
            arr_copy[j + 1] = key
            swaps += 1
            
    return arr_copy, comparisons, swaps

def draw_table(selection_comparisons, bubble_comparisons, insertion_comparisons, 
                  selection_swaps, bubble_swaps, insertion_swaps):
    print()
    header = f"{'Метод сортировки':<20} | {'Сравнений':<12} | {'Перестановок':<15}"
    separator = '-' * len(header)
    print(separator)
    print(header)
    print(separator)

    print(f"{'Selection Sort':<20} | {selection_comparisons:<12} | {selection_swaps:<15}")
    print(f"{'Bubble Sort':<20} | {bubble_comparisons:<12} | {bubble_swaps:<15}")
    print(f"{'Insertion Sort':<20} | {insertion_comparisons:<12} | {insertion_swaps:<15}")

    print(separator)
    print()

def demo_mode():
    print("Введите длину массива:")
    input_line = input()
    try:
        arr_length = int(input_line)
        
        if arr_length<=1:
            print("ошибка, длинна массива не должна быть меньше 2")#равная 1 не имеет смысл
            return
        
        arr = generate_random_list(0, 99, arr_length)
        print("Созданный массив:")
        print(*arr)
        
        selection_arr, selection_comparisons, selection_swaps = selection_sort(arr)
        bubble_arr, bubble_comparisons, bubble_swaps = bubble_sort(arr)
        insertion_arr, insertion_comparisons, insertion_swaps = insertion_sort(arr)

        draw_table(selection_comparisons, bubble_comparisons, insertion_comparisons, 
                  selection_swaps, bubble_swaps, insertion_swaps)

    except ValueError:
        print("Ошибка: введите число")

def input_array():
    print("Введите числа массива через пробел:")
    try:
        arr = list(map(int, input().split()))
        return arr
    except ValueError:
        print("Ошибка: введите целые числа!")
        return []

def edit_array(array):
    print("Текущий массив:")
    print(*array)
    print("Для изменения введите измененный массив (числа через пробел)")
    print("Для сохранения исходного введите 'yes' или 'ок'")
    
    input_line = input().split()
    if not input_line:
        print("Ошибка: ничего не введено")
        return array
    
    if input_line and (input_line[0].lower() in ['ок', 'ok', 'y', 'yes', 'да']):# без больщого количесва or можно таким образом сделать проще
        return array
    try:
        edited_arr = list(map(int, input_line))
        return edited_arr
    except ValueError:
        print("Ошибка: введены некорректные данные, оставлен исходный массив")
        return array

def interactive_mode():
    print("1 - ввести массив вручную")
    print("2 - сгенерировать массив")
    array = []
    
    try:
        choice = int(input())
        if choice == 1:
            array = input_array()
            if not array:
                print("Массив пустой!")
                return

        elif choice == 2:
            print("Введите параметры через пробел:")
            print("мин.значение макс.значение длина")
            try:
                params = input().split()
                if len(params) != 3:
                    print("Ошибка: нужно ввести 3 числа!")
                    return
                min_value, max_value, array_length = map(int, params)
                
                if array_length<=1:
                    print("ошибка, длинна массива не должна быть меньше 2")#равная 1 не имеет смысл
                    return
                '''
                if array_length>100000:#в условии не сказанно но пользователь может ввести огромную длинну для генерации
                    print("Внимание, возможно длительное выполнение программы!")
                    return
                '''    
                if min_value > max_value:
                    min_value, max_value = max_value, min_value
                    print("Заметка: min и max значения были автоматически поменяны местами")#можно было просто min max, но почему бы не сказать пользователю
                array = generate_random_list(min_value, max_value, array_length)
                array = edit_array(array)
            except ValueError:
                print("Ошибка ввода параметров")
                return

        else:
            print("Неверный выбор")
            return

        print("Выберите вариант сортировки:")
        print("1 - выборочная")
        print("2 - пузырьковая")
        print("3 - вставочная")

        try:
            selection = int(input())
            if selection == 1:
                sorted_array, comparisons, swaps = selection_sort(array)
                sort_name = "Selection Sort"
            elif selection == 2:
                sorted_array, comparisons, swaps = bubble_sort(array)
                sort_name = "Bubble Sort"
            elif selection == 3:
                sorted_array, comparisons, swaps = insertion_sort(array)
                sort_name = "Insertion Sort"
            else:
                print("Неверный выбор сортировки")
                return
            
            print(f"\n{sort_name}:")
            print("Оригинальный массив:")
            print(*array)
            print("-" * 20)
            print("Отсортированный массив:")
            print(*sorted_array)
            print()
            print(f"Сравнения: {comparisons}")
            print(f"Перестановки: {swaps}")

        except ValueError:
            print("Ошибка ввода выбора сортировки")
            return

    except ValueError:
        print("Ошибка ввода")
        return

def main():
    global_run = True
    while global_run:
        print()
        print("="*40)
        print("Главное меню:")
        print("1 - демонстрация")
        print("2 - интерактивный")
        print("3 - выход")
        print("="*40)

        try:
            choice = int(input("Выберите режим: "))
            if choice == 1:
                demo_mode()
            elif choice == 2:
                interactive_mode()
            elif choice == 3:
                global_run = False
                print("Выход из программы...")
            else:
                print("Неверный выбор. Введите 1, 2 или 3.")
        except ValueError:
            print("Ошибка: введите число от 1 до 3")

if __name__ == "__main__":
    main()   
