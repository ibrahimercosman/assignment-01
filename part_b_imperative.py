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


if __name__ == "__main__":
    # B1 — Total and count (no sum(), no len() as primary count: use accumulators)
    total_expenses = 0.0
    number_of_records = 0
    for expense in expenses:
        total_expenses += expense["amount"]
        number_of_records += 1

    print(f"Total expenses: {total_expenses:.2f}")
    print(f"Number of records: {number_of_records}")

    # B2 — Category breakdown (dictionary, print sorted alphabetically by category)
    category_totals = {} # empty dictionary to store the category totals
    for expense in expenses:
        cat = expense["category"]
        if cat in category_totals:
            category_totals[cat] += expense["amount"]
        else:
            category_totals[cat] = expense["amount"]

    print("Category breakdown:")
    category_names = []
    for name in category_totals:
        category_names.append(name)

    unique_cats = 0
    for _ in category_totals:
        unique_cats += 1

    # Sort alphabetically without sorted(): nested-loop swap
    i = 0
    while i < unique_cats:
        j = i + 1
        while j < unique_cats:
            if category_names[i] > category_names[j]:
                tmp = category_names[i]
                category_names[i] = category_names[j]
                category_names[j] = tmp
            j += 1
        i += 1

    k = 0
    while k < unique_cats:
        cname = category_names[k]
        amt = category_totals[cname]
        print(f"  {cname} : {amt:.2f}")
        k += 1

    # B3 — Most and least expensive (no max/min; loop + tracking variables)
    most_expensive = expenses[0]
    least_expensive = expenses[0]
    for expense in expenses:
        if expense["amount"] > most_expensive["amount"]:
            most_expensive = expense
        if expense["amount"] < least_expensive["amount"]:
            least_expensive = expense

    print(
        f'Most expensive : {most_expensive["description"]} '
        f'({most_expensive["category"]}) - {most_expensive["amount"]:.2f}'
    )
    print(
        f'Least expensive: {least_expensive["description"]} '
        f'({least_expensive["category"]}) - {least_expensive["amount"]:.2f}'
    )

    # B4 — Average (first loop), then strictly above average (second loop)
    sum_for_avg = 0.0
    count_for_avg = 0
    for expense in expenses:
        sum_for_avg += expense["amount"]
        count_for_avg += 1

    average_expense = sum_for_avg / count_for_avg
    print(f"Average expense: {average_expense:.2f}")
    print("Expenses above average:")
    for expense in expenses:
        if expense["amount"] > average_expense:
            print(f"- {expense['description']} ({expense['amount']:.2f})")