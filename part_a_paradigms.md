## Snippet 1

**Paradigm**: Imperative programming

**Explanation**: This code uses a `for` loop and changes a variable step by step (`total += ...`). You tell the computer exactly what to do in order. At the end it prints the result. That is a simple, direct style with clear commands and changing state.

## Snippet 2

**Paradigm**: Procedural programming

**Explanation**: Here the work is split into small functions with names, like `get_total` and `get_by_category`. You call the functions instead of writing one long block. The functions still use loops inside, but the main program is easier to read because each part has a name and a job.

## Snippet 3

**Paradigm**: Mixed style (imperative + functional parts)

**Explanation**: First there is a loop that fills a dictionary. That part is imperative because you update the dictionary many times. Then the code uses `max(..., key=lambda ...)` to pick the best category. That part is more functional because you use a built-in tool and a small `lambda` function instead of writing another loop by hand.

## Snippet 4

**Paradigm**: Functional programming (with Python tools)

**Explanation**: This code uses `sum` with a generator, and also `map` and `filter` with `lambda`. You work with the list in a short, expression-based way. You do not write a big loop with an index. The style focuses on transforming data with built-in helpers.