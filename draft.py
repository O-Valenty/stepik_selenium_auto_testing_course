# import os
# # Поиск пути файла
# # Этот код рекурсивно обойдет все вложенные папки внутри корневой папки
# # и выведет путь к файлу.
# search_folder = "D:/stepik_selenium_auto_testing_course"  # Укажи корневую папку
# file_name = "_practice.py"

# for root, _, files in os.walk(search_folder):
#     if file_name in files:
#         print("Файл найден:", os.path.join(root, file_name))
    

# скрипт, который найдет все файлы с "_practice" в названии в папке "D:/stepik_selenium_auto_testing_course"
# и ее вложенных папках, а затем переименует их, убрав "_practice" из названия.

# Папка, в которой будем искать файлы
search_folder = "D:/stepik_selenium_auto_testing_course"

# Проход по всем файлам во вложенных папках
for root, _, files in os.walk(search_folder):
    for file in files:
        if "_practice" in file:  # Проверяем, есть ли в названии _practice
            old_path = os.path.join(root, file)  # Полный путь к старому файлу
            new_name = file.replace("_practice", "")  # Убираем _practice
            new_path = os.path.join(root, new_name)  # Полный путь к новому файлу
            
            os.rename(old_path, new_path)  # Переименовываем файл
            print(f"Переименован: {old_path} -> {new_path}")