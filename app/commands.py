import sys

def app_exit(args):
    sys.exit(0 if not args else int(args[0]))
app_exit.type = "shell builtin"

def app_echo(args):
    sys.stdout.write(" ".join(args) + "\n")
app_echo.type = "shell builtin"

def app_type(args):
    if args[0] in commands:
        sys.stdout.write(args[0] + " is a " + commands[args[0]].type + "\n")
    else:
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
