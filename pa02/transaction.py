'''
transaction file
'''
import sqlite3

def to_cat_dict_list(tuples):
    ''' to category dictionary list'''
    return [to_cat_dict(category) for category in tuples]

def to_cat_dict(category_tuple):
    ''' to dictionary'''
    category = {
        'rowid':category_tuple[0],
        'number_of_items':category_tuple[1],
        'amount':category_tuple[2],
        'category':category_tuple[3],
        'date':category_tuple[4],
        'desc':category_tuple[5]}
    return category

class Transaction():
    ''' class transaction'''
    def __init__(self,dbfile):
        ''' init'''
        con= sqlite3.connect(dbfile)
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS transactions
                    (number_of_items int, amount float, category text,
                    date text, month text, year text, desc text)''')
        con.commit()
        con.close()
        self.dbfile = dbfile

    def select_all(self):
        ''' select all tuples'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,number_of_items,amount,category,date,month,year,desc from transactions''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def add(self,item):
        ''' add a row and return '''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute("INSERT INTO transactions VALUES(?,?,?,?,?,?,?)",
            (item['number_of_items'],
            item['amount'],
            item['category'],
            item['date'],
            item['month'],
            item['year'],
            item['desc']))
        con.commit()
        cur.execute("SELECT last_insert_rowid()")
        last_rowid = cur.fetchone()
        con.commit()
        con.close()
        return last_rowid[0]

    def delete(self,rowid):
        ''' delete a row by id'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''DELETE FROM transactions
                       WHERE rowid=(?);
        ''',(rowid,))
        con.commit()
        con.close()

    def date(self):
        ''' order by date'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,number_of_items,amount,category,
        date,desc from transactions order by date''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def category(self):
        ''' order by category'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,number_of_items,amount,category,date,
        desc from transactions order by category''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)

    def month(self):
        ''' order by category'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,number_of_items,amount,category,date,
        desc from transactions order by month''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)
    def year(self):
        ''' order by category'''
        con= sqlite3.connect(self.dbfile)
        cur = con.cursor()
        cur.execute('''SELECT rowid,number_of_items,amount,category,date,
        desc from transactions order by year''')
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return to_cat_dict_list(tuples)
