students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}


def mean(values):
    if not values:
        return None
    return sum(values) / len(values)


def minimum(values):
    if not values:
        return None

    smallest = values[0]
    for value in values:
        if value < smallest:
            smallest = value
    return smallest


def maximum(values):
    if not values:
        return None

    largest = values[0]
    for value in values:
        if value > largest:
            largest = value
    return largest


def classify(score):
    if score >= 90:
        return "отличный"
    elif score >= 75:
        return "хороший"
    elif score >= 60:
        return "удовлетворительный"
    return "недостаточный"


def student_summary(name, results):
    average = mean(results)
    category = "нет результатов" if average is None else classify(average)

    return {
        "name": name,
        "mean": average,
        "min": minimum(results),
        "max": maximum(results),
        "category": category,
    }


def find_top_students(students):
    leaders = []
    best_average = None

    for name, results in students.items():
        average = mean(results)
        if average is None:
            continue

        if best_average is None or average > best_average:
            best_average = average
            leaders = [name]
        elif average == best_average:
            leaders.append(name)

    return leaders


def group_summary(students):
    counts = {
        "отличный": 0,
        "хороший": 0,
        "удовлетворительный": 0,
        "недостаточный": 0,
        "нет результатов": 0,
    }
    all_results = []

    for name, results in students.items():
        data = student_summary(name, results)
        counts[data["category"]] += 1
        all_results.extend(results)

    return {
        "mean": mean(all_results),
        "min": minimum(all_results),
        "max": maximum(all_results),
        "counts": counts,
        "leaders": find_top_students(students),
    }


def format_report(student_data, group_data):
    ranked = sorted(
        (data for data in student_data if data["mean"] is not None),
        key=lambda data: data["mean"],
        reverse=True,
    )

    lines = ["Рейтинг студентов"]
    for place, data in enumerate(ranked, start=1):
        lines.append(
            f"{place}. {data['name']} — средний {data['mean']:.2f}, "
            f"мин. {data['min']}, макс. {data['max']}, {data['category']}"
        )

    for data in student_data:
        if data["mean"] is None:
            lines.append(f"{data['name']} — нет результатов")

    lines.append("\nСтатистика группы")
    if group_data["mean"] is None:
        lines.append("У группы нет результатов")
    else:
        lines.append(f"Средний балл группы: {group_data['mean']:.2f}")
        lines.append(f"Минимум: {group_data['min']}, максимум: {group_data['max']}")
        lines.append("Лидеры: " + ", ".join(group_data["leaders"]))

    lines.append("\nКоличество студентов по категориям")
    for category, count in group_data["counts"].items():
        lines.append(f"{category}: {count}")

    return "\n".join(lines)


student_data = [
    student_summary(name, results) for name, results in students.items()
]
group_data = group_summary(students)
print(format_report(student_data, group_data))