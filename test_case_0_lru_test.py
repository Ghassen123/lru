import unittest
from main import create_lru, format_input


class TesLRU(unittest.TestCase):
    def test_capacity_2(self):
        """
        Run use case 1
        :return:
        """
        self.assertEqual(
            create_lru(2, ['SET', 'SET', 'GET', 'SET', 'GET', 'SET', 'GET'], ['5', '10', '5', '15', '10', '5', '5'],
                       ['11', '22', '1', '33', '1', '55', '1']), [11, -1, 55], "Should be [11, -1, 55]")

    def test_capacity_4(self):
        """
        Run use case 2
        :return:
        """
        self.assertEqual(
            create_lru(4, ['SET', 'SET', 'GET', 'SET', 'GET', 'SET', 'GET'], ['5', '10', '5', '15', '10', '5', '5'],
                       ['11', '22', '1', '33', '1', '55', '1']), [11, 22, 55], "result [11, 22, 55]")

    def test_capacity_1(self):
        """
        Run use case 3
        :return:
        """
        self.assertEqual(
            create_lru(1, ['SET', 'SET', 'GET', 'SET', 'GET', 'SET', 'GET', 'GET', 'GET', 'GET'],
                       [1, 2, 1, 3, 2, 4, 1, 1, 3, 4],
                       [1, 2, 1, 3, 1, 4, 1, 1, 3, 4]), [-1, -1, -1, -1, -1, 4],
            "result should be equal to [-1, -1, -1, -1, -1, 4]")

    def test_capacity_0(self):
        """
        Run use case 4
        :return:
        """
        self.assertRaises(AttributeError, lambda: create_lru(0, ['SET', 'SET', 'GET', 'SET', 'GET', 'SET', 'GET'],
                                                             ['5', '10', '5', '15', '10', '5', '5'],
                                                             ['11', '22', '1', '33', '1', '55', '1']))

    def test_format_input_file(self):
        """
        Run use case file exists
        :return:
        """
        self.assertEqual(format_input("input_files/input.txt"), (
            2, ["SET", "SET", "GET", "SET", "GET", "SET", "GET"], ['5', '10', '5', '15', '10', '5', '5'],
            ['11', '22', '1', '33', '1', '55', '1']))

    def test_format_input_file_1(self):
        """
        Run use case input file not found
        :return:
        """
        self.assertRaises(FileNotFoundError, lambda: format_input("input_files/input_not_exist.txt"))


    def test_format_input_file_2(self):
        """
        Run use case input unstructured data input file
        :return:
        """
        self.assertRaises(AttributeError, lambda: format_input("input_files/unstructured_input_data.txt"))

if __name__ == '__main__':
    """
    create unittest use cases 
    """
    unittest.main()
