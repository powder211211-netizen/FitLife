# Проект FitLife - MVP версия 1.0

print('Приветствую! Я ваш личный помощник в мире фитнеса!\n')


user_name = input('Как вас зовут? ').title()


while True:  # Проверяем корректность ввода возраста(числом)
    try:
        user_age = int(input('Сколько вам лет? '))
        break
    except ValueError:
        print("Ошибка! Вы ввели текст. Введите только цифры (например, 20).")


user_weight = float(input('Укажите ваш вес в килограммах: '))
user_height = float(input('Укажите ваш рост в метрах (например, 1.80): '))


while user_height < 0.5 or user_height > 2.5:  # Проверяем ввод роста в метрах
    print("Ошибка: Введен неккоректный рост. Проверьте, что ввели в метрах.")
    user_height = float(input('Укажите ваш рост в метрах (например, 1.80): '))


bmi = user_weight / (user_height ** 2)  # Рассчет ИМТ


water_ml = user_weight * 30
water_needed = water_ml / 1000  # Суточный объем воды


print()
print(f'Приятно познакомиться, {user_name}!\n')
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Ваш индекс массы тела: {round(bmi, 1)}')
print(f'Рекомендуемый суточный объем воды: {round(water_needed, 1)}\n')
print("Расчет окончен. Будьте здоровы!")
