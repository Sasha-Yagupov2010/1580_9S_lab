import random

def generate_random_count(from_count, to_count):
    random_number = random.randint(from_count, to_count)
    return random_number

def generate_random_list(min_count, max_count, list_length):
    arr = [random.randint(min_count, max_count) for i in range(list_length)]
    return arr

def selection_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        min_idx = i
        for j in range(i + 1, arr_length):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(0, arr_length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



def demo_mode():
    print("введите диапозон значений для заполнения")
    print("формат: мин.знач  макс.знач  длинна")
    input_line = input().split()
    if len(input_line) == 3:
        if input_line[0].isdigit() and input_line[1].isdigit()and input_line[2].isdigit():
            min_count = int(input_line[0])
            max_count = int(input_line[1])
            arr_length = int(input_line[2])

            arr = generate_random_list(min_count, max_count,arr_length)
            print("созданный массив:")
            print(*arr)

        else:
            print("ошибка, неверные входные данные!")
            return
    else:
        print("ошибка, неверные входные данные!")
        return

def interactive_mode():
    print("")


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


