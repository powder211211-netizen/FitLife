# Проект FitLife - MVP версия 1.0

print('Приветствую! Я ваш личный помощник в мире фитнеса!\n')


user_name = input('Как вас зовут? ').title()


while True:  # Проверяем корректность ввода возраста(числом)
    try:
        user_age = int(input('Сколько вам лет? '))
        break
    except ValueError:
        print("Ошибка! Вы ввели текст. Введите только цифры (например, 20).")


# user_weight = float(input('Укажите ваш вес в килограммах: '))
# user_height = float(input('Укажите ваш рост в метрах (например, 1.80): '))


while True:  # Проверяем корректность ввода веса(числом)
    try:
        user_weight = float(input('Укажите ваш вес в килограммах: '))
        break
    except ValueError:
        print("Ошибка! Вы ввели текст. Введите только цифры (например, 75).")


while True:  # Проверяем корректность ввода роста(числом)
    try:
        user_height = float(input('Укажите рост в метрах (например, 1.80): '))
        break
    except ValueError:
        print("Ошибка! Вы ввели текст. Введите только цифры (например, 1.80).")


while not 0.5 < user_height < 2.5:  # Проверяем ввод роста в метрах
    print("Ошибка: Введен неккоректный рост. Проверьте, что ввели в метрах.")
    user_height = float(input('Укажите рост в метрах (например, 1.80): '))


bmi = round(user_weight / (user_height ** 2), 2)  # Рассчет ИМТ


WATER_PER_KG = 30
ML_PER_LITER = 1000


water_ml = user_weight * WATER_PER_KG
water_needed = round(water_ml / ML_PER_LITER, 2)  # Суточный объем воды


print()
print(f'Приятно познакомиться, {user_name}!\n')
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш индекс массы тела: {bmi}')
print(f'Рекомендуемый суточный объем воды: {water_needed}\n')
print("Расчет окончен. Будьте здоровы!")
