#!/usr/bin/env python3
"""Import modules"""
import cmd, sys

class HBNBCommand(cmd.Cmd):
    # ---- Creation de class-----

    # ------ Change of the prompt for '(hbnb)'----
    prompt = '(hbnb)'

    # ------Method 'emptyline'----
    def emptyline(self):
        pass
    
    # ------Method 'quit' and man quit----
    def do_quit(self, line):
        sys.exit(1)
    
    def help_quit(self):
        print("Syntax: quit")
        print("--Quit command to exit the program")
    
    # ------Method 'EOF'----
    def do_EOF(self, line):
        "Exit ctrl + C"
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
