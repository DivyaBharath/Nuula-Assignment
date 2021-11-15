import os
import xml.etree.ElementTree as ET
from pprint import pprint

class DataParser:
  def __init__(self, path):
    """ 
    """

    self.data_path = path
    self.objects_data = { 'Errors': [], 'Rules': [], 'Messages': [] }

  def get_files(self):
    """ Gets the list of available files in the data directory """
    self.files = os.listdir(self.data_path)

    self.tags_to_parse = [ 'Nuula', 'DataExtract900jer' ]
    from pprint import pprint
    pprint(self.files)

  def read_file(self):
    """ Read File """
    
    for pfile in self.files:
        #
        pfilepath = '/'.join([self.data_path, pfile])
        print(f"Attempting to read the path {pfilepath}")

        # Parse the file
        tree = ET.parse(pfilepath)
        root = tree.getroot()

        # DO NOT Proceed if Root element is not 'Data'
        if root.tag != "Data":
          next

        for child in list(root):
          if child.tag in self.tags_to_parse:

            #print(f"Tag Name : {child.tag}")

            for subchild in list(child):
              #.getchildren():
              #print(f"SubChild : {subchild.tag}")

              #
              if subchild.tag in ['Errors','Rules','Messages']:
                for errortag in list(subchild):
                  self.objects_data[subchild.tag].append(errortag.attrib)


  def print_data(self):
    
    #
    print("- - - - - - - - - - OUTPUT - - - - - - - - - - - - -")
    for entry in self.objects_data:
      print(entry)
      pprint(self.objects_data.get(entry)[0])

if __name__ == '__main__':
    parser = DataParser('data')

    #
    parser.get_files()

    parser.read_file()

    parser.print_data()
