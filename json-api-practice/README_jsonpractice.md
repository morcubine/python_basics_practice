# JSON & API Practice (Python)

Small, self-contained exercises for practicing HTTP requests and JSON handling in Python using the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) test API and the `requests` library.

Each question is solved independently in `json_practise.py` (most are commented out so they don't all run at once — uncomment one block at a time to test it).

## Exercises

| # | Task | Concepts practiced |
|---|------|---------------------|
| 1 | GET a single user, print name/username/email if `status_code == 200` | Basic GET request, status code checking, `.json()` |
| 2 | GET a user, print nested address fields (street, suite, city, zipcode) | Accessing nested dicts |
| 3 | GET all users, ask for a city, print matching names | Looping over a list of dicts, user input, filtering |
| 4 | GET all users, filter emails ending in `.biz` | String methods (`.endswith()`), building a filtered list |
| 5 | Find the user with the longest name | Tracking a running max while looping |
| 6 | Sort users by length of name | `sorted()` with a `lambda` key |
| 7 | Ask for a username, print the full matching dict or "not found" | `for...else`, early exit with `break` |
| 8 | Count unique company names | `set()` for deduplication |
| 9 | Find the user with the highest ID | Running max pattern (numeric) |
| 10 | Build a new list of simplified dicts (name, city, company) | Reshaping/transforming data |
| 11 | GET all posts, count posts by `userId == 5` | Filtering + counting |
| 12 | Find the post with the longest title | Running max pattern (string length) |
| 13 | Find posts with `'est'` in the title | Substring search |
| 14 | POST a new post (title/body/userId), check `status_code == 201` | Sending data with POST, confirming creation |

## Notes

- All requests use the free [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake API — no auth needed.
- Question 14 uses `requests.post()`; JSONPlaceholder doesn't actually persist data, but it fakes a `201` response with an assigned ID, useful for practicing POST handling.
- Common pattern throughout: `requests.get(URL)` → check `.status_code` → `.json()` → work with the resulting dict/list.

## Next steps

- Try combining exercises (e.g. filter by city *and* sort by name length)
- Add error handling for network failures (`try/except`) rather than just checking status codes
