import sqlite3

from book import Book
from exception import ValidationError


class library:
	def __init__(self, name: str):
		self.name = name
		self.connection = sqlite3.connect(f"{self.name}.db")
		self.cursor = self.connection.cursor()
		self.create_table()
		self.books = self.get_books_from_db()
		self.borrowed_books = []

	def create_table(self):
		self.cursor.execute(
			"""
			CREATE TABLE IF NOT EXISTS books (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				title TEXT NOT NULL,
				author TEXT NOT NULL,
				publication_year INTEGER,
				isbn TEXT NOT NULL UNIQUE,
				borrowed BOOLEAN NOT NULL CHECK (borrowed IN (0, 1)) DEFAULT 0
			)
			"""
		)
		self.connection.commit()

	def get_books_from_db(self):
		"""Fetch all books from the database and return them as a list of tuples."""
		self.cursor.execute("SELECT title, author, publication_year, isbn FROM books")
		books = self.cursor.fetchall()
		return books

	def add_book(self, book: Book):
		self.cursor.execute(
			"""
				INSERT INTO books (title, author, publication_year, isbn, borrowed)
				VALUES (?, ?, ?, ?, ?)
				""",
			(book.title, book.author, book.publication_year, book.ISBN, book.borrowed),
		)
		self.connection.commit()

	def borrow_book(self, title):
		pass

	def return_book(self, title):
		pass

	def view_available_books(self):
		pass
