import unittest
from app.io.input import read_file_builtin, read_file_pandas
import pandas as pd
import os


class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        # Створити папку data, якщо її ще нема
        os.makedirs("data", exist_ok=True)

        # Підготовка тестових файлів
        self.text_file = "data/test_sample.txt"
        self.csv_file = "data/test_sample.csv"

        with open(self.text_file, 'w', encoding='utf-8') as f:
            f.write("Тестовий текст для читання.")

        df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [30, 25]})
        df.to_csv(self.csv_file, index=False)

    def tearDown(self):
        # Видалення тестових файлів
        if os.path.exists(self.text_file):
            os.remove(self.text_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_read_file_builtin(self):
        content = read_file_builtin(self.text_file)
        self.assertEqual(content, "Тестовий текст для читання.")

    def test_read_file_pandas_columns(self):
        df = read_file_pandas(self.csv_file)
        self.assertListEqual(list(df.columns), ["Name", "Age"])

    def test_read_file_pandas_data(self):
        df = read_file_pandas(self.csv_file)
        self.assertEqual(df.iloc[0]["Name"], "Alice")
        self.assertEqual(df.iloc[1]["Age"], 25)


if __name__ == '__main__':
    unittest.main()
