# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трехзначное число: '))

num1 = number//100
num2 = number//10%10
num3 = number%10
sum = num1 + num2 + num3
print(f'У цифр числа {number} сумма цифр {num1} + {num2} + {num3} равна {sum}')