import sqlite3
import pytest

@pytest.fixture
def setup_database():
    """ Fixture to set up the in-memory database with test data """
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
	    CREATE TABLE items
        (item_id integer, name text, email text, updated_at blob, created_at blob)''')
    sample_data = [
        (0, 'test', 'test@test.com', '2023-10-23', '2023-10-23'),
        (1, 'test1', 'test1@test.com', '2023-10-23', '2023-10-23'),
    ]
    cursor.executemany('INSERT INTO items VALUES(?, ?, ?, ?, ?)', sample_data)
    yield conn


def test_connection(setup_database):
    # Test to make sure that there are 2 items in the database

    cursor = setup_database
    assert len(list(cursor.execute('SELECT * FROM items'))) == 2
