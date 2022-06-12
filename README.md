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
- Doesn't explicity rule out the definite spots of yellow letters when you have ruled out the spots it's not in
