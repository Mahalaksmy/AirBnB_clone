#!/usr/bin/python3

import cmd
import sys
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    # ---- Creation de class-----

    # ------ Change of the prompt for '(hbnb)'----
    prompt = '(hbnb)'
    lista_clas = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']
 
    # ------Method 'emptyline'----
    def emptyline(self):
        pass
    
    # ------Method 'quit' and man quit----
    def do_quit(self,line):
        sys.exit(1)
    
    def help_quit(self):
        print("Syntax: quit")
        print("--Quit command to exit the program")
    
    # ------Method 'EOF'----
    def do_EOF(self,line):
        "Exit ctrl + C"
        return True

    """ Aquí nuevo código """
    def do_create(self, args):
        """" create Method """

        if not args:
            print("** class name missing **")
        elif args not in self.lista_clas:
            print("** class doesn't exist **")
        else:
            new_clas = BaseModel()
            new_clas.save()
            print(new_clas.id)

    def do_show(self, args):
        """
        Method that show the
        representation of the instance
        """
        cls_arg = args.split()
        dict_obj = storage.all()
        if not args:
            print("** class name missing **")
        #elif nombre de la clase :   
        elif cls_arg[0] not in self.lista_clas:
            print("** class doesn't exist **")
        elif len(cls_arg) == 1:
            print("** instance id missing **")
        elif (cls_arg[0] + "." + cls_arg[1]) not in dict_obj:
            print("** no instance found **")
        else:
            print(dict_obj["{}.{}".format(cls_arg[0], cls_arg[1])])

    def do_destroy(self, args):
        """
        Method that show the
        representation of the instance
        """
        cls_arg = args.split()
        dict_obj = storage.all()
        if not args:
            print("** class name missing **")
        #elif nombre de la clase :   
        elif cls_arg[0] not in self.lista_clas:
            print("** class doesn't exist **")
        elif len(cls_arg) == 1:
            print("** instance id missing **")
        elif (cls_arg[0] + "." + cls_arg[1]) not in dict_obj:
            print("** no instance found **")
        
        else:
            del dict_obj["{}.{}".format(cls_arg[0], cls_arg[1])]
            storage.save()

    def do_all(self, args):
        """ methos """
        if not args or (args in self.lista_clas):
            #dic_all = []
            for key in storage.all():
               #dic_all[key] = storage.all()
               print(storage.all()[key])
               #print(dic_all)
            #print(dic_all)

        elif args not in self.lista_clas:
            print("** class doesn't exist **")

        """else:
            print("** class doesn't exist **")"""

if __name__ == '__main__':
    HBNBCommand().cmdloop()