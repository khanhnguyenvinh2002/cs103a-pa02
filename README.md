# cs103a-pa02
 
================================================= test session starts =================================================
platform win32 -- Python 3.9.2, pytest-7.1.1, pluggy-1.0.0
rootdir: C:\Users\Admin\Documents\GitHub\cs103a-pa02\pa02, configfile: pytest.ini
collected 7 items

test_category.py ....                                                                                            [ 57%]
test_transaction.py ...                                                                                          [100%]

================================================== 7 passed in 0.91s ==================================================

C:\Users\Admin\Documents\GitHub\cs103a-pa02\pa02>python tracker.py

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

Next command: 1
id  name       description
1   1          1
2   2          2
3   3          3
4   4          4
Next command: 2
Category name: 4
Category description: 4
Next command: 3
Updating category
rowid: 5
Category name: 5
Category description: 5
Next command: 1
id  name       description
1   1          1
2   2          2
3   3          3
4   4          4
5   5          5
Next command: 4


row_id     item number amount     category   date       description
1          1          1          1          1          1
Next command: 5
Transaction item number: 2
Transaction amount: 2
Transaction category: 2
Transaction description: 2
Transaction month: 2
Transaction year: 2
What date was this transaction made(mm/dd/yyyy): 2
Next command: 4


row_id     item number amount     category   date       description
1          1          1          1          1          1
2          2          2          2          2          2
Next command: 6
Provide ID of transaction to be deleted: 2
Deleting Element with ID: 2
Next command: 4


row_id     item number amount     category   date       description
1          1          1          1          1          1
Next command: 7


row_id     item number amount     category   date       description
1          1          1          1          1          1
Next command: 8


row_id     item number amount     category   date       description
1          1          1          1          1          1
Next command: 9


row_id     item number amount     category   date       description
1          1          1          1          1          1
Next command: 5
Transaction item number: 2
Transaction amount: 2
Transaction category: 2
Transaction description: 2
Transaction month: 2
Transaction year: 2
What date was this transaction made(mm/dd/yyyy): 2
Next command: 7


row_id     item number amount     category   date       description
1          1          1          1          1          1
2          2          2          2          2          2
Next command: 8


row_id     item number amount     category   date       description
1          1          1          1          1          1
2          2          2          2          2          2
Next command: 9


row_id     item number amount     category   date       description
1          1          1          1          1          1
2          2          2          2          2          2
Next command: 0
thank you for using