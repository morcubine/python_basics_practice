# Python OOP Practice

A Colab notebook of 10 exercises practicing class design in Python — attributes, methods, `__init__`, and `__str__` — plus a few scratch cells exploring list behavior and object types along the way.

## What's covered

Each exercise follows the same pattern: a spec (attributes, methods, sample input/output) followed by a class implementation and a test run.

1. **`Book`** — title/author/isbn/available copies; `borrow_book()`, `return_book()`, custom `__str__`
2. **`Rectangle`** — length/width; `area()`, `perimeter()`, custom `__str__`
3. **`Student`** — name/age/grades; `add_grade()`, `average_grade()`, custom `__str__`
4. **`BankAccount`** — account number/holder/balance; `deposit()`, `withdraw()`, custom `__str__`
5. **`Timer`** — hours/minutes/seconds; `tick()` to simulate a second passing with rollover, custom `__str__` with zero-padded `HH:MM:SS`
6. **`ShoppingCart`** — dict of item → quantity; `add_item()`, `remove_item()`, custom `__str__`
7. **`Library`** — list of book titles; `add_book()`, `remove_book()`, `list_books()`, custom `__str__`
8. **`Playlist`** — list of song dicts (title/artist); `add_song()`, `remove_song()`, `get_total_songs()`, custom `__str__`
9. **`ContactBook`** — list of contact dicts (name/email/phone); `add_contact()`, `remove_contact()`, `find_contact()`, custom `__str__`
10. **`WeatherForecast`** — dict of date → weather description; `add_forecast()`, `get_forecast()`, custom `__str__`

**Scratch cells between Exercise 1 and 2** also cover: list creation and `append()`, checking a variable's `type()`, f-strings vs plain strings, list concatenation (`+`) and repetition (`*`), lexicographic list comparison (`>`), and a quick look at `dir(list)` to see available list methods.

## Notes — a few implementations don't fully match their spec yet

Worth revisiting these against the exercise instructions, since the test output doesn't match the "Expected Output" in a few cases:

- **Timer (Ex. 5):** rollover checks use `> 60` instead of `>= 60`, and the minutes rollover is nested inside the seconds rollover — so it only fires in the same tick the seconds roll over, not independently. This one happens to still print the right expected output for the given test case, but the rollover logic isn't quite matching the general spec.
- **ShoppingCart (Ex. 6):** `add_item()` doesn't `return` after setting the initial quantity, so it always adds `quantity` a second time on a brand-new item. `__init__` also takes `item_name`/`quantity` as required constructor args rather than initializing an empty dict as specced, so `ShoppingCart()` alone won't work — the test call uses placeholder args (`cart = ShoppingCart(_, _)`) to work around this.
- **Library (Ex. 7):** `remove_book()` tries `self.book -= 1` instead of `self.book.remove(book)`, which would error on an actual match (not exercised by the test, since the removed title isn't in the list).
- **Playlist (Ex. 8):** songs are stored as `{title, artist}` (a set) instead of `{"title": title, "artist": artist}` (a dict), so the `__str__` format won't match the spec's "Title - Artist" style, and `remove_song(title)` checks membership against whole song-sets rather than titles.
- **ContactBook (Ex. 9):** same set-vs-dict issue as Playlist — contacts are stored as `{name, email, phone}` sets, so `remove_contact()` and `find_contact()` (which check/index by `name`) can't actually match a stored contact, and `find_contact` returns `None` and prints instead of returning the dict as specced.

None of these break the notebook — they just mean a couple of exercises would fail on inputs slightly different from the ones tested here (e.g. actually removing an existing book, or looking up a contact that isn't a fresh dict). Worth a pass to make `Timer`, `ShoppingCart`, `Library`, `Playlist`, and `ContactBook` dict-based/spec-accurate if you want them fully robust.

## Next steps

- Fix the five issues above so each class behaves correctly on inputs beyond the exact sample given
- Try adding a couple of edge-case tests per class (e.g. withdrawing more than the balance in `BankAccount`, removing a song/contact that *is* present) to catch these kinds of bugs earlier
