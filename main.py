from app.io.input import input_from_console, read_file_builtin, read_file_pandas
from app.io.output import print_to_console, write_to_file


def main():
    # Зчитуємо текст з консолі
    text_from_console = input_from_console()
    print_to_console(f"Введений текст: {text_from_console}")
    write_to_file('data/console_input.txt', text_from_console)

    # Зчитуємо текст з файлу за допомогою built-in функцій
    text_from_file = read_file_builtin('data/sample.txt')
    print_to_console(f"Вміст файлу (built-in): {text_from_file}")
    write_to_file('data/builtin_read_output.txt', text_from_file)

    # Зчитуємо текст з файлу за допомогою pandas
    data_from_file = read_file_pandas('data/sample.csv')
    print_to_console("Вміст файлу (pandas):")
    print_to_console(data_from_file.to_string())
    data_from_file.to_csv('data/pandas_read_output.csv', index=False)


if __name__ == "__main__":
    main()
