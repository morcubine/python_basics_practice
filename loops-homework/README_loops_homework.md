# Python Loops Homework

A Colab notebook of 16 short exercises practicing `for` and `while` loops — printing patterns, iterating with index, filtering and summarizing lists, building strings from lists, and digit manipulation on numbers.

## What's covered

**Basic iteration & counting**
- Printing numbers 1–10 alongside their squares
- Counting down from 30 to 0 in steps of 5 with a `while` loop
- Printing an inverted triangle pattern (`*****` down to `*`)

**Index-aware iteration**
- Printing each item in a list alongside its index (cities)
- Summing only the values at even indexes in a list

**Filtering with conditions**
- Printing numbers outside a given range (`< 10 or > 50`)
- Counting how many numbers in a list are greater than the one immediately before them
- Finding words that contain a doubled letter (nested loop, print each match once)

**Building new lists/strings from existing ones**
- Creating a list of word lengths from a list of words
- Creating an acronym from the first letter of each word in a list

**Digit manipulation on numbers**
- Counting the number of digits in a number
- Finding the sum of a number's digits
- Reversing a number
- Checking whether a number is a palindrome
- Finding the largest digit in a number
- Counting how many digits in a number are even

## Notes

- The first 10 questions work with lists and strings; questions 11–16 shift focus to loops over the digits of a single number, usually via `str(num)`.
- Several solutions lean on Python's string/list built-ins (`str(num)[::-1]`, `sorted(str(num))`) inside the loop rather than pure arithmetic — worth revisiting some of these with `% 10` and `// 10` for digit extraction as an alternative approach.
- The doubled-letter word check (Q10) is the one nested-loop exercise in the set.

## Next steps

- Redo the digit exercises (11–16) using arithmetic (`num % 10`, `num // 10`) instead of converting to a string, for practice with that pattern
- Try the pattern-printing exercise (Q3) with nested loops to build 2D shapes (e.g. a pyramid) instead of a single-line-per-row triangle
