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
    key = input('Enter the category')
    return key.lower()

def ask_yes_no_question(question):
    response = input(question)
    if response is None or len(response) == 0:
        return True
    if response[:1].lower() == 'y':
        return True
    return False

#### MAIN PROGRAM STARTS HERE ####
# 1. establish budget
budget = {'income': {}, 'expenses': {}}
total_income = 0
total_expenses = 0


while True:
    # 2. get main user input
    keep_going = ask_yes_no_question("Do you want to enter more budget entries? ")
    if not keep_going:
        break

    type_key = get_type()
    print(type_key)

    category_key = get_category()

    print('Enter dollar amount')
    dollar_amount = get_dollar_amount()
    print(dollar_amount)

    print(type_key, category_key, dollar_amount)
    budget[type_key][category_key] = dollar_amount

    if category_key == 'income':
        total_income += dollar_amount
    else:
        total_expenses += dollar_amount

    print('Budget so far: ' + str(budget))

print('final budget: ' + str(budget))
print(total_income, total_expenses)


def display_budget():
    for top_key, sub_dict in budget.items():
        print(top_key)
        for cat, dollar_string in sub_dict.items():
            amount = float(dollar_string)
            print(' ' * 2 + cat + ' ' + str(amount))




display_budget()