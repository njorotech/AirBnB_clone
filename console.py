#!/usr/bin/python3
"""Module for the AirBnB_clone console"""

import cmd
from models.base_model import BaseModel
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """A class for the AirBnB_clone console"""

    prompt = '(hbnb) '

    def emptyline(self):
        """An empty line + ENTER shouldn't execute anything"""

        return False

    def do_EOF(self, line):
        """Exit the program on receiving end-of-file marker"""

        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""

        return True

    def postloop(self):
        """Print a new line after exiting the program"""

        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it
        and prints the id
        """
        
        if not arg:
            print("** class name missing **")
            return

        class_name = globals().get(arg)
        if class_name:
            new_inst = class_name()
            new_inst.save()
            print(new_inst.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """

        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split(' ')
        class_name = globals().get(arg_list[0])
        if class_name:
            if len(arg_list) < 2:
                print("** instance id missing **")
            else:
                ins_id = arg_list[1]
                data = storage.get_objects()
                for key in data:
                    if data[key]["id"] == ins_id:
                        data_list = data.split('}{')
                        obj1 = BaseModel(data)
                        print(obj1)
                        return
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
