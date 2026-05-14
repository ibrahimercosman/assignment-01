# Shared dataset — Assignment 1 (Programming Paradigms)
expenses = [
    {"date": "2024-01-05", "category": "Food", "amount": 42.50, "description": "Groceries"},
    {"date": "2024-01-07", "category": "Transport", "amount": 15.00, "description": "Bus pass"},
    {"date": "2024-01-09", "category": "Entertainment", "amount": 60.00, "description": "Concert ticket"},
    {"date": "2024-01-10", "category": "Food", "amount": 8.75, "description": "Coffee & snack"},
    {"date": "2024-01-12", "category": "Utilities", "amount": 120.00, "description": "Electricity bill"},
    {"date": "2024-01-14", "category": "Food", "amount": 55.20, "description": "Restaurant dinner"},
    {"date": "2024-01-15", "category": "Transport", "amount": 30.00, "description": "Taxi"},
    {"date": "2024-01-17", "category": "Entertainment", "amount": 14.99, "description": "Streaming subscription"},
    {"date": "2024-01-20", "category": "Food", "amount": 38.00, "description": "Groceries"},
    {"date": "2024-01-22", "category": "Utilities", "amount": 45.00, "description": "Internet bill"},
    {"date": "2024-01-25", "category": "Transport", "amount": 22.00, "description": "Train ticket"},
    {"date": "2024-01-28", "category": "Entertainment", "amount": 25.00, "description": "Book"},
]


def get_total(expense_list):
    """Return the sum of all expense amounts.

    Args:
        expense_list (list): Expense dicts with an ``amount`` key.

    Returns:
        float: Total of all ``amount`` values.
    """
    total = 0.0
    for e in expense_list:
        total += e["amount"]
    return total


def get_count(expense_list):
    """Return how many expense records are in the list.

    Args:
        expense_list (list): Expense dicts.

    Returns:
        int: Number of records.
    """
    n = 0
    for _ in expense_list:
        n += 1
    return n


def get_category_totals(expense_list):
    """Map each category name to its total spending.

    Args:
        expense_list (list): Expense dicts with ``category`` and ``amount``.

    Returns:
        dict: ``{category: total_amount}``.
    """
    totals = {}
    for e in expense_list:
        cat = e["category"]
        if cat in totals:
            totals[cat] += e["amount"]
        else:
            totals[cat] = e["amount"]
    return totals


def get_most_expensive(expense_list):
    """Return the expense dict with the highest amount (no ``max()`` built-in).

    Args:
        expense_list (list): Non-empty list of expense dicts.

    Returns:
        dict: The expense entry with the largest ``amount``.
    """
    best = expense_list[0]
    for e in expense_list:
        if e["amount"] > best["amount"]:
            best = e
    return best


def get_least_expensive(expense_list):
    """Return the expense dict with the lowest amount (no ``min()`` built-in).

    Args:
        expense_list (list): Non-empty list of expense dicts.

    Returns:
        dict: The expense entry with the smallest ``amount``.
    """
    worst = expense_list[0]
    for e in expense_list:
        if e["amount"] < worst["amount"]:
            worst = e
    return worst


def get_average(expense_list):
    """Return the average expense amount as a float.

    Args:
        expense_list (list): Non-empty list of expense dicts.

    Returns:
        float: Mean of all ``amount`` values.
    """
    return get_total(expense_list) / get_count(expense_list)


def get_above_average(expense_list):
    """Return expense dicts whose amount is strictly above the average.

    Preserves the same dict objects from ``expense_list`` (order preserved).

    Args:
        expense_list (list): Expense dicts.

    Returns:
        list: Subset of ``expense_list`` references with ``amount > average``.
    """
    avg = get_average(expense_list)
    out = []
    for e in expense_list:
        if e["amount"] > avg:
            out.append(e)
    return out


def print_summary(expense_list):
    """Print a full summary report using the helper functions above.

    Produces the same output as Parts B1–B4 combined.

    Args:
        expense_list (list): Expense dicts.
    """
    print(f"Total expenses: {get_total(expense_list):.2f}")
    print(f"Number of records: {get_count(expense_list)}")

    print("Category breakdown:")
    totals = get_category_totals(expense_list)
    for cname in sorted(totals.keys()):
        print(f"  {cname} : {totals[cname]:.2f}")

    most = get_most_expensive(expense_list)
    least = get_least_expensive(expense_list)
    print(
        f'Most expensive : {most["description"]} '
        f'({most["category"]}) - {most["amount"]:.2f}'
    )
    print(
        f'Least expensive: {least["description"]} '
        f'({least["category"]}) - {least["amount"]:.2f}'
    )

    avg = get_average(expense_list)
    print(f"Average expense: {avg:.2f}")
    print("Expenses above average:")
    for e in get_above_average(expense_list):
        print(f"- {e['description']} ({e['amount']:.2f})")


if __name__ == "__main__":
    print_summary(expenses)