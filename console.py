#!/usr/bin/python3

import cmd
import sys
import models
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ ---- Creation de class-----"""

    """------ Change of the prompt for '(hbnb)'----"""
    prompt = '(hbnb)'

    """------Method 'emptyline'----""" 
    def emptyline(self):
        pass
    
    """ ------Method 'quit' and man quit----"""
    def do_quit(self,line):
        sys.exit(1)
    
    def help_quit(self):
        print("Syntax: quit")
        print("--Quit command to exit the program")
    
    """ ------Method 'EOF'----"""
    def do_EOF(self,line):
        "Exit ctrl + C"
        return True
    
    def do_destroy(self, args):
        """
        Method that delete an instance
        """
        divide_clas = args.split()
        if not args:
            print("** class name missing **")   
        elif divide_clas[0] not in self.lista_clas:
            print("** class doesn't exist **")
        elif len(divide_clas) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = models.storage.all()

            if key in instances:
                del instances[key]
                models.storage.save()
            else:
                print("** no instance found **")
    

if __name__ == '__main__':
    HBNBCommand().cmdloop()