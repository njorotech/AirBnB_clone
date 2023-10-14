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
        class_name = arg_list[0]
        class_obj = globals().get(class_name)
        if class_obj:
            if len(arg_list) < 2:
                print("** instance id missing **")
            else:
                ins_id = arg_list[1]
                data = storage.all()
                for key, value in data.items():
                    if key == class_name + "." + ins_id:
                        obj1 = class_obj(value)
                        print(obj1)
                        return
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split(' ')
        class_name = arg_list[0]
        class_obj = globals().get(class_name)
        if class_obj:
            if len(arg_list) < 2:
                print("** instance id missing **")
            else:
                ins_id = arg_list[1]
                data = storage.all()
                for key, value in data.items():
                    if key == class_name + "." + ins_id:
                        del data[key]
                        storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not not on the class name"""

        obj_list = []
        if not arg:
            data = storage.all()
            """for key, value in data.items():
            #obj_list.append(obj.__str__())
            class_name = value['__class__']
            class_obj = globals().get(class_name)
            obj1 = class_obj(value)
            obj_list.append(str(obj1))
            # print(class_name)
            """
            print('This part is under surveillance')
            return
        arg_list = arg.split(' ')
        class_name = arg_list[0]
        class_obj = globals().get(class_name)
        if class_obj:
            '''data = storage.all()
            for key, value in data.items():
                obj1 = class_obj(value)
                obj_list.append(str(obj1))
            print(obj_list)'''
            print('This part is under surveillance')
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file).
        """

        if not arg:
            print("** class name missing **")
            return

        arg_list = arg.split(' ')
        class_name = arg_list[0]
        class_obj = globals().get(class_name)
        if class_obj:
            if len(arg_list) < 2:
                print("** instance id missing **")
            else:
                ins_id = arg_list[1]
                data = storage.all()
                for key, value in data.items():
                    if key == class_name + "." + ins_id:
                        if len(arg_list) < 3:
                            print("** attribute name missing **")
                        else:
                            if len(arg_list) < 4:
                                print("** value missing **")
                            else:
                                attr_name = arg_list[2]
                                attr_value = arg_list[3]
                                attr_type = type(getattr(value, attr_name))
                                if attr_type is str:
                                    attr_value = str(attr_value)
                                elif attr_type is int:
                                    attr_value = int(attr_value)
                                elif attr_type is float:
                                    attr_value = float(attr_value)
                                setattr(value, attr_name, attr_value)
                                storage.save()
                        return
                print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
