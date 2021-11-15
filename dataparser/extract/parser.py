import os
import errno
import json
import xml.etree.ElementTree as ET
from dataparser.utils import get_logger
from dataparser.extract.generatexlsx import GenerateXLSX


class Parser:
    """
    User class for extracting objects from XML files and generating XLSX file with the objects data
    """

    def __init__(self, data_path, **kwargs):
        """
        :param data_path: Data Path where XML files are available
        """

        self.log = get_logger()

        self.log.info("Initiating the 'Parser' object .. ")

        if not os.path.exists(data_path):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), data_path)

        self.data_path = data_path

        self.config_file = '../configs/app.json'
        if 'config_file' in kwargs:
            self.config_file = kwargs.get('config_file')

        self.config = self.get_config_data()

        self.data_files = self.get_data_files()

        self.log.info("Object initialized successfully")

    def get_config_data(self):
        """
        :return: Loads configuration JSON file and returns the data structure
        """
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), self.config_file)

        with open(self.config_file, 'r') as json_file:
            config_data = json.load(json_file)

        return config_data

    def get_data_files(self):
        """
        :return: List of data files (XML)
        """
        _files = []
        for _file in os.listdir(self.data_path):

            # Ensure we pick up only XML files
            if _file.endswith(".xml"):
                _files.append(_file)

        return _files

    def load_xml_file(self, pfile):
        """
        :param pfile: XML File to load for extracting the objects
        :return:
        """

        pfilepath = "/".join([self.data_path, pfile])
        self.log.info(f"Attempting to read the path {pfilepath}")

        try:
            # Parse the file
            tree = ET.parse(pfilepath)
        except Exception as e:
            raise f"Problem loading the XML file {pfilepath} " + str(e)

        return tree

    def get_objects(self):
        """
        :return: objects_data: Dictionary with the list of objects extracted from XML files
        """

        objects_data = {}
        for pfile in self.data_files:

            xmltree = self.load_xml_file(pfile)

            root = xmltree.getroot()

            for object_pattern in self.config.get('object_patterns'):

                index_root = root

                pattern_index = 0
                user_pattern_tags = object_pattern.split(".")

                current_tag = user_pattern_tags[pattern_index]
                self.log.debug(f"Current Tag : {current_tag}")

                if root.tag != current_tag:
                    self.log.debug(
                        f"File {pfile} is not in expected structure. Ignoring it"
                    )
                    self.log.debug(
                        f"Expected to find {current_tag} but found {root.tag}"
                    )
                    next

                pattern_index += 1
                parent_node_found = True

                while pattern_index < len(user_pattern_tags):

                    self.log.debug(
                        f"Current Tag[1] : {user_pattern_tags[pattern_index]}"
                    )

                    matched_element = False
                    for child in list(index_root):

                        if child.tag == user_pattern_tags[pattern_index]:
                            matched_element = True
                            index_root = child
                            break

                    self.log.debug(f"MATCHED ELEMENT FLAG : {matched_element}")
                    if not matched_element:
                        parent_node_found = False
                        self.log.debug(
                            f"File {pfile} is not in expected structure. Ignoring it"
                        )
                        self.log.debug(
                            f"Did not find expected element: {user_pattern_tags[pattern_index]}"
                        )
                        break

                    pattern_index += 1

                # Parse data only if we found the expected parent node
                if parent_node_found:
                    for element in list(index_root):

                        if not object_pattern in objects_data:
                            objects_data[object_pattern] = []
                        objects_data[object_pattern].append(element.attrib)

        return objects_data


if __name__ == "__main__":
    parser = Parser("../../data")

    data = parser.get_objects()

    xlsx_path = '/Users/kiranmasani/Downloads/output.xlsx'
    xlsx_writer = GenerateXLSX(xlsx_path)
    xlsx_writer.add_data_table(data)
