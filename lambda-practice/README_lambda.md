# Python Lambda & Comprehension Practice

A Colab notebook of short exercises practicing `lambda` functions, `sorted()` with custom keys, filtering, list comprehensions, and dictionary-based string/frequency problems.

## What's covered

**Lambda basics**
- Writing simple one-line functions with `lambda` instead of `def` (add, larger of two numbers, absolute difference)
- Conditional logic inside a lambda (even/odd, positive/negative/zero, pass/fail based on marks, number between 10–50, divisible by 3)
- String operations via lambda (length, uppercase, last character, longer of two strings, starts with a vowel, is a single alphabet character)

**Sorting with `sorted()` + `key=`**
- Sorting a list of names alphabetically, case-insensitively (`key=lambda x: x.lower()`)
- Sorting a list of dicts by a specific field — students by marks (descending), products by price (ascending), words by length, employees by age
- Sorting tuples by the length of their first element, and dicts by the length of a string field (`name`)
- Sorting integers by the sum of their digits
- Multi-step pipelines that combine filter → sort → extract in sequence (e.g. Gmail addresses: filter, lowercase, dedupe, sort; students above 80: filter, sort by marks descending, pull out names only; words: dedupe, keep ≥5 letters, title-case, sort alphabetically)

**Filtering**
- Using a loop + `if` to collect items matching a condition (students who passed, words over 5 characters)
- Rewriting the same filter as a **list comprehension** for comparison — this is a good habit, since it shows you the "long way" and the "short way" side by side
- Additional filter exercises: keep only perfect squares, keep filenames ending in `.py`, keep words where the first and last character match, remove empty strings, double all odd numbers and discard results over 50

**Transforming data**
- Converting a list of names to uppercase, both with a loop and with a list comprehension
- Extracting just one field (name) from a list of dicts into its own list
- Squaring a list of numbers, converting integers to strings, rounding floats to 2 decimal places, summing/multiplying corresponding elements across two lists, converting minutes to rounded hours — each shown as both a loop and a comprehension

**Strings & dictionaries (frequency/counting problems)**
- Character frequency count using a dictionary (e.g. counting letters in `"mississippi"`)
- Word frequency count from a sentence split into words
- Finding the first non-repeating character in a string
- Removing duplicate characters while preserving order
- Finding the longest word in a sentence without using `max()`
- Finding the largest number in a list without using `max()`
- Finding all palindrome words in a sentence
- String compression (collapsing consecutive repeated characters into char+count form, e.g. `"aaabbccccdaaa"` → `"a3b2c4d1a3"`)
- Anagram check between two strings without using `sorted()`
- Moving all zeros in a list to the end while preserving the order of other elements

## Notes

- Several exercises show both the loop version and the comprehension version of the same task — useful for seeing how the two map onto each other before comprehensions start feeling natural.
- The recurring pattern of `sorted(data, key=lambda x: x['field'])` here is the same one used throughout the JSON/API practice repo, so it's worth noticing that these two sets of exercises reinforce each other.
- The frequency/counting section is a step up in complexity from the earlier lambda and comprehension exercises — it's mostly plain loops with dictionaries, building toward writing helper functions instead of one-liners.

## Next steps

- Try combining a filter + comprehension in one line (e.g. names of students with marks ≥ 40, uppercased)
- Practice `map()` and `filter()` directly (mentioned but not yet used in this notebook)
- Try rewriting the frequency-counting exercises using `collections.Counter` for comparison against the manual dictionary approach
