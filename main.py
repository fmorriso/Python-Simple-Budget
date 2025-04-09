import json
import locale
import os
import sys

from budget_key import BudgetKey

# 1. establish budget
budget = {
    BudgetKey.INCOME: {},
    BudgetKey.EXPENSES: {},
    'totals': {
        BudgetKey.INCOME: 0,
        BudgetKey.EXPENSES: 0
    }
}


def get_dollar_amount():
    while True:
        try:
            dollars = float(input("Enter the dollar amount: "))
            return dollars
        except ValueError:
            print("Please enter a number.")
            continue


def get_type():
    while True:
        response = input('Enter budget type [e]xpense or [i]ncome ').lower()
        if response[:1] == 'e':
            return BudgetKey.EXPENSES
        elif response[:1] == 'i':
            return BudgetKey.INCOME
        else:
            print("Please enter either [e]xpense or [i]ncome")


def get_category():
    while True:
        key = input('Enter the category: ')
        if key is None or len(key) == 0:
            print('Please enter a category')
        else:
            break

    return key.lower()


def ask_yes_no_question(question):
    response = input(question)
    if response is None or len(response) == 0:
        return True
    if response[:1].lower() == 'y':
        return True
    return False


def update_budget(top_key, cat_key, money, ):
    if cat_key not in budget[top_key].keys():
        budget[top_key][cat_key] = 0
    budget[top_key][cat_key] += money

    budget[BudgetKey.TOTALS][top_key] += money


def display_budget():
    # get ready to format dollars and cents correctly
    locale.setlocale(locale.LC_ALL, '')
    for top_key, sub_dict in budget.items():
        print(top_key)
        for cat, dollar_string in sub_dict.items():
            amount = locale.currency(float(dollar_string), grouping = True)
            print(f'\t{cat:<20} {amount:>10}')


def save_budget():
    with open('budget.json', 'w') as f:
        json.dump(budget, f, indent = 4)


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


#### MAIN PROGRAM LOGIC STARTS HERE ####
print(f'Simple Budget program using python version {get_python_version()}')

# if there is a previous budget, pull that in
if os.path.isfile('budget.json'):
    with open('budget.json', 'r') as f:
        budget = json.load(f)

while True:
    # 2. get main user input
    keep_going = ask_yes_no_question("Do you want to enter more budget entries? ")
    if not keep_going:
        break

    type_key = get_type()
    category_key = get_category()
    dollar_amount = get_dollar_amount()

    update_budget(type_key, category_key, dollar_amount)

display_budget()
save_budget()
