import sys
import os
import subprocess
import shutil


pwd = os.getcwd()


def app_exit(args):
    sys.exit(0 if not args else int(args[0]))


app_exit.type = "shell builtin"


def app_echo(args):
    sys.stdout.write(" ".join(args) + "\n")


app_echo.type = "shell builtin"


def app_type(args):
    if args[0] in commands:
        sys.stdout.write(args[0] + " is a " + commands[args[0]].type + "\n")
    elif path := shutil.which(args[0]):
        sys.stdout.write(args[0] + " is " + path + "\n")
    else:
        sys.stdout.write(args[0] + ": not found\n")


app_type.type = "shell builtin"


def app_pwd(args):
    sys.stdout.write(pwd + "\n")


app_pwd.type = "shell builtin"


def app_cd(args):
    global pwd
    if not args:
        return
    if args[0] == "..":
        pwd = os.path.dirname(pwd)
    elif args[0] == "~":
        pwd = os.path.expanduser("~")
    else:
        new_pwd = os.path.join(pwd, args[0])
        if os.path.isdir(new_pwd):
            pwd = new_pwd
        else:
            sys.stdout.write("cd: " + args[0] +
                             ": No such file or directory\n")


app_cd.type = "shell builtin"


def run_executable(command, args):
    try:
        subprocess.run([command] + args)
    except FileNotFoundError:
        sys.stdout.write(command + ": command not found\n")


commands = {
    "exit": app_exit,
    "echo": app_echo,
    "type": app_type,
    "pwd": app_pwd,
    "cd": app_cd
}


def run_command(command, args):
    if command in commands:
        commands[command](args)
    elif path := shutil.which(command):
        run_executable(path, args)
    else:
        sys.stdout.write(command + ": command not found\n")
    sys.stdout.flush()
