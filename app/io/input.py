def input_from_console():
    """
    Функція для зчитування тексту, введеного користувачем через консоль.
    """
    return input("Введіть текст: ")


def read_file_builtin(path):
    """
    Функція для зчитування вмісту файлу за допомогою вбудованих можливостей Python.

    :param path: шлях до файлу
    :return: вміст файлу як рядок
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def read_file_pandas(path):
    """
    Функція для зчитування вмісту файлу за допомогою бібліотеки pandas.

    :param path: шлях до файлу
    :return: вміст файлу як DataFrame
    """
    import pandas as pd
    return pd.read_csv(path)
