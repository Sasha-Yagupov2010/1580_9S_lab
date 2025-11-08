'''
Ночь: с 0:00 до 5:59
Утро: с 6:00 до 11:59
День: с 12:00 до 17:59
Вечер: с 18:00 до 23:59
'''


def translate_hours(hours):
    print(hours,end=" ")


def translate_minutes(minutes):
    print(minutes,end=" ")


def check_hours(hours):
    if hours >= 0 and hours <= 23:
        return True
    else:
        return False


def check_minutes(minutes):
    if minutes >= 0 and minutes <= 59:
        return True
    else:
        return False

input_error_text = "Ошибка, неверный формат вводимых данных!"
def main():
    ''' обработка ввода чисел'''

    print("Введите время в формате:")
    print("часы минуты")

    input_line = input()
    parts = input_line.split()

    if len(parts) == 2:
        hours = parts[0]
        minutes = parts[1]

        if hours.isdigit() and minutes.isdigit():
            hours = int(hours)
            minutes = int(minutes)

            if check_hours(hours) and check_minutes(minutes):
                translate_hours(hours)
                translate_minutes(minutes)
            else:
                print(input_error_text)

        else:
            print(input_error_text)

    else:
        print(input_error_text)






if __name__ == "__main__":
    main()