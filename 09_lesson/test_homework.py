from sqlalchemy import create_engine, inspect, text
from config import Url_base

db_connection_string = Url_base

db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert len(names) == 9


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(subject_title) VALUES (:name)")
    connection.execute(sql, {"name": "Portugal"})

    sql_delete = text("DELETE FROM subject WHERE subject_title = :name")
    connection.execute(sql_delete, {"name": "Portugal"})

    transaction.commit()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO subject(subject_title) VALUES (:name)")
    connection.execute(sql, {"name": "Portugal"})

    sql = text("UPDATE subject SET subject_title = :new_name WHERE subject_title = 'Portugal'")
    connection.execute(sql, {"new_name": "Japan"})

    sql_delete = text("DELETE FROM subject WHERE subject_title = :name")
    connection.execute(sql_delete, {"name": "Japan"})

    transaction.commit()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql = text("INSERT INTO teacher(email) VALUES (:mail)")
    connection.execute(sql, {"mail": "new_teache@gmail.com"})

    sql = text("DELETE FROM teacher WHERE email = :mail")
    connection.execute(sql, {"mail": "new_teache@gmail.com"})

    transaction.commit()
    connection.close()
