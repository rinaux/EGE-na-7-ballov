'''with open('8_0028. txt') as f:
    n = int (f. readline())
    a = [int(x) for x in f]
m = 0
for i in range(len(a) - 1):
    m = max (m, a[i] + a[i + 1])
print (m)'''

'''with open('8_0020. txt') as f:
    a = [int(x) for x in f]
m = float ('-inf')
for i in range(len(a)):
    if a[i] % 10 = 3:
        m = max (m, a[i])
k = 0
s = float ('-infl
for i in range(len(a)-1):
    if (a[i] % 10 == 3 and a[i+1] % 10 != 3 or a[i]
    k += 1
    s = max(s, a[i]**2 + a[i+1]**2)
print (k, s)'''

'''with open ('1_0038. csv') as f:
    a = [[int(y) for y in x.split(',')] for x in f]
k = 0
for a, b, c in a:
    if a < b + cand b < a + c and c < a + b:
        k += 1
print (k)'''

'''with open('8_0021,txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f]
m = 0
k = 0
b = 0
afor i in range(len(a)): 1
    if a[i] % 3 == 0:
        m = max (a[il, m)
for i in range(len(a)-1):
    if (a[i] % 4 == 0 or a[i+1] % 4 == 0) and ((a[i] + a[i+1]) <= m):
        k = max(k, abs (a[i] + a[i+1]))
        b += 1
print (b, k)'''

'''with open('13_0021.txt') as f:
    n = int(f.readline())
    a = [int(x) for x in f]
m = float('-inf')
for i in range(len(a)-1):
    if abs(a[i]) % 5 == 0:
        m = max(m, a[i])
k = 0
s = float('-inf')
for i in range(len(a)-1):
    if (abs(a[i]) % 8 == 0 and abs(a[i+1]) % 8 != 0) or (abs(a[i]) % 8 != 0 and abs(a[i+1]) % 8 == 0) or (abs(a[i]) % 8 == 0 or abs(a[i+1]) % 8 == 0) and a[i]+a[i+1] <= m:
        k += 1
        s = max(s, (a[i]+a[i+1]))
print(k, s)
m = 100000000000
for i in range(len(a)-1):
    m = min(m, a[i])
k = 0
s = float('-inf')
for i in range(len(a)-1):
    if (abs(a[i]) % 109 == m or abs(a[i+1]) % 109 != m) and (abs(a[i]) % 109 != m or abs(a[i+1]) % 109 == m):
        k += 1
        s = max(s, (a[i]+a[i+1]))
print(k, s)'''


# Открываем файл и считываем данные
with open('13_0021.txt') as f:
    n = int(f.readline().strip())  # Читаем количество элементов
    a = [int(line.strip()) for line in f]  # Читаем последовательность чисел
# Инициализация переменных
m = float('-inf')
# Находим максимальный элемент, кратный 5
for number in a:
    if number % 5 == 0:
        m = max(m, number)
k = 0  # Счетчик пар
s = float('-inf')  # Максимальная сумма
# Ищем пары, соответствующие условиям
for i in range(len(a) - 1):
    current_pair_sum = a[i] + a[i + 1]
    # Проверяем условия для пар
    if ((abs(a[i]) % 8 == 0) or (abs(a[i + 1]) % 8 == 0)) and (current_pair_sum <= m):
        k += 1  # Увеличиваем счетчик пар
        s = max(s, current_pair_sum)  # Обновляем максимальную сумму
# Вывод результатов
print(k, s)

