import sys
from .commands import run_command


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input_str = input()
    splitted = input_str.split()
    command = splitted[0]
    args = splitted[1:]

    run_command(command, args)

if __name__ == "__main__":
    while True:
        main()
