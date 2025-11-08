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
    if minutes == 0:
        form = "ровно"
    else:
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
        return "ночь"
    elif 6 <= hours < 12:
        return "утро"
    elif 12 <= hours < 18:
        return "день"
    else:
        return "вечер"


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

output_error_text = "Ошибка, неверный формат вводимых данных!"

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
                if hours == 0 and minutes == 0:
                    print("полночь")
                elif hours == 12 and minutes == 0:
                    print("полдень")
                else:
                    translate_hours(hours)
                    translate_minutes(minutes)
                    print_time_of_day(hours, minutes)
            else:
                print(output_error_text)

        else:
            print(output_error_text)

    else:
        print(output_error_text)




if __name__ == "__main__":
    main()