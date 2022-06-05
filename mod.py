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


def passed(passedText: str):
    """Give warning"""
    LINE_LEN = len(max(passedText.split("\n")))
    print_line(LINE_LEN)
    print(
        f"\u001b[32m\u001b[1mPASSED ✅\n\u001b[0m\u001b[32m{passedText}\u001b[0m")
    print_line(LINE_LEN)


def get_input(message, warning="Please enter a value") -> str:
    """Soley just to force an input from user"""
    while True:
        userInput = input(message)
        if userInput:
            return userInput
        else:
            error(warning)


def get_answer(COND1="y", COND2="n") -> bool:
    """Get user's responce based on given conditions::

        COND1 == True
        COND2 == False

    i.e. Function will return `True` if user selects `COND1`"""

    while True:
        print(f"({COND1}/{COND2})")
        # Upper is used in case they accidentally input a capital
        USER_CHOICE = input("> ").upper()
        if USER_CHOICE == COND1.upper() or USER_CHOICE == COND2.upper():
            if USER_CHOICE == COND1.upper():
                return True
            else:
                return False
        else:
            error(
                f"Incorrect input.\n"
                f"Enter \"{COND1}\" or \"{COND2}\"")


def search_guess(GUESS: str, OPTIONS: list) -> str:
    """
        From https://www.datacamp.com/community/tutorials/fuzzy-string-python
        levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t

        I've altered the function to create a ratio for every item in `OPTIONS`
        and store it in a list of tuples. Tuple contains the ratio of `s` (User
        input) to each recipe name in `OPTIONS` E.g. (0.34343,'Pancakes')
        Then the function returns the best match with its ratio (confidence)

        `0.0 <= Ratio <= 1.0`

        OUTPUT = `(0.98765, 'Match')`

    """

    ratios = []
    for t in OPTIONS:

        # Initialize matrix of zeros
        rows = len(GUESS)+1
        cols = len(t)+1
        distance = [[0 for x in range(cols)] for y in range(rows)]

        # Populate matrix of zeros with the indeces of each character of both strings
        for i in range(1, rows):
            for k in range(1, cols):
                distance[i][0] = i
                distance[0][k] = k

        # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions
        for col in range(1, cols):
            for row in range(1, rows):
                if GUESS[row-1] == t[col-1]:
                    # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
                    cost = 0
                else:
                    # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                    # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                    cost = 2
                distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                         # Cost of insertions
                                         distance[row][col-1] + 1,
                                         distance[row-1][col-1] + cost)
        ratios.append(
            ((((len(GUESS)+len(t)) - distance[row][col]) / (len(GUESS)+len(t))), t))

    return max(ratios)


def multi_line_input() -> str:
    while True:
        print("Click enter to go to new line\n"
              "2 consecutive enters will submit the text\n")
        lines = []
        while True:
            line = input("> ")
            if line:
                lines.append(line)
            else:
                break
        userInputJoin = '\n'.join(lines)
        if userInputJoin:
            break
    return userInputJoin
