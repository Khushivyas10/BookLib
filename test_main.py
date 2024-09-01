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

# checks whether a new book can be added to the library database and
# verifies its existence before and after the addition
def test_add_book(setup_library):
	# Create a new Book object using the user's input
	library = setup_library
	new_book = Book(
		title="test_book_title",
		author="test_book_author",
		publication_year=9999,
		ISBN="9783161484100",
	)
	book_in_lib = library.cursor.execute(
		"SELECT EXISTS(SELECT title FROM books WHERE title='test_book_title')"
	).fetchone()
	# sqlite iterator returns value in tuple.
	assert book_in_lib == (0,)  # to ensure book does not exist before adding

	library.add_book(new_book)
	book_in_lib = library.cursor.execute(
		"SELECT EXISTS(SELECT title FROM books WHERE title='test_book_title')"
	).fetchone()
	assert book_in_lib == (
		1,
	)  # to ensure that the book has been successfully added and exists in the database.

	# Attempt to add the same book again (with the same ISBN)
	with pytest.raises(
		sqlite3.IntegrityError
	):  # Expecting an IntegrityError due to the unique ISBN constraint
		library.add_book(new_book)


