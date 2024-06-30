import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input_str = input()
    splitted = input_str.split()
    command = splitted[0]
    args = splitted[1:]

    match command:
        case "exit":
            sys.exit(0 if not args else int(args[0]))
        case "echo":
            sys.stdout.write(" ".join(args) + "\n")
        case _:
            sys.stdout.write(input_str + ": command not found\n")

    sys.stdout.flush()

if __name__ == "__main__":
    while True:
        main()
