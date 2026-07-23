# Python OOP Practice

A Colab notebook of 10 exercises practicing class design in Python — attributes, methods, `__init__`, and `__str__` — plus a few scratch cells exploring list behavior and object types along the way.

## What's covered

Each exercise follows the same pattern: a spec (attributes, methods, sample input/output) followed by a class implementation and a test run.

1. **`Book`** — title/author/isbn/available copies; `borrow_book()`, `return_book()`, custom `__str__`
2. **`Rectangle`** — length/width; `area()`, `perimeter()`, custom `__str__`
3. **`Student`** — name/age/grades; `add_grade()`, `average_grade()`, custom `__str__`
4. **`BankAccount`** — account number/holder/balance; `deposit()`, `withdraw()`, custom `__str__`
5. **`Timer`** — hours/minutes/seconds; `tick()` simulates a second passing, with independent rollover checks for seconds→minutes and minutes→hours (`>= 60` on each, checked separately rather than nested), custom `__str__` with zero-padded `HH:MM:SS`
6. **`ShoppingCart`** — dict of item → quantity; `add_item()`, `remove_item()` (drops the item entirely once quantity hits 0), custom `__str__` built by joining formatted key/value pairs
7. **`Library`** — list of book titles; `add_book()`, `remove_book()` (removes the matching title or prints "Book Not Found"), `list_books()`, custom `__str__` joining the list
8. **`Playlist`** — list of song dicts (title/artist); `add_song()`, `remove_song()` (loops with a `for...else` to detect a missing title), `get_total_songs()`, custom `__str__`
9. **`ContactBook`** — list of contact dicts (name/email/phone); `add_contact()`, `remove_contact()` and `find_contact()` (both loop with `for...else`, comparing `name` by exact match and removing the matched dict itself), custom `__str__`
10. **`WeatherForecast`** — dict of date → weather description; `add_forecast()`, `get_forecast()`, custom `__str__`

**Scratch cells between Exercise 1 and 2** also cover: list creation and `append()`, checking a variable's `type()`, f-strings vs plain strings, list concatenation (`+`) and repetition (`*`), lexicographic list comparison (`>`), and a quick look at `dir(list)` to see available list methods.

## Notes

All 10 exercises are now fully working and match their specs. The fix pattern that came up across a few of them is worth remembering for future exercises: when removing an item from a list of dicts by a field value, loop through with `for item in self.list`, compare the field with `==` (not `in`, which does a substring/membership check), and call `.remove(item)` on the matched object itself — not on the search key you were given. That exact shape fixed `remove_song` (Playlist), `remove_contact` (ContactBook), and `remove_book` (Library).

The `Timer` fix followed a different pattern: two independent rollover checks (seconds→minutes, minutes→hours) rather than nesting the second inside the first, so a rollover in one unit isn't dependent on a rollover also happening in the other during the same tick.

## Next steps

- Nothing outstanding on this notebook — all classes match their specs and pass their sample tests
- If you want to stress-test further: try removing an item that's genuinely present (rather than one that was never added) in `Library`/`ContactBook`/`Playlist`, and try a `Timer` case where minutes roll over without seconds also rolling over in the same tick (e.g. `Timer(0, 59, 0)` ticking 60 times)
