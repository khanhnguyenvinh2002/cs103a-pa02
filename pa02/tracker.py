'''
tracker
'''
from category import Category
from transaction import Transaction

transactions = Transaction('tracker.db')
category = Category('tracker.db')


# here is the menu for the tracker app

MENU = '''
0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu
'''

def proceed(choice):
    ''' proceed the program '''
    if choice=='1':
        cats = category.select_all()
        categories_print(cats)
    elif choice=='2':
        name = input("Category name: ")
        desc = input("Category description: ")
        cat = {'name':name, 'desc':desc}
        category.add(cat)
    elif choice=='3':
        print("Updating category")
        rowid = int(input("rowid: "))
        name = input("Category name: ")
        desc = input("Category description: ")
        cat = {'name':name, 'desc':desc}
        category.update(rowid,cat)
    elif choice == '4':
        item = transactions.select_all()
        transaction_print(item)
    elif choice == '5':
        number_of_items = input("Transaction item number: ")
        amount = input("Transaction amount: ")
        category_transaction = input("Transaction category: ")
        desc = input("Transaction description: ")
        month = input("Transaction month: ")
        year = input("Transaction year: ")
        date = input("What date was this transaction made(mm/dd/yyyy): ")
        item = {
            'number_of_items':number_of_items,
            'amount':amount,
            'category':category_transaction,
            'date':date,
            'month':month,
            'year':year,
            'desc':desc}
        transactions.add(item)
    elif choice == '6':
        row_id = int(input("Provide ID of transaction to be deleted: "))
        print("Deleting Element with ID: "+ str(row_id))
        transactions.delete(row_id)
    elif choice == '7':
        transaction_print(transactions.date())
    elif choice == '8':
        transaction_print(transactions.month())
    elif choice == '9':
        transaction_print(transactions.year())
    elif choice == '10':
        transaction_print(transactions.category())
    elif choice == '11':
        print(MENU)
    else:
        return '0'

    choice = input("Next command: ")
    return choice


def track():
    ''' handle the user's choice '''
    print(MENU)
    choice = input("Next command: ")
    while choice !='0' :
        choice = proceed(choice)
    print('thank you for using')

def transaction_print(items):
    ''' print the transactions '''
    if len(items)==0:
        print('Nothing here')
        return
    print('row_id     item number amount     category   date       description')
    for item in items:
        values = tuple(item.values())
        print("%-10s %-10s %-10d %-10s %-10s %-30s"%
        (values[0], values[1], values[2], values[3], values[4], values[5]))

def category_print(category_item):
    '''
    print a category
    '''
    print("%-3d %-10s %-30s"%(category_item['rowid'],category_item['name'],category_item['desc']))

def categories_print(categories):
    '''
    print categories
    '''
    print("id  name       description    ")

    for category_item in categories:
        category_print(category_item)

track()
