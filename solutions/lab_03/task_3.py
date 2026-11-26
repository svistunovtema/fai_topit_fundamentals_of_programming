import sys

submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = set()
laboratories = set()
attempts_by_student = {}
best_results = {}
attempt_counts = {}
students_by_lab = {}


def add_submission(student, laboratory, score):
    students.add(student)
    laboratories.add(laboratory)

    if student not in attempts_by_student:
        attempts_by_student[student] = []
    attempts_by_student[student].append((laboratory, score))

    key = (student, laboratory)

    if key not in best_results or score > best_results[key]:
        best_results[key] = score

    attempt_counts[key] = attempt_counts.get(key, 0) + 1

    if laboratory not in students_by_lab:
        students_by_lab[laboratory] = set()
    students_by_lab[laboratory].add(student)


for student, laboratory, score in submissions:
    add_submission(student, laboratory, score)

both_works = students_by_lab["lab_01"] & students_by_lab["lab_02"]
print("Сдавали обе работы до обновления:", sorted(both_works))

new_submission = ("daria", "lab_02", 4)
submissions.append(new_submission)
student, laboratory, score = new_submission
add_submission(student, laboratory, score)

print("Студенты:", sorted(students))
print("Лабораторные работы:", sorted(laboratories))
print("Попытки по студентам:", attempts_by_student)
print("Лучшие результаты:", best_results)
print("Количество попыток:", attempt_counts)

both_works = students_by_lab["lab_01"] & students_by_lab["lab_02"]
print("Сдавали обе работы после обновления:", sorted(both_works))


#практическое расширение
for line in sys.stdin:
    parts = line.split()

    if not parts:
        continue

    match parts:
        case ["student", student]:
            result = attempts_by_student.get(student)

        case ["best", student, laboratory]:
            result = best_results.get((student, laboratory))

        case ["attempts", student, laboratory]:
            result = attempt_counts.get((student, laboratory))

        case ["completed", laboratory]:
            students_for_lab = students_by_lab.get(laboratory)
            if students_for_lab is None:
                result = None
            else:
                result = sorted(students_for_lab)

        case _:
            print("Неизвестная команда или неверное число аргументов")
            continue

    if result is None:
        print("Данные не найдены")
    else:
        print(result)