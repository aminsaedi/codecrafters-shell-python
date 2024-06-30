import sys
import os

def app_exit(args):
    sys.exit(0 if not args else int(args[0]))
app_exit.type = "shell builtin"

def app_echo(args):
    sys.stdout.write(" ".join(args) + "\n")
app_echo.type = "shell builtin"

def app_type(args):
    print("app_type")
    executables = {}
    try:
        PATH = os.environ.get("PATH", "")
        all_dirs = PATH.split(":")
        for dir in all_dirs:
            for file in os.listdir(dir):
                executables[file] = os.path.join(dir, file)
    except:
        pass

    print(args)

    if args[0] in commands:
        print("commands")
        sys.stdout.write(args[0] + " is a " + commands[args[0]].type + "\n")
    elif args[0] in executables:
        print("executables")
        sys.stdout.write(args[0] + " is " + executables[args[0]] + "\n")
    else:
        print("not found")
        sys.stdout.write(args[0] + ": not found\n")
app_type.type = "shell builtin"


commands = {
        "exit": app_exit,
        "echo": app_echo,
        "type": app_type
        }

def run_command(command, args):
    if command in commands:
        commands[command](args)
    else:
        sys.stdout.write(command + ": command not found\n")
    sys.stdout.flush()
