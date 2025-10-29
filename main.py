#словник
diction = [
    {"Номер групи": "103", "ПІБ": "Лагода Тимофій Сергійович", "Курс": "2",
     "Предмети та оцінки": {"Програмування": "76", "Англійська": "67"}},
    {"Номер групи": "103", "ПІБ": "Мізерний Іван Володимирович", "Курс": "3",
     "Предмети та оцінки": {"Математика": "78", "Програмування": "80"}},
    {"Номер групи": "102", "ПІБ": "Лєпіхін Гліб Ігорович", "Курс": "3",
     "Предмети та оцінки": {"Українська мова": "97"}},
    {"Номер групи": "102", "ПІБ": "Зякун Владислав Олександрович", "Курс": "2",
     "Предмети та оцінки": {"Англійська": "69", "Чисельні методи": "79", "Українська мова": "89"}}
]
#Функція виведення (Мізерний Іван)
def print_diction():
    print("-" * 100)
    print(f"{'ПІБ':<30} | {'Номер групи':<5} | {'Курс':<3} | {'Предмети та Оцінки':}")
    for element in diction:#друк всіх елементів словнику за допомогою циклу
        pib = element["ПІБ"]
        group = element["Номер групи"]
        course = element["Курс"]
        subjects_and_mark = element["Предмети та оцінки"]
        # використаний метод .join, щоб вивести елементи вкладеного словника через кому
        subjects_mark = ", ".join(f"{k}: {v}" for k, v in subjects_and_mark.items())
        print(f"{pib:<30} | {group:^11} | {course:^4} | {subjects_mark:}")
    print("-" * 100)
#Функція оновлення елементу (Мізерний Іван)
def update_diction():
    update = input("Введіть ПІБ студента, для якого потрібно оновити дані: ")
    for element in diction:
        if element["ПІБ"].lower() == update.lower():#пошук введених даних у списку
            choice = input("Виберіть параметр для оновлення: 1 - Номер групи, 2 - Курс, 3 - Оцінка за вибраним предметом ")
            if choice == "1":
                update_element = input(f"Введіть новий номер групи для студента {element["ПІБ"]}: ")
                element["Номер групи"] = update_element#оновлення старого значення номеру групи
                print(f"Новий номер групи для студента {element["ПІБ"]}: {update_element}")
            if choice == "2":
                update_element = input(f"Введіть новий курс групи для студента {element["ПІБ"]}: ")
                element["Курс"] = update_element#оновлення старого значення курсу
                print(f"Новий курс для студента {element["ПІБ"]}: {update_element}")
            if choice == "3":
                subject_name = input("Введіть предмет для якого бажаєте змінити оцінку: ")
                if subject_name in element["Предмети та оцінки"]:#пошук елементу у вкладеному словнику
                    update_element = input(f"Введіть нову оцінку за вибраним предметом для студента {element["ПІБ"]} ")
                    element["Предмети та оцінки"][subject_name] = update_element#оновлення старого значення оцінки для вибраного предмету
                    print(f"Нова оцінка для студента {element["ПІБ"]} з дисципліни {subject_name}: {update_element}")
# Функція додавання студента (Лагода Тимофій)
def addstudent():
    lessons = {}#створення вкладеного словнику для предметів та оцінок
    #заповнення нового елемента словника
    number = input("Введіть номер групи: ")
    pib = input("Введіть ПІБ студента: ")
    course = input("Введіть номер курсу: ")
    k = int(input("Введіть кількість предметів: "))
    for i in range(k):
        lesson = input("Введіть назву предмета: ")
        grade = input("Введіть оцінку: ")
        lessons[lesson] = grade
    new_student = {#створення нового елеметну словника
        "Номер групи": number,
        "ПІБ": pib,
        "Курс": course,
        "Предмети та оцінки": lessons
    }
    diction.append(new_student)
#Функція видалення (Зякун Владислав)
def delete_student():
    pib_to_delete = input("Введіть ПІБ студента, якого потрібно видалити: ")
    for student in diction:
        if student["ПІБ"].lower() == pib_to_delete.lower():#пошук студента, якого потрібно видалити
            diction.remove(student)
            print(f"\nСтудента {student['ПІБ']} видалено з бази\n")
            return
    print("Студента з таким ПІБ не знайдено")
#Функція пошуку (Лєпіхін Гліб)
def search():
    while True:
        print("\nОберіть критерій пошуку:")
        print("1 - За ПІБ")
        print("2 - За номером групи")
        print("3 - За курсом")
        choice = input("Ваш вибір: ")
        if choice == "1":
            key = "ПІБ"
            value = input("Введіть ПІБ для пошуку: ")
        elif choice == "2":
            key = "Номер групи"
            value = input("Введіть номер групи для пошуку: ")
        elif choice == "3":
            key = "Курс"
            value = input("Введіть номер курсу для пошуку: ")
        else:
            print("Некоректний ввід")
            return
        found = False
        print(f"\nРезультати пошуку за '{key}' = {value}:")
        print("-" * 100)
        for student in diction:  # цикл для виводу знайдених студентів за вибраним критерієм (якщо критерій знайдено)
            if student[key].lower() == value.lower():
                pib = student["ПІБ"]
                group = student["Номер групи"]
                course = student["Курс"]
                subjects_and_mark = student["Предмети та оцінки"]
                subjects_mark = ", ".join(f"{k}: {v}" for k, v in subjects_and_mark.items())
                print(f"ПІБ: {pib} | Номер групи: {group} | Курс: {course} | Предмети та Оцінки: {subjects_mark}")
                found = True
        if not found:  # якщо критерій не знайдено
            print("Студентів не знайдено.")
        print("-" * 100)
        while True:  # можливість повторного пошуку
            again = input("\nБажаєте здійснити ще один пошук? (так/ні): ")
            if again.lower() == "так":
                break
            elif again.lower() == "ні":
                print("Пошук завершено.")
                return
            else:
                print("Некоректний ввід. Спробуйте ще раз")

    # Меню вибору (Зякун Владислав)
def main_menu():
    while True:
        print("\nМЕНЮ ")  # меню вибору функцій
        print("1 - Показати всіх студентів")
        print("2 - Додати нового студента")
        print("3 - Видалити студента")
        print("4 - Пошук")
        print("5 - Оновити дані")
        print("6 - Вийти")
        choice = input("Ваш вибір: ")
        if choice == "1":
            print_diction()
        elif choice == "2":
            addstudent()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            search()
        elif choice == "5":
            update_diction()
        elif choice == "6":
            print("Програму завершено.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
main_menu()