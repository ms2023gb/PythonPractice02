# Семинар 2. Циклы(for, while)
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Input: 5 -> 1 0 1 1 0
# Output: 2

num_input = int(input("Введите количество монет: "))  # 5
coin_0 = 0
for i in range(num_input):
    coin_0_or_1 = True
    while coin_0_or_1:
        coin = int(input(f"Введите 0 или 1 для {i + 1} монеты: "))  # 1 0 1 1 0
        if coin == 0 or coin == 1:
            coin_0_or_1 = False
            if coin == 0:
                coin_0 += 1
        else:
            coin_0_or_1 = True
            print("Ошибка, повторите ввод")
if coin_0 > num_input - coin_0:
    print(f"Минимально перевернуть - {num_input - coin_0}")
else:
    print(f"Минимально перевернуть - {coin_0}")