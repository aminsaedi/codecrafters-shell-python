import sys
import os
import subprocess

executables = {}
PATH = os.environ.get("PATH", "")
all_dirs = PATH.split(":")
for dir in all_dirs:
    if os.path.isdir(dir):
        for file in os.listdir(dir):
                if os.access(os.path.join(dir, file), os.X_OK):
                    executables[file] = os.path.join(dir, file)

def app_exit(args):
    sys.exit(0 if not args else int(args[0]))
app_exit.type = "shell builtin"

def app_echo(args):
    sys.stdout.write(" ".join(args) + "\n")
app_echo.type = "shell builtin"

def app_type(args):
    if args[0] in commands:
        sys.stdout.write(args[0] + " is a " + commands[args[0]].type + "\n")
    elif args[0] in executables:
        sys.stdout.write(args[0] + " is " + executables[args[0]] + "\n")
    else:
        sys.stdout.write(args[0] + ": not found\n")
app_type.type = "shell builtin"


def run_executable(command, args):
    try:
        subprocess.run([command] + args)
    except FileNotFoundError:
        sys.stdout.write(command + ": command not found\n")



commands = {
        "exit": app_exit,
        "echo": app_echo,
        "type": app_type
        }

def run_command(command, args):
    if command in commands:
        commands[command](args)
    elif command in executables:
        run_executable(executables[command], args)
    else:
        print(executables.keys())
        sys.stdout.write(command + ": command not found\n")
    sys.stdout.flush()
