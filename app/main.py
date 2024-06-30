import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input_str = input()

    match input_str:
        case "exit":
            sys.exit(0)
        case _:
            sys.stdout.write(input_str + ": command not found\n")

    sys.stdout.flush()

if __name__ == "__main__":
    main()
