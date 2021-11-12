#!/usr/bin/env python3


import cmd
import sys

class HBNBCommand(cmd.Cmd):
    # ---- Creation de class-----
    # ------ Change of the prompt for '(hbnb)'----
    prompt = '(hbnb)'

    Data_Type = [BaseModel = 'BaseModel']

    # ------Method 'Create'----
    def do_create (self, line):
        if not len(line)
    
    def do_show (self, line):
        if len(sys.line) > 1:
            print("** class name missing **")
        elif sys.line[1] not in self.Data_Type:
            print("** class doesn't exist **")
        elif len(sys.line) > 2:
            print("** instance id missing **")
        else: 
            if sys.line[2] not in id.instance:
                print("** no instance found **")
        

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
