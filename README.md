# Wordle Solver

An algoirithmic brute force solver for [Wordle](https://www.nytimes.com/games/wordle/index.html)

**Requires**: `Python 3.10.x`, and packages in `requirements.txt`

---

## Installation

<!-- Keep code level with +1 indentation -->

1. Clone repo

   ```cmd
   git clone https://github.com/Sandwich1699975/Wordle-Solver.git
   ```

1. Enter directory

   ```cmd
   cd Wordle-Solver/
   ```

1. Install packages

   ```cmd
   pip3.10 install -r requirements.txt
   ```

1. Run `main`

   ```cmd
   python3.10 main.py
   ```

## Demo

Example run with no color:

```txt
--------------------------------------------------------------------------------

⬛️ = "-"
🟨 = "y"
🟩 = "g"

| Choice | Word  | Score |
| ------ | ----- | ----- |
| 1      | Tests | 4.5   | 

          
1 | Enter in TOEAS
Enter results:
> yyy--

+---+---+---+---+---+
| T | O | E | A | S |
+---+---+---+---+---+

Removed 80.3% of previous options  (12947 -> 2551)
Total removed 80.3% of all options (12947 -> 2551)

[ 1 ] quote, 4.0
[ 2 ] flote, 4.0
[ 3 ] bento, 4.0
[ 4 ] helot, 4.0
[ 5 ] retox, 4.0

What word do you choose?
> 1
Picked quote

2 | Enter in QUOTE
Enter results:
> yyg--

+---+---+---+---+---+
| T | O | E | A | S |
+---+---+---+---+---+
| Q | U | O | T | E |
+---+---+---+---+---+

Removed 92.59% of previous options  (2551 -> 189)
Total removed 98.54% of all options (12947 -> 189)

[ 1 ] glout, 4.0
[ 2 ] grout, 4.0
[ 3 ] knout, 4.0
[ 4 ] crout, 4.0
[ 5 ] clout, 4.0

What word do you choose?
> 5
Picked clout

3 | Enter in CLOUT
Enter results:
> ggggg

Well done.
--------------------------------------------------------------------------------
```

---

## Limitations

This attempt ingores a few aspects:

- Relvance of letters in guess
  - Guesses gives you suggestions with rare letters like x & y, rather than priorising vowels and common letters
    - This is why you pick from 'top 5'
- Not playing on hard mode
  - The guesses adhere to hard mode, all previous hints must be used in next answer
  - This means the bot can have trouble gaining yellow letters if the board is mostly discovered
- Optimisations
  - This is mostly brute force. A more efficient method may be beneficial
- Doesn't explicity rule out the definite spots of yellow letters when you have ruled out the spots it's not in - See [#1](https://github.com/Sandwich1699975/Wordle-Solver/issues/1)
