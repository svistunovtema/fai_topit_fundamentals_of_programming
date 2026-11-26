def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    if not values:
        raise ValueError("Для вычисления среднего нужен непустой список")

    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и делает первую букву каждой части заглавной."""
    parts = name.split()
    return " ".join(part.capitalize() for part in parts)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчёт о результатах студента."""
    name = normalize_name(student)

    if not results:
        return f"{prefix}: {name} — нет результатов"

    average = arithmetic_mean(results)
    return f"{prefix}: {name} — средний балл {average:.{precision}f}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    cleaned_tags = []
    seen = set()

    for tag in tags:
        tag = tag.strip()
        if lowercase:
            tag = tag.lower()

        if tag and tag not in seen:
            seen.add(tag)
            cleaned_tags.append(tag)

    return tuple(cleaned_tags)

#Исправленная функция
def add_result(value, results=None):
    if results is None:
        results = []
    else:
        results = results.copy()

    results.append(value)
    return results


assert add_result(5) == [5]
assert add_result(4) == [4]

original = [3]
assert add_result(5, original) == [3, 5]
assert original == [3]

#Практическое расширение
def apply_to_results(operation, values):
    transformed = []

    for value in values:
        transformed.append(operation(value))

    return transformed


def add_bonus(value):
    return value + 1


def make_threshold_checker(threshold):
    def check_result(result):
        return result >= threshold

    return check_result



# Проверки arithmetic_mean
assert arithmetic_mean([2.0, 4.0, 6.0]) == 4.0
assert arithmetic_mean(values=[5.5]) == 5.5
assert arithmetic_mean([-2.0, 2.0]) == 0.0

# Проверки normalize_name
assert normalize_name("  аННа   иВАНОВА ") == "Анна Иванова"
assert normalize_name(name="БОРИС") == "Борис"
assert normalize_name("   ") == ""

# Проверки build_report
assert build_report("анна", [4, 5]) == "Результат: Анна — средний балл 4.50"
assert build_report(
    student="борис", results=[3, 4], precision=1, prefix="Итог"
) == "Итог: Борис — средний балл 3.5"
assert build_report("дарья", []) == "Результат: Дарья — нет результатов"

# Проверки collect_tags
assert collect_tags(" Python ", "python", " LAB ") == ("python", "lab")
assert collect_tags("", "   ") == ()
assert collect_tags("Lab", "lab", "Lab", lowercase=False) == ("Lab", "lab")


### Именованная функция и lambda
results = [3, 4, 5]

print(apply_to_results(add_bonus, results))                
print(apply_to_results(lambda value: value * 2, results))   

# Две проверки с разными порогами
check_at_least_4 = make_threshold_checker(4)
check_at_least_5 = make_threshold_checker(5)


print(check_at_least_4(4))  
print(check_at_least_5(4))  
print(check_at_least_5(5))  
### 


tag_list = [" Python ", "LAB", "python"]
print(collect_tags(*tag_list))  


report_options = {"precision": 1, "prefix": "Итог"}
print(build_report("анна", [4, 5], **report_options))

#Исследование LEGB
course = "Основы программирования"


def demonstrate_scope():
    course = "Коллекции"

    def change_course(new_course):
        nonlocal course
        course = new_course

    print("В функции до изменения:", course)
    change_course("Функции")
    print("В функции после изменения:", course)


demonstrate_scope()
print("На уровне файла:", course)