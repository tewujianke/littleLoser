"""
Author: Guanduo
Date: 10.31.2016

Database Manager module provides  db load/edit/update service
"""
from __future__ import print_function

from os.path import exists
import shelve
import logging

class NotStringExcept(Exception): pass


class dbManager(object):

    def __init__(self,name,db_file_path,dbgmode=0):
        """
        Constructor requires a string of path to the .db file. Typically each .db needs one dbManager.
        """
        if not isinstance(db_file_path,str):
            raise NotStringExcept("Not a string passed to dbManager")
        self.db_file_path = db_file_path
        self.mem = None
        self.num_of_element = None
        self.instance_name = name
        self.dbgmode=dbgmode

    def load_db(self):
        """
        Calling Load will load .db into the memory
        Must be called first before any other operations!
        """
        if not exists(str(self.db_file_path)):
            raise IOError("file not exists")
        else:
            self.mem = shelve.open(str(self.db_file_path))

        self.num_of_element = len(self.mem)
    def get_num(self):
        """
        Return the number of product items loaded
        """
        print (str(self.num_of_element)+"")
        return self.num_of_element

    def modify(self,product_key,attribute,value):
        """
        Modify a product's attribute.
        e.g. dbmanage.modify("supreme tom-style shoe",'price','$20')
        """
        if not str(product_key) in self.mem:
            raise KeyError("Modifying a product though dbManage %s: %s key not found in mem" %(self.instance_name,str(product_key)))

        if not attribute in self.mem[product_key]:
            raise KeyError("Modifying an invalid attribute: %s"%attribute)

        if(self.dbgmode):
            print('dbg: old value is %s'%self.mem[product_key][attribute])

        self.mem[product_key][attribute] = value

        if(self.dbgmode):
            print('dbg: new value is %s'%self.mem[product_key][attribute])

    def generate_html(self):
        """
        Generate a webpage containing all loaded items from .xml (or modified tree)
        """
        pass #place holder now
    
    def debug_print(self):
        """
        Debug only. Exhaustively print out the loaded info
        """
        print(dict(self.mem))

    def __del__(self):
        self.mem.close()

if __name__ == "__main__":

    db = dbManager('supreme_db','supremeSpider_products.db')
    print ("YES!")
    db.load_db()
    print(db.get_num())
    db.debug_print()

