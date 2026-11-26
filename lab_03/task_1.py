def classify_student(score, work_type, absences):
    if score not in range(0, 101):
        return "error", None
    elif absences not in range(0, 6):
        return "error", None
    else:
        if score >= 90:
            level_index = 3
        elif score >= 75:
            level_index = 2
        elif score >= 60:
            level_index = 1
        else:
            level_index = 0

        if absences > 3 and level_index > 0:
            level_index -= 1

        level = levels[level_index]

        match work_type:
            case "exam":
                explanation = "экзаменационная работа"
            case "project":
                explanation = "проектная работа"
            case "practice":
                explanation = "практическая работа"
            case _:
                explanation = "неизвестный тип работы"

        return f"{level} — {explanation}", level


levels = ["недостаточный", "удовлетворительный", "хороший", "отличный"]



score = int(input())
work_type = input().strip()
absences = int(input())


single_result, _ = classify_student(score, work_type, absences)
print(single_result)

records = [
    (0, "exam", 5),
    (59, "project", 0),
    (60, "practice", 3),
    (74, "exam", 4),
    (75, "project", 0),
    (89, "practice", 0),
    (90, "exam", 0),
    (100, "project", 5),
    (75, "quiz", 0),
    (101, "exam", 0),
]

results = []
counts = {}

for level in levels:
    counts[level] = 0

for score, work_type, absences in records:
    result, level = classify_student(score, work_type, absences)
    results.append(f"{score}, {work_type}, {absences} — {result}")

    if level is not None:
        counts[level] += 1

print("\nИндивидуальные результаты")
for result in results:
    print(result)

print("\nИтоговая сводка")
for level in levels:
    print(f"{level}: {counts[level]}")