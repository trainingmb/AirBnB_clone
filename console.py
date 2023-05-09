#!/usr/bin/python3
"""
Command Loop
"""
import cmd
from shlex import split
from models.base_model import BaseModel
from models import storage


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


class HBNBCommand(cmd.Cmd):
    """
    The Command interpreter for the
    AirBnB Clone Project
    """
    prompt = "(hbnb)"
    allowed_classes = {"BaseModel":BaseModel}

    def do_quit(self, line):
        """
        Quit the program
        """
        return True

    def help_quit(self):
        """
        Help String for quit cmd
        """
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        """
        Quit the program
        """
        return True

    def help_EOF(self):
        """
        Help String for quit cmd
        """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """
        Do nothing on empty line
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in self.allowed_classes.keys():
                newobj = self.allowed_classes[args[0]]()
                newobj.save()
                print(newobj.id)
            else:
                print("** class doesn't exist **")

    def help_create(self):
        """
        Help for create
        """
        print("Usage:\ncreate <class name>\n")

    def do_show(self, line):
        """
        Prints the string representation of an
        instance based on the class name and id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in self.allowed_classes.keys():
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    all_objs = storage.all()
                    key = args[0] + "." + args[1]
                    if key in all_objs.keys():
                        print(str(all_objs[key]))
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_show(self):
        """
        Help for show
        """
        print("Usage:\nshow <class name> <id>")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class
        name and id (save the change into the
        JSON file)
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in self.allowed_classes.keys():
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    all_objs = storage.all()
                    key = args[0] + "." + args[1]
                    if key in all_objs.keys():
                        all_objs.pop(key)
                        storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_destroy(self):
        """
        Help for show
        """
        print("Usage:\ndestroy <class name> <id>")

    def do_all(self, line):
        """
        Prints all string representation of all
        instances based or not on the class name
        """
        args = line.split()
        if len(args) == 0:
            all_objs = storage.all()
            printlist = [str(value) for _, value in all_objs.items()]
            print(printlist)
        else:
            if args[0] in self.allowed_classes.keys():
                all_objs = storage.all()
                printlist = [str(value) for key, value in all_objs.items() if key.startswith(args[0])]
                print(printlist)
            else:
                print("** class doesn't exist **")

    def help_all(self):
        """
        Help for show
        """
        print("Usage:\nall [classname]")

    def do_update(self, line):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        (save the change into the JSON file).
        """
        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in self.allowed_classes.keys():
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    all_objs = storage.all()
                    key = args[0] + "." + args[1]
                    if key in all_objs.keys():
                        if len(args) < 3:
                            print("** attribute name missing **")
                        else:
                            obj = all_objs[key]
                            if len(args) < 4:
                                print("** value missing **")
                            else:
                                if args[3].isdigit():
                                    obj.__dict__[args[2]] = int(args[3])
                                elif isfloat(args[3]):
                                    obj.__dict__[args[2]] = float(args[3])
                                else:
                                    obj.__dict__[args[2]] = args[3]
                                obj.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def help_update(self):
        """
        Help for show
        """
        print("Usage:\naupdate <class name> <id> <attribute name>"+
              "\"<attribute value>\"")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
