#!/usr/bin/python3
"""
Command Loop
"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def isfloat(num):
    """
    Checks if s is a float
    """
    try:
        float(num)
        return True
    except ValueError:
        return False


def str2dict(s):
    """
    Attempts to converts a str 's' to dict
    """
    d = None
    try:
        d = eval(s)
    except Exception:
        return d
    if isinstance(d, dict):
        return d
    else:
        return None


def commaninja(s):
    """
    Remove commas from the begining or end
    the string s
    """
    if s[0] == ',':
        s = s[1:]
    if s[-1] == ',':
        s = s[:-1]
    return s.strip()


class HBNBCommand(cmd.Cmd):
    """
    The Command interpreter for the
    AirBnB Clone Project
    """
    prompt = "(hbnb)"
    allowed_classes = {"BaseModel": BaseModel, "User": User,
                       "State": State, "Amenity": Amenity,
                       "Place": Place, "Review": Review}

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
        print()
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

    def do_count(self, line):
        """
        Counts the Number of instances saved
        of a given object
        """
        args = split(line)
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args[0] in self.allowed_classes.keys():
                all_objs = storage.all()
                printlist = [str(value)
                             for key, value in all_objs.items()
                             if key.startswith(args[0])]
                print(len(printlist))
            else:
                print("** class doesn't exist **")

    def help_count(self):
        """
        Help for create
        """
        print("Usage:\ncount <class name>\n")

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints
        the id
        """
        args = split(line)
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
        args = split(line)
        if len(args) == 0:
            all_objs = storage.all()
            printlist = [str(value) for _, value in all_objs.items()]
            print(printlist)
        else:
            if args[0] in self.allowed_classes.keys():
                all_objs = storage.all()
                printlist = [str(value)
                             for key, value in all_objs.items()
                             if key.startswith(args[0])]
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
        args = [commaninja(x) for x in split(line)]
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
                            nl = line[line.find(args[1]) + len(args[1]):]
                            sf = nl.find("{")
                            sl = nl.rfind("}")
                            d = str2dict(nl[sf:sl+1])
                            if d is not None:
                                for key, value in d.items():
                                    obj.__dict__[key] = value
                            elif len(args) < 4:
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
        print("Usage:\nupdate <class name> <id> <attribute name>" +
              "\"<attribute value>\"")

    def onecmd(self, line):
        ''' define $ as a shortcut for the dollar command
            and ask for confirmation when the interpreter exit'''
        ms = re.match("([^.\\s]+)\\.([^\\(]+)\\((.*)\\)", line)
        if ms is not None:
            tp = ms.groups()
            args = tp[2].split(", ")
            line = tp[1] + " " + tp[0] + " " + ", ".join(args)
        r = super(HBNBCommand, self).onecmd(line)
        return r


if __name__ == '__main__':
    HBNBCommand().cmdloop()
