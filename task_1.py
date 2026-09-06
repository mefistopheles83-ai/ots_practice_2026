# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: [Рахматулов Марсель Рамилевич]

def get_system_info():
    """
    Эта функция должна вернуть словарь с информацией о вашей "системе".
    """
    # TODO: Заполните словарь вашими реальными данными
    system_info = {
        "student_name": "Рахматулов Марсель Рамилевич",
        "academic_group": "ИВТИИбд-12",
        "github_link": "https://github.com/mefistopheles83-ai"
    }
    return system_info

# Вывод информации для проверки
if __name__ == "__main__":
    info = get_system_info()
    print("Информация о системе:")
    for key, value in info.items():
        print(f"- {key}: {value}")

  # Added task_1.py with system info
