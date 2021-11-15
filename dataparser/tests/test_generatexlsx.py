import unittest
import os
from dataparser.extract.generatexlsx import GenerateXLSX


class TestGenerateXLSX(unittest.TestCase):
    def test_get_object_schema(self):
        """
        test if we are able to call get_object_schema successfully
        :return: Boolean
        """
        headers = GenerateXLSX.get_object_schema({ 'col-a': 1, 'col-b': 2})

        self.assertEqual(len(headers), 2)

    def test_add_data_table(self):
        """
        test if we are able to call add_data_table successfully
        :return: Boolean
        """
        data = {'messages': [{'col-a': 1, 'col-b': 2},
                             {'col-a': 3, 'col-b': 4}]}

        file_writer = GenerateXLSX('./testfile.xlsx')

        file_writer.add_data_table(data)

        self.assertGreater(os.path.getsize('./testfile.xlsx'), 0, msg="Non empty file")


if __name__ == '__main__':
    unittest.main()
