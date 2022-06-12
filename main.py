from mod import *
from pprint import pprint
import re
import colorama

# Constants:
with open('popular.txt', 'r') as f:
    POPULAR = set(f.read().split())

# Total number of words that wordle can use as an answer. Lenght of words.txt
TOTAL_WORDS = 12947


def pretty_box(game: list):
    print()
    for row in game:
        print(f'{"+---"*5}+')
        for word, results in zip(row[0], row[1]):
            word = word.upper()
            for letter, symbol in zip(word, results):
                match symbol:
                    case '-':
                        print(f'| {letter} ', end='')
                    case 'y':
                        print(
                            f'|{colorama.Back.YELLOW}{colorama.Fore.BLACK} {letter} {colorama.Back.RESET}{colorama.Fore.RESET}', end='')
                    case 'g':
                        print(
                            f'|{colorama.Back.GREEN}{colorama.Fore.BLACK} {letter} {colorama.Back.RESET}{colorama.Fore.RESET}', end='')
                    case _:
                        error(
                            f'Fatal error for result print, symbol = {symbol}')
        # New row
        print('|')
    print(f'{"+---"*5}+\n')


def check():
    while True:
        results = input('Enter results:\n> ').lower().strip()
        if results == 'ggggg':
            # Game finished
            print('\nWell done.')
            print_line()
            exit(0)
        if re.match(r'[-yg]{5}', results):
            # Valid input
            return results
        else:
            print('Please enter valid results')


def get_score(word, assumptions):
    """
    Score the word based on:
    - Has green letter -> += 2
    - Has yellow letter -> += 1

    Each letter: [[may be], [is not]] or when definite: "letter" -> "a"
    """
    score = 0.0
    for letter, ass in zip(word, assumptions):
        if isinstance(ass, str):
            if letter == ass:
                # This has already been figured out. This letter is fine
                # NOTE this can be changed back to a 2, 1 was for testing
                score += 1
                continue
            else:
                # There is no way this word is valid
                return -1
        elif letter in ass[0]:
            # Letter has been spotted as a yellow match
            score += 1
        if letter in ass[1]:
            # Letter has been explicitly proved impossible in this spot
            return -1
    if len(set(word)) == len(word):
        # No duplicates
        score += 1
    if word[0] in POPULAR:
        # Word is commonly used
        score += 0.5
    return [word, score]


def guess(game):
    # Each letter: [[may be], [is not]] or when definite: "letter" -> "a"
    assumptions = [[set(), set()] for _ in range(5)]
    yellows = set()
    for row in game:
        for i, (letter, symbol) in enumerate(zip(*row)):
            match symbol:
                case 'g':
                    assumptions[i] = letter
                case 'y':
                    # Add letter to 'may be' for all but the tile it was yellow for
                    for j in range(5):
                        # Add to yellow spots for all letters but itself, if it hasn't been marked as impossible
                        if j != i and isinstance(assumptions[j], list) and letter not in assumptions[j][1]:
                            assumptions[j][0].add(letter)
                    # This spot will not be the yellow letter
                    yellows.add(letter)
                    assumptions[i][1].add(letter)
                    # This spot has now been prooved to not be the yellow letter
                    if letter in assumptions[i][0]:
                        assumptions[i][0].remove(letter)
                case '-':
                    # Add the letter that is not in the word to list of [is not in word] per letter
                    if letter not in yellows:
                        for j in range(5):
                            if isinstance(assumptions[j], list):
                                assumptions[j][1].add(letter)
                    else:
                        # NOTE, this may not belong in the else statement?
                        # Well it's not in this spot at least
                        assumptions[i][1].add(letter)
                        if letter in assumptions[i][0]:
                            # This has been proved to not be here
                            assumptions[i][0].remove(letter)
                case _:
                    error(
                        f'Fatal error for guess, symbol = {symbol}')

    # Calculate possible answers
    # Answers stored in form of [word, hueristic score]
    possible = []
    possible_amount = 0
    with open('temp.txt', 'r') as f:
        for line in f:
            possible_amount += 1
            word_placement = get_score(line.strip(), assumptions)
            if word_placement != -1:
                possible.append(word_placement)

    rem_percent = ((possible_amount-len(possible))/possible_amount)*100
    total_percent = ((TOTAL_WORDS-len(possible))/TOTAL_WORDS)*100

    print(
        f'Removed {round(rem_percent,2)}% of previous options  ({possible_amount} -> {len(possible)})')
    print(
        f'Total removed {round(total_percent,2)}% of all options ({TOTAL_WORDS} -> {len(possible)})')

    # Update temp
    with open('temp.txt', 'w') as f:
        f.write('\n'.join(x[0] for x in possible))

    # Print top 5 answers, and get user to pick best one?
    print()
    top_5 = sorted(possible, key=lambda x: x[1], reverse=True)[:5]

    # Get user to pick their option
    for i, (word, score) in enumerate(top_5, start=1):
        print(
            f'[ {colorama.Style.BRIGHT}{i}{colorama.Style.RESET_ALL} ] {word}, {score}')

    print()

    if len(top_5) == 1:
        # There is only one choice
        return top_5[0][0]
    elif len(top_5) == 0:
        error('Fatal error, no more possible guesses. Assumptions printed below')
        pprint(assumptions)
        exit(1)
    else:
        while True:
            pick_index = input('What word do you choose?\n> ')
            try:
                pick_index = int(pick_index)
                assert pick_index >= 1 and pick_index <= len(top_5)
            except (AssertionError, ValueError):
                print('Plese enter a valid answer')
                continue
            picked_word = top_5[pick_index-1][0]
            print(
                f'Picked {colorama.Style.BRIGHT}{picked_word}{colorama.Style.RESET_ALL}\n')
            break

    return picked_word


def main() -> None:

    print_line()

    # First guess of the wordle. Toeas was mathematicaly the best starting word
    STARTING_WORD = 'toeas'
    last_guess = STARTING_WORD
    # Game board, [ [word, results] ... ]
    game = [[STARTING_WORD]]

    # Reset temp file
    with open('temp.txt', 'w') as f:
        with open('words.txt', 'r') as r:
            f.write(r.read())

    print('''
⬛️ = "-"
🟨 = "y"
🟩 = "g"
          ''')

    for i in range(5):
        print(
            f'{i+1} | Enter in {colorama.Style.BRIGHT}{last_guess.upper()}{colorama.Style.RESET_ALL}')
        results = check()
        game[i].append(results)
        pretty_box(game)
        last_guess = guess(game)
        game.append([last_guess])

    print_line()


if __name__ == "__main__":
    main()
