# Wordle Solver

An algoirithmic brute force solver for Wordle

This attempt ingores a few aspects:

- Relvance of letters in guess
  - Guesses gives you suggestions with rare letters like x & y, rather than priorising vowels and common letters
    - This is why you pick from 'top 5'
- Not playing on hard mode
  - The guesses adhere to hard mode, all previous hints must be used in next answer
  - This means the bot can have trouble gaining yellow letters if the board is mostly green
- Optimisations
  - This is mostly brute force
- Quantity of single letters
  - If you get a yellow and a grey on the same letter, the guesses are now flawed. They will exclude the yellow letter
  - This may have been fixed, have not tested yet.
    - *Tests indicate this may be resolved*
  