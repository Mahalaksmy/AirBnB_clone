#!/usr/bin/python3
"""Create of the class HBNBCommand"""
import cmd
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
    """---- Creation de class-----"""

    """------ Change of the prompt for '(hbnb)'----"""
    prompt = '(hbnb)'

    lista_clas = ['BaseModel', 'User', 'Place',
                  'State', 'City', 'Amenity', 'Review']

    """------Method 'emptyline'----"""
    def emptyline(self):
        """Emptyline"""
        pass

    """------Method 'quit' and man quit----"""
    def do_quit(self, line):
        """Exit of the program"""
        return True

    """------Method 'EOF'----"""
    def do_EOF(self, line):
        """Exit ctrl + C"""
        return True

    """ ------Method Create New Instance------"""
    def do_create(self, args):
        """" Method Create New Instance """

        if not args:
            print("** class name missing **")
        elif args not in self.lista_clas:
            print("** class doesn't exist **")
        else:
            new_clas = BaseModel()
            new_clas.save()
            print(new_clas.id)

    """ ------Method Show------"""
    def do_show(self, args):
        """
        Method that show the
        representation of the instance
        """
        cls_arg = args.split()
        dict_obj = storage.all()
        if not args:
            print("** class name missing **")
        elif cls_arg[0] not in self.lista_clas:
            print("** class doesn't exist **")
        elif len(cls_arg) == 1:
            print("** instance id missing **")
        elif (cls_arg[0] + "." + cls_arg[1]) not in dict_obj:
            print("** no instance found **")
        else:
            print(dict_obj["{}.{}".format(cls_arg[0], cls_arg[1])])

    """ ------Method Destroy------"""
    def do_destroy(self, args):
        """
        Method that show the
        representation of the instance
        """
        cls_arg = args.split()
        dict_obj = storage.all()
        if not args:
            print("** class name missing **")
        elif cls_arg[0] not in self.lista_clas:
            print("** class doesn't exist **")
        elif len(cls_arg) == 1:
            print("** instance id missing **")
        elif (cls_arg[0] + "." + cls_arg[1]) not in dict_obj:
            print("** no instance found **")

        else:
            del dict_obj["{}.{}".format(cls_arg[0], cls_arg[1])]
            storage.save()

    """ ------Method All------"""
    def do_all(self, args):
        """ Method All, priny all instance """
        if not args or (args in self.lista_clas):

            for key in storage.all():
                print(storage.all()[key])
        elif args not in self.lista_clas:
            print("** class doesn't exist **")

    def do_User(self, arg):
        """Method for print all instance with user """
        if arg == '.all()':
            self.do_all('User')

    """ ------Help Commands------"""

    def help_quit(self):
        """ Help of the command quit"""
        print("Quit command to exit the program\n")

    def help_create(self):
        """ Help of the command create"""
        print("Create command to create new instances\n")

    def help_show(self):
        """ Help of the command create"""
        print("Show command to show info of the instance\n")

    def help_destroy(self):
        """ Help of the command Destroy"""
        print("Destroy command to delete a instance\n")

    def help_all(self):
        """ Help of the command All"""
        print("All command to show all instance\n")

    def help_User(self):
        """ Help of the command User"""
        print("User command to print info of the instances\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
