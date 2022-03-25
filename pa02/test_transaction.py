''' test transaction'''
import pytest
from transaction import Transaction, to_cat_dict

@pytest.fixture
def dbfile(tmpdir):
    ''' create temp db file '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty db '''
    db_transaction = Transaction(dbfile)
    yield db_transaction

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    item1 = {'number_of_items':10,
        'amount':10,
        'category':'testing delete',
        'date':'20/12/2022',
        'month':'12',
        'year':'12',
        'desc':'I like this hw'}
    item2 = {'number_of_items':21,
        'amount':21,
        'category':'testing delete',
        'date':'12/12/1212',
        'month':'12',
        'year':'12',
        'desc':'I enjoy this hw'}
    item3 = {'number_of_items':12,
        'amount':12,
        'category':'testing delete',
        'date':'12/12/2121',
        'month':'12',
        'year':'12',
        'desc':'I love this hw'}
    id1=empty_db.add(item1)
    id2=empty_db.add(item2)
    id3=empty_db.add(item3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    ids=[]
    # add 10
    for i in range(10):
        my_string = str(i)
        item ={
            'number_of_items':12,
            'amount':12,
            'category':"hw" +my_string,
            'date':"12/12/1212",
            'month':'12',
            'year':'12',
            'desc':'hw'+my_string
            }
        item_id = small_db.add(item)
        ids.append(item_id)

    yield small_db

    # remove 10
    for j in range(10):
        small_db.delete(ids[j])

@pytest.mark.simple
def test_to_cat_dict():
    ''' teting the to_cat_dict function '''
    my_test = to_cat_dict(
        (1, 2, 3, 'testing delete','4/1/2022'
        ,'testing delete')
    )
    assert my_test['number_of_items']==2
    assert my_test['amount']==3
    assert my_test['category']=='testing delete'
    assert my_test['date']=='4/1/2022'
    assert my_test['desc']=='testing delete'
    assert len(my_test.keys())==6

@pytest.mark.add
def test_add(med_db):
    ''' add and check size change'''
    item0 = {
        'number_of_items':12,
        'amount':12,
        'category':"testing delete",
        'date':"12/12/1212",
        'month':'12',
        'year':'12',
        'desc':'testing delete'
        }
    items0 = med_db.select_all()
    med_db.add(item0)
    items1 = med_db.select_all()
    assert len(items1) == len(items0) + 1

@pytest.mark.delete
def test_delete(med_db):
    ''' delete and check size change'''
    items0 = med_db.select_all()
    item0 = {'number_of_items':12,
            'amount':12,
            'category':"testing delete",
            'date':"2022-04-01",
            'month':'12',
            'year':'12',
            'desc':'testing delete'
            }
    rowid = med_db.add(item0)
    items1 = med_db.select_all()
    med_db.delete(rowid)
    items2 = med_db.select_all()
    assert len(items0)==len(items2)
    assert len(items2) == len(items1)-1
