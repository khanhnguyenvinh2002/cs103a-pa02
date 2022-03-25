# cs103a-pa02

We were finally able to run script with another computer, here is the result: 

Script started on Fri Mar 25 19:23:14 2022
[1m[7m%[27m[1m[0m                                                                                                                
 

[0m[27m[24m[J(base) NguyenThiKimThuy1@nguyens-air pa02 % [K[?2004hppytest[?2004l

[1m============================================== test session starts ==============================================[0m
platform darwin -- Python 3.8.8, pytest-7.1.0, pluggy-0.13.1
rootdir: /Users/NguyenThiKimThuy1/Desktop/Projects/InfinityCubehttps:/github.com/khanhnguyenvinh2002/cs103a-pa02/pa02, configfile: pytest.ini
plugins: anyio-2.2.0
[1mcollecting ... [0m[1m
collected 7 items                                                                                               [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                     [ 57%][0m
test_transaction.py [32m.[0m[32m.[0m[32m.[0m[32m                                                                                   [100%][0m

[32m=============================================== [32m[1m7 passed[0m[32m in 0.09s[0m[32m ===============================================[0m
[1m[7m%[27m[1m[0m                                                                                                                
 

[0m[27m[24m[J(base) NguyenThiKimThuy1@nguyens-air pa02 % [K[?2004hppylint transaction.py[?2004l

************* Module transaction
transaction.py:38:0: C0301: Line too long (110/100) (line-too-long)

-----------------------------------
Your code has been rated at 9.86/10

[0m[1m[7m%[27m[1m[0m                                                                                                                
 

[0m[27m[24m[J(base) NguyenThiKimThuy1@nguyens-air pa02 % [K[?2004hppylint tracker.py[?2004l


------------------------------------
Your code has been rated at 10.00/10

[0m[1m[7m%[27m[1m[0m                                                                                                                
 

[0m[27m[24m[J(base) NguyenThiKimThuy1@nguyens-air pa02 % [K[?2004hppylint test_transaction.py[?2004l

************* Module test_transaction
test_transaction.py:11:13: W0621: Redefining name 'dbfile' from outer scope (line 6) (redefined-outer-name)
test_transaction.py:17:13: W0621: Redefining name 'empty_db' from outer scope (line 11) (redefined-outer-name)
test_transaction.py:49:11: W0621: Redefining name 'small_db' from outer scope (line 17) (redefined-outer-name)
test_transaction.py:88:13: W0621: Redefining name 'med_db' from outer scope (line 49) (redefined-outer-name)
test_transaction.py:105:16: W0621: Redefining name 'med_db' from outer scope (line 49) (redefined-outer-name)

-----------------------------------
Your code has been rated at 9.02/10

[0m[1m[7m%[27m[1m[0m                                                                                                                
 

[0m[27m[24m[J(base) NguyenThiKimThuy1@nguyens-air pa02 % [K[?2004hppython tracker.py3 tracker.py[11D[?2004l


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
Next command: 2
Category name: 1
Category description: 1
Next command: 1
id  name       description                   
1   1          1                             
Next command: 3
Updating category
rowid: 1
Category name: 2
Category description: 2
Next command: 1
id  name       description                   
1   2          2                             
Next command: 4
Nothing here
Next command: 5
Transaction item number: 1
Transaction amount: 1
Transaction category: 1
Transaction description: 1
Transaction month: 1
Transaction year: 1
What date was this transaction made(mm/dd/yyyy): 1
Next command: 4


row_id     item number amount     category   date       description                   
1          1          1          1          1          1                             
Next command: 6
Provide ID of transaction to be deleted: 1
Deleting Element with ID: 1
Next command: 4
Nothing here
Next command: 7 5
Transaction item number: 1
Transaction amount: 1
Transaction category: 1
Transaction description: 1
Transaction month: 1
Transaction year: 1
What date was this transaction made(mm/dd/yyyy): 1
Next command: 5
Transaction item number: 2
Transaction amount: 2
Transaction category: 2
Transaction description: 2
Transaction month: 2
Transaction year: 2
What date was this transaction made(mm/dd/yyyy): 2
Next command: 5
Transaction item number: 1
Transaction amount: 2
Transaction category: 1
Transaction description: 2
Transaction month: 1
Transaction year: 2
What date was this transaction made(mm/dd/yyyy): 1
Next command: 7


row_id     item number amount     category   date       description                   
1          1          1          1          1          1                             
3          1          2          1          1          2                             
2          2          2          2          2          2                             
Next command: 8


row_id     item number amount     category   date       description                   
1          1          1          1          1          1                             
3          1          2          1          1          2                             
2          2          2          2          2          2                             
Next command: 9


row_id     item number amount     category   date       description                   
1          1          1          1          1          1                             
2          2          2          2          2          2                             
3          1          2          1          1          2                             
Next command: 10


row_id     item number amount     category   date       description                   
1          1          1          1          1          1                             
3          1          2          1          1          2                             
2          2          2          2          2          2                             
Next command: 11

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

Next command: 0
thank you for using
[1m[7m%[27m[1m[0m                                                                                                                
 

[0m[27m[24m[J(base) NguyenThiKimThuy1@nguyens-air pa02 % [K[?2004heexit[?2004l


Script done on Fri Mar 25 19:26:34 2022
