def print_line(n=80):
    """Line printer"""
    print(f"\033[31m\033[1m{'-'*n}\033[0m")


def error(errorMessage: str):
    """Give error"""
    LINE_LEN = len(max(errorMessage.split("\n"), key=len))
    print_line(LINE_LEN)
    print(
        f"\u001b[31m\u001b[1mERROR ❌\n\u001b[0m\u001b[31m{errorMessage}\u001b[0m")
    print_line(LINE_LEN)


def warning(warningMessage: str):
    """Give warning"""
    LINE_LEN = len(max(warningMessage.split("\n"), key=len))
    print_line(LINE_LEN)
    print(
        f"\u001b[33m\u001b[1mWARNING ⚠️\n\u001b[0m\u001b[33m{warningMessage}\u001b[0m")
    print_line(LINE_LEN)


def get_input(message, warning="Please enter a value") -> str:
    """Soley just to force an input from user"""
    while True:
        userInput = input(message)
        if userInput:
            return userInput
        else:
            error(warning)
