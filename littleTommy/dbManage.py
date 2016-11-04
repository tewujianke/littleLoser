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
class KeyNotExistinMem(Exception): pass

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
        if not exists('./db/'+str(self.db_file_path)):
            raise IOError("file not exists")
        else:
            database_read_from_disk = shelve.open('./db/'+str(self.db_file_path))
            self.mem = dict(database_read_from_disk)
            database_read_from_disk.close()

        self.num_of_element = len(self.mem)
    def get_num(self):
        """
        Return the number of product items loaded
        """
        print (str(self.num_of_element)+"")
        return self.num_of_element

    def modify(self,product_key,attribute,value):
        """
        Modify a product's attribute. MUST BE CALLED IN A TRY BLOCK!!
        e.g. dbmanage.modify("supreme tom-style shoe",'price','$20')
        This method only updates memory. Call update to write to disk
        """

        if not str(product_key) in self.mem:
            print( "oopps")
            raise KeyError("Modifying a product though dbManage %s: %s key not found in mem" %(self.instance_name,str(product_key)))

        if not attribute in self.mem[product_key]:
            raise KeyError("Modifying an invalid attribute: %s"%attribute)
        print("passed check")
        
        if(self.dbgmode):
            print('dbg: old value is %s'%self.mem[product_key][attribute])

        self.mem[product_key][attribute] = value

        if(self.dbgmode):
            print('dbg: new value is %s'%self.mem[product_key][attribute])

    def update(self):
        """
        Write current dict from the memory to the disk
        Must be called in a TRY block except IOError
        """
        if not exists('./db/'+str(self.db_file_path)):
            raise IOError("file not exists %s"%self.db_file_path)
        else:
            import os
            #don't want .db postfix
            os.rename('./db/'+self.db_file_path,'./db/'+'old_'+str(self.db_file_path[:-3])+'.db')
        new_db = shelve.open('./db/'+self.db_file_path[:-3])

        #need deep copy instead of pointers
        for key in self.mem.keys():
            new_db[key] = self.mem[key]

        new_db.close()

    def __contains__(self,something):
        """
        used in 'in' context. Check whether a key exsited in memory
        e.g. if "supreme Shoe" in db:
        """
        if str(something) in self.mem:
     
            return True
        else:
          
            return False

    def __getitem__(self,key):
        """
        Return a dict of found item. Raise exception if key is not found
        e.g. item_dict = db["Supreme Some Shoes"]
        """
        if not str(key) in self.mem:
            raise KeyNotExistinMem(" Can't find '%s' in db"%str(key))

        return self.mem[str(key)]
    
    def generate_html(self):
        """
        Generate a webpage containing all loaded items from .xml (or modified tree) Place holder. Not working now. Need future work
        """
        pass #place holder now
    
    def debug_print(self):
        """
        Debug only. Exhaustively print out the loaded info
        """
        print(dict(self.mem))


if __name__ == "__main__":

    db = dbManager('supreme_db','supremeSpider_products.db','1')
    print ("YES!")
    db.load_db()
    print(db.get_num())
    db.debug_print()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n\n\n\n")
    try:

        db.modify('Supreme: Reversible Hooded Puffy Jacket','price',u'$900982')
    except KeyError as K:
        print ("ended with exception: %s" % K)

    try:
        db.update()
    except Exception as K:
        print("IOERROR EXCP: %s"%K)

    newdb = dbManager('new_db','supremeSpider_products.db','1')
        
    newdb.load_db()
    newdb.debug_print()

    try:
        print("started")
        if 'Supreme: Reversible Hooded Puffy Jacket' in newdb:
            print("Found")
            print(newdb['Supreme: Reversible Hooded Puffy Jacket'])
        else:
            print('not found')
            
    except Exception as K:
        print ("Exception collected: %s" % K)
