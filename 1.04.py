# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

width = int(input('Введите ширину плитки: '))
length = int(input('Введите длину плитки: '))
number_of_slices = int(input('Введите количество долек, которое хотите отломить: '))

if (number_of_slices%width==0 or number_of_slices%length==0) and (number_of_slices<width*length):
    print('YES')
else:
    print('NO')