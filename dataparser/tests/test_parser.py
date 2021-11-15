import unittest
from dataparser.extract.parser import Parser


class TestParser(unittest.TestCase):

    def test_get_config_data(self):
        """
        Test if we are able to call get_config_data successfully
        :return:  Boolean
        """
        parser = Parser('.')
        config_data = parser.get_config_data()
        self.assertEqual(type(config_data), type({}))

    def test_get_data_files(self):
        """
        Test if we are able to call get_data_files successfully
        :return: Boolean
        """
        parser = Parser('./data')
        files = parser.get_data_files()
        self.assertEqual(len(files), 1)

    def test_load_xml_file(self):
        """
        Test if we are able to call load_xml_file successfully
        :return: Boolean
        """
        parser = Parser('./data')

        #
        xml_handle = parser.load_xml_file('test_data_file.xml')
        self.assertIsNotNone(xml_handle)

    def test_get_objects(self):
        """
        Test if we are able to call get_objects successfully
        :return: Boolean
        """
        args = { 'config_file': './test_config_file.json'}
        parser = Parser('./data', **args)

        data = parser.get_objects()
        self.assertIsNotNone(data)


if __name__ == '__main__':
    unittest.main()
