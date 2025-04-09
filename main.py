# 1. establish budget
budget = {
    'income': {},
    'expenses': {},
    'totals': {
        'income': 0,
        'expenses': 0}
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
        response = input('Enter type budget type [e]xpense or [i]ncome ')
        if response[:1].lower() == 'e':
            return 'expenses'
        elif response[:1].lower() == 'i':
            return 'income'
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


def update_budget(top_key, cat_key, money,):
    if cat_key not in budget[top_key].keys():
        budget[top_key][cat_key] = 0
    budget[top_key][cat_key] += money

    budget['totals'][top_key] += money


def display_budget():
    for top_key, sub_dict in budget.items():
        print(top_key)
        for cat, dollar_string in sub_dict.items():
            amount = float(dollar_string)
            print(' ' * 2 + cat + ' ' + str(amount))


#### MAIN PROGRAM LOGIC STARTS HERE ####

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
