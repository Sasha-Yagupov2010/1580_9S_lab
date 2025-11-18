'''
Ночь: с 0:00 до 5:59
Утро: с 6:00 до 11:59
День: с 12:00 до 17:59
Вечер: с 18:00 до 23:59
'''


def translate_hours(hours):
    print(hours,end=" ")
    last_digit = hours % 10
    if 11 <= hours <= 14:
        form = "часов"
    elif last_digit == 1:
        form = "час"
    elif 2 <= last_digit <= 4:
        form = "часа"
    else:
        form = "часов"

    print(form,end=" ")


def translate_minutes(minutes):
    if minutes != 0:
        print(minutes, end=" ")
        last_digit = minutes % 10
        if minutes >= 11 and minutes <= 14:
            form = "минут"
        elif last_digit == 1:
            form = "минута"
        elif 2 <= last_digit <= 4:
            form = "минуты"
        else:
            form = "минут"

        print(form, end=" ")


def print_time_of_day(hours, minutes):
    if 0 <= hours < 6:
        form = "ночи"
    elif 6 <= hours < 12:
        form = "утра"
    elif 12 <= hours < 18:
        form = "дня"
    else:
        form = "вечера"
    print(form,end=" ")

def print_exactly(minutes):
    if minutes == 0:
        print("ровно", end=" ")

def check_hours(hours):
    if hours >= 0 and hours <= 23:
        return True
    else:
        print("Введены недопустимые данные: часы должны быть от 0 до 23.")
        return False


def check_minutes(minutes):
    if minutes >= 0 and minutes <= 59:
        return True
    else:
        print("Введены недопустимые данные: минуты должны быть от 0 до 59.")
        return False


def main():
    '''Обработка ввода чисел с использованием try'''
    print()
    print("Введите время в формате:")
    print("часы минуты")

    input_line = input()
    parts = input_line.split()

    if len(parts) != 2:
        print("ошибка, вводите время в заданном формате")
        return
    
    #if parts[0].count("-")!=0 or parts[1].count("-")!=0:
    if parts[0].startswith('-') or parts[1].startswith('-'):#правильнее, исключение особых случаев
        print("ошибка, вводите время в верном диапозоне значений")
        return
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
    except ValueError:
        print("ошибка, вводите время в заданном формате")
        return


    if not check_hours(hours):
        return
    if not check_minutes(minutes):
        return


    if hours == 0 and minutes == 0:
        print("полночь")
    elif hours == 12 and minutes == 0:
        print("полдень")
    else:
        translate_hours(hours)
        translate_minutes(minutes)
        print_time_of_day(hours, minutes)
        print_exactly(minutes)




if __name__ == "__main__":
    main()
