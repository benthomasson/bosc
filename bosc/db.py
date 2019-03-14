
from sqlalchemy import create_engine

engine = create_engine('sqlite:///file.db')
connection = engine.connect()


def make_tables():
    connection.execute('''create table client (
        id integer not null
    ); ''')
    connection.execute('''create table message (
        id integer not null,
        client_id integer not null,
        message_type varchar not null
    ); ''')

def drop_tables():
    connection.execute('drop table client')
    connection.execute('drop table message')
