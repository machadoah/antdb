from antdb import DataBase, Table, TableModel


def get_db():
    db = DataBase()
    return db


def get_table():
    table = Table(name='test', model=TableModel)
    return table
