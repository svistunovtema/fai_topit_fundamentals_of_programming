measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]
#первый проход
total = 0
minimum = measurements[0]
maximum = measurements[0]
even_count = 0

for value in measurements:
    total += value

    if value < minimum:
        minimum = value
    if value > maximum:
        maximum = value
    if value % 2 == 0:
        even_count += 1

#второй проход
average = total / len(measurements)
highaverage = 0
for value in measurements:
    if value > average:
        highaverage += 1
print("Сумма:", total)
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Чётных значений:", even_count)
print("Среднее:", average)
print("Значений выше среднего:", highaverage)

#линейный поиск
target = int(input("Введите целое число для поиска: "))
found_index = -1

for i in range(len(measurements)):
    if measurements[i] == target:
        found_index = i
        break

print(found_index)

#эксперимент
number = int(input("Введите целое число для проверки на простоту: "))
is_prime = number >= 2
divisor = 2

while is_prime and divisor * divisor <= number:
    if number % divisor == 0:
        is_prime = False
    divisor += 1

if is_prime:
    print("Простое число")
else:
    print("Не простое число")

#практическое расширение
def selection_sort(values):
    for i in range(len(values) - 1):
        smallest_index = i

        for j in range(i + 1, len(values)):
            if values[j] < values[smallest_index]:
                smallest_index = j

        values[i], values[smallest_index] = values[smallest_index], values[i]


def linear_search(values, target):
    comparisons = 0

    for index in range(len(values)):
        comparisons += 1
        if values[index] == target:
            return index, comparisons

    return -1, comparisons


def binary_search(values, target):
    left = 0
    right = len(values) - 1
    comparisons = 0

    while left <= right:
        middle = (left + right) // 2

        comparisons += 1
        if values[middle] == target:
            return middle, comparisons

        comparisons += 1
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comparisons


print("\n| Размер списка | Линейный поиск | Бинарный поиск |")


for size in (10, 100, 1000):
    values = list(range(size, 0, -1))
    selection_sort(values)

    target = size
    _, linear_comparisons = linear_search(values, target)
    _, binary_comparisons = binary_search(values, target)

    print(f"| {size} | {linear_comparisons} | {binary_comparisons} |")
