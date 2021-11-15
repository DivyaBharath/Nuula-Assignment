import os
import errno
from dataparser.utils import get_logger
import xlsxwriter


class GenerateXLSX:
    """
    User class for generating XLSX file for a given data structure
    """

    def __init__(self, filepath):
        self.log = get_logger()
        self.log.info("Initiating the 'Parser' object .. ")
        self.xlsx_name = filepath

        if os.path.exists(filepath):
            raise FileExistsError(errno.EEXIST, os.strerror(errno.EEXIST), filepath)

        # Create a workbook and add a worksheet.
        self.workbook = xlsxwriter.Workbook(filepath)
        self.worksheet = self.workbook.add_worksheet()

    @staticmethod
    def get_object_schema(data_sample):
        """
        :param data_sample: Key-value pair of data
        :return: headers : Array of column headers
        """
        headers = data_sample.keys()
        return headers

    def add_data_table(self, data):
        """

        :param data: Data Structure that needs to be written to XLSX File
        Expects data to be a Dictionary of Object-types; Each key 'object-type' having value as a list of dictionaries
        :return: Boolean
        """
        end_row = 1

        for object_type in data:
            data_sample = data.get(object_type)[0]
            object_schema = self.get_object_schema(data_sample)

            start_col = 3
            end_col = start_col + len(object_schema) - 1
            start_row = 2 + end_row
            end_row = start_row + len(data.get(object_type))

            table_data = []
            for datarow in data.get(object_type):
                print(datarow)
                row = []
                for header in object_schema:
                    row.append(datarow.get(header))
                    table_data.append(row)

            columns = []
            for header in object_schema:
                columns.append({'header': header})

            self.worksheet.add_table(start_row, start_col, end_row, end_col, {'data': table_data,
                                                                              'columns': columns
                                                                              })
        self.workbook.close()
