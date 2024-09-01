from exception import ValidationError
from utils import is_valid_ISBN_code as is_ISBN_code


class Book:
	def __init__(self, ISBN, title, author, publication_year):
		if not is_ISBN_code(ISBN):
			raise ValidationError("Incorrect ISBN")
		self.ISBN = ISBN
		self.title = title
		self.author = author
		self.publication_year = publication_year
		self.borrowed = False

	def is_valid_ISBN_code(isbn):
		return is_ISBN_code(isbn)

