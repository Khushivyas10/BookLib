import sqlite3

import pytest

from exception import ValidationError
from library import library
from book import Book


@pytest.fixture
def setup_library():
	"""Fixture to set up and tear down the Library instance."""
	library_instance = library(name="Test Library")
	# Clear the database before each test
	library_instance.cursor.execute("DELETE FROM books")
	library_instance.connection.commit()
	yield library_instance
	library_instance.connection.close()  # Ensure the connection is closed


