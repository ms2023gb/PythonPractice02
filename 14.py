# Семинар 2. Циклы(for, while)
# Задача 14: Требуется вывести все целые степени двойки (т.е. числа 
# вида 2^k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8
num_input = int(input("Input: "))
i = 0
print(f"Output: {num_input}", end=" -> ")
while 2 ** i <= num_input:
    print(f"{2 ** i}", end=" ")
    i += 1