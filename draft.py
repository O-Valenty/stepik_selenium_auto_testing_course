import os
# Поиск пути файла
# Этот код рекурсивно обойдет все вложенные папки внутри корневой папки
# и выведет путь к файлу.
search_folder = "D:/stepik_selenium_auto_testing_course"  # Укажи корневую папку
file_name = "step10_successful_registration_practice.py"

for root, _, files in os.walk(search_folder):
    if file_name in files:
        print("Файл найден:", os.path.join(root, file_name))
        break
