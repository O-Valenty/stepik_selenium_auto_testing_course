# stepik_selenium_auto_testing_course
## Проект для хранения практических заданий по курсу "Автоматизация тестирования с помощью Selenium и Python".

__[Stepik course link](https://stepik.org/course/575/syllabus "Перейти на сайт курса")__

---
### Начало работы:
1. Создайте виртуальное окружение: `python -m venv environment_name`
2. Активируйте виртуальное окружение[^2]: `environment_name\Script\activate`
3. Установите requirements.txt[^3]: `pip install -r requirements.txt`
4. Чтобы выйти из виртуального окружения, выполните команду: `deactivate`



### Структура:
* chapter_ - раздел курса
* lesson_ - урок в разделе
* step_ - номер шага, на котором дано практическое задание[^1]
* find_element - краткое описание сути задания следует за номером шага

[^1]: Если "step_" отсутствуют, это указывает на то, что файл
содержит заметки по теоретической части урока.
[^2]: Если при попытке подключения виртуального окружения вы столкнулись с ошибкой "Невозможно загрузить файл "...", так как выполнение сценариев отключено в этой системе.", воспользуйтесь командой <Set-ExecutionPolicy Unrestricted -Scope Process> и повторите подключение виртуального окружения.
[^3]: Просмотреть список установленных пакетов можно командой <pip list>

