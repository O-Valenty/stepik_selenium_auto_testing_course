import unittest  # подключаем модуль unittest, который помогает писать и запускать тесты.

# class – это класс. Это шаблон (схема), по которому можно создавать объекты.

# За словом 'class' следует любое ваше название тестового класса.
# В в unittest принято, что названия классов тестов начинаются с Test, чтобы их легко находила тестовая система.

# unittest.TestCase – это готовый класс из модуля unittest.
# Мы наследуем (TestAbs берет всё от unittest.TestCase) и получаем возможность использовать встроенные методы тестирования (например, assertEqual).

class TestAbs(unittest.TestCase):

# В unittest тесты всегда должны быть функциями внутри класса.
# Простые инструкции (print, if, for) в классе не запустятся автоматически, а вот функции запустятся.
# В unittest все функции тестов должны начинаться с test_, иначе они не запустятся.
    def test_abs1(self):
# self – это ссылка на сам объект, внутри которого мы находимся.
# Он нужен внутри классов, чтобы обращаться к методам и переменным этого класса.
# В тестах self позволяет использовать assert внутри методов тестов.
# self нужен всегда в методах класса, чтобы обращаться к нему. Без self не сработает!
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
# Аргументы assert(ожидаемый результат, фактический результат, ваше сообщение с пояснением)
# assert ставится в конце, после всех действий

# Условие проверяет, что код запущен напрямую, а не импортирован в другой файл.
# Если код из этого модуля импортировать в другой модуль(2), то он не запустится.
# Подробное про это условие в видео-уроке 'https://www.youtube.com/watch?v=cW_-zGG4ef4'
if __name__ == "__main__":
    # unittest.main() находит все тестовые функции (test_*) и запускает их.
    unittest.main()
    