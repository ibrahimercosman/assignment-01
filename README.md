# Assignment 01 — My Personal Expense Tracker

## What this project is

This is a small school project. I work with a fixed list of expenses in Python. Each expense has a date, a category, an amount of money, and a short description. The program prints a simple text report. It shows the total money spent, how many expenses I have, totals per category, the cheapest and most expensive item, the average amount, and a list of items above the average.

I wrote the same idea in three different styles. That was the main goal of the course work.

## How to run the code

Open a terminal. Go to the `assignment-01` folder. Then run:

```bash
python part_b_imperative.py
python part_c_procedural.py
python part_d_functional.py
```

Here is what each file does in simple words:

- **Part B (`part_b_imperative.py`)** — This version prints the full report with loops and `if` statements. I do not use helper functions here. I also do not use `sum`, `max`, `min`, `map`, or `filter`, because the assignment asked for a very basic style.
- **Part C (`part_c_procedural.py`)** — This version prints the **same** report, but the work is inside functions like `get_total` and `print_summary`. It is easier to read in small pieces.
- **Part D (`part_d_functional.py`)** — This version checks that some “functional” functions give the same answers as Part C. Then it prints each expense as one long text line with pipes (`|`).

**Part A** is not Python code. It is a short text file called `part_a_paradigms.md`. I explain what programming style four small code examples show.

When Part D finishes the checks, you should see something like this:

```text
All assertions passed.

Formatted expenses:
2024-01-05 | Food | Groceries | $42.50
```

## Comparing the three styles 

**1. Imperative (Part B)**  
This style was easy for me when the list was small. I could follow the steps like a recipe: start numbers at zero, go through the list, add values, print. If the list had **100,000** rows, the program would still work in theory, but one long file is harder to read and harder to fix when there is a bug. I would need more comments and more care.

**2. Procedural (Part C)**  
I liked this style because each function has one job. I can test one part of the idea without running everything. With **100,000** rows, the computer still has to look at each row about the same number of times, but the code is easier to organize. If I want to change only the “above average” part, I can go to one function.

**3. Functional style (Part D)**  
Here I use tools like `sum`, `map`, `filter`, and short `lambda` functions. The code can be shorter. Sometimes short code is very clear; sometimes it is harder for a beginner (like me) to read. With **100,000** rows, the speed is mostly similar to the other versions in Python, but very long chains of `map`/`filter` can be harder to debug if something is wrong.

## One thing I would do differently

If I started again, I would compare the printed output from Part B and Part C **early**, line by line. Small text differences are easy to miss, but they matter when Part D uses checks (`assert`) that compare results. Fixing format problems at the end takes more time than fixing them at the start.