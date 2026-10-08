# Space Turtle Chomp

The code, pictures and sounds for **Jess's Coding Adventure: Space Turtle Chomp**,
a story book that teaches you to build a Python game step by step.

Chomp (the green turtle) and Crunch (the pink turtle) race around space eating
biscuits. You steer Chomp with the arrow keys, and whoever eats the most biscuits
in 60 seconds wins.

## What you need

- Python 3 from [python.org](https://www.python.org/downloads/). It comes with
  **IDLE**, the program the book uses to write and run the code.
- All the files below, saved in **one folder** (the book calls it `TurtleGame`).
  The game looks for the pictures and sounds in the same folder as the `.py`
  file, so if they're somewhere else the game can't find them.

## The files

| File | What it is |
| --- | --- |
| `turtlegame.py` | The finished game. |
| `turtlegame1.py` … `turtlegame13.py` | The game as it grows, one save per step in the book (see below). |
| `space-bg.gif` | The space background picture. |
| `chomp.mp3`, `bounce.mp3` | Sounds for a Mac. |
| `chomp.wav`, `bounce.wav` | The same sounds for Windows. |

Each numbered file contains every module up to that point:

| File | Ends with | Chapter |
| --- | --- | --- |
| `turtlegame1.py` | Module 1: Importing the Python libraries | 1 |
| `turtlegame2.py` | Module 3: A border around the game world | 2 |
| `turtlegame3.py` | Module 4: Chomp the green space turtle | 3 |
| `turtlegame4.py` | Module 5: Crunch the pink space turtle | 4 |
| `turtlegame5.py` | Module 6: Keeping score | 4 |
| `turtlegame6.py` | Module 7: The great biscuit hunt | 5 |
| `turtlegame7.py` | Module 8: A helping hand (keyboard controls) | 6 |
| `turtlegame8.py` | Module 9: Pushing the limits (the game timer) | 7 |
| `turtlegame9.py` | Module 10: Bounce, bounce, bounce | 8 |
| `turtlegame10.py` | Module 11: Food flight | 9 |
| `turtlegame11.py` | Module 12: Crash, bang, oomph for Chomp | 10 |
| `turtlegame12.py` | Module 13: Crash, bang, oomph for Crunch | 10 |
| `turtlegame13.py` | Module 14: And the winner is… (the whole game) | 11 |

## Stuck?

If your code won't run and you can't find the mistake, open the file for the step
you're on, copy its code and paste it into IDLE in place of yours. Then choose
**Run → Run Module**.

The most common mistakes:

- **Curly quotes.** Python only understands straight quotes, `'` and `"`. Quotes
  copied from a document or ebook are often curly (‘ ’ “ ”).
- **Indentation.** Lines inside an `if`, `for`, `while` or `def` must start with
  4 spaces, and every line in the same block needs the same number.
- **Spelling.** Python uses the American spellings `color` and `center`, and
  capital letters matter: `Turtle` and `turtle` are different.
- **Background picture name.** These files use `space-bg.gif`. If your copy of the
  book says `game-bg.gif`, rename the picture or change line 12 to match.

## Sounds

Sounds play on Windows (using the `.wav` files) and on a Mac (using the `.mp3`
files). On other computers, such as Linux or a Chromebook, the game works without
sound.

## Make it your own

- Change the colours on the lines that say `color(...)`.
- Make your own 600 × 600 background, save it as a `.gif` and put its name on line 12.
- Change the time limit: `10*6` on line 63 means 60 seconds.
