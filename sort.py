import random

def generate_random_count(from_count, to_count):
    random_number = random.randint(from_count, to_count)
    return random_number

def generate_random_list(min_count, max_count, list_length):
    arr = [random.randint(min_count, max_count) for _ in range(list_length)]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    pass


if __name__ == "__main__":
    main()


