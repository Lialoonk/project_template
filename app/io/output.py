def print_to_console(text):
    """
    Функція для виводу тексту у консоль.

    :param text: текст для виводу
    """
    print(text)


def write_to_file(path, text):
    """
    Функція для запису тексту у файл за допомогою вбудованих можливостей Python.

    :param path: шлях до файлу
    :param text: текст для запису
    """
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
