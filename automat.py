'''
функция вывода стоимости товара
   возвращаем стоимость товара

функция считаем сдачу
    рассчитываем колличество 10
    рассчитываем колличество 5
    рассчитываем колличество 1
    возвращаем колличество монет разного номинала
    

инициализируем массив продуктов

def main():
    принимаем от пользователя строку с названием напитка и целое число — сумму денег.
    если напитка нет в списке, выводим "Неверный выбор".
    получаем стоимость продукта
    если денег хватает, рассчитываем сумму
        
    вычисляем сдачу
    выводим сообщение пользователя

запускаем программу



'''


def get_drink_price(drink_name):
    if drink_name == 'вода':
        return 50
    elif drink_name == 'чай':
        return 75
    elif drink_name == 'кофе':
        return 100
    else:
        return -1

def calculate_change(amount):
    coins_10 = amount // 10
    amount %= 10
    coins_5 = amount // 5
    amount %= 5
    coins_1 = amount
    return coins_10, coins_5, coins_1

drink_list = ["вода","чай","кофе"]

def main():
    drink_name = input(f"Введите название напитка({', '.join(drink_list)}): ").lower()
    if not drink_name in drink_list:
        print("Такого напитка нет в списке")
        return
    try:
        money = int(input("Введите сумму денег: "))
    except ValueError:
        print("Некорректный ввод суммы.")
        return


    price = get_drink_price(drink_name)
    if money < price:
        print("Недостаточно средств")
        return

    change = money - price
    coins_10, coins_5, coins_1 = calculate_change(change)


    print(
        f"Ваш{"a" if drink_name == "вода" else ""} {drink_name}. Сдача: {coins_10} монет по 10 руб., "
        f"{coins_5} по 5 руб., {coins_1} по 1 руб."
    )

if __name__ == "__main__":
    main()
