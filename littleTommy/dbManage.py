"""
Author: Guanduo
Date: 10.31.2016

Database Manager module provides xml db load/edit/update service
"""
from __future__ import print_function
import xml.etree.ElementTree as ET
from os.path import exists

class NotStringExcept(Exception): pass


class dbManager(object):
    """
    Constructor requires a string of path to the .xml file. Typically each xml needs one dbManager
    """
    def __init__(self,xml_file):
        if not isinstance(xml_file,str):
            raise NotStringExcept("Not a string passed to dbManager")
        self.xml_file = xml_file
        self.tree = None
        self.root = None
        self.mem = {}
        self.num_of_element = 0

    """
    Calling Load will load .xml into the memory
    """
    def load(self):
        if not exists(str(self.xml_file)):
            raise IOError("file not exists")
        else:
            self.tree = ET.parse(str(self.xml_file))
            self.root = self.tree.getroot()#root is "items"

            for each in self.root.findall('./'): #each item
                self.num_of_element += 1
                #fixfixfix use 'name' for now. changed to hash later
                key = each.findall('.//name/value')[0].text
                itemInSubDict = {}
                for attr in each.findall('./'): #each attribute is key, value is text
                    print(attr.tag)
                    itemInSubDict[str(attr.tag)] = str(attr.findall('./value')[0].text)
                print(itemInSubDict)
                self.mem[str(key)]=itemInSubDict

    """
    return the number of product items loaded
    """
    def get_num(self):
        print (str(self.num_of_element)+"")
        return self.num_of_element

                
    def debug_print(self):

        print(self.mem)

if __name__ == "__main__":

    db = dbManager('supremeSpider_products.xml')
    print ("YES!")
    db.load()
    db.get_num()
    db.debug_print()
