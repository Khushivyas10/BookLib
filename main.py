import inquirer

from book import Book
from library import library

library = library(name="My Library")


def main_menu():
	questions = [
		inquirer.List(
			"operation",
			message="Select an operation",
			choices=["Add Book", "Borrow Book", "Return Book", "View Books", "Close"],
		),
	]
	answers = inquirer.prompt(questions)
	return answers["operation"]


def add_book():
	"""
	Prompts the user for book details and adds the book to the library.
	"""
	# Ask user for book details
	questions = [
		inquirer.Text("title", message="Enter the book title"),
		inquirer.Text("author", message="Enter the author's name"),
		inquirer.Text("publication_year", message="Enter the publication year"),
		inquirer.Text("ISBN", message="Enter the ISBN number"),
	]
	answers = inquirer.prompt(questions)

	# Create a new Book object using the user's input
	new_book = Book(
		title=answers["title"],
		author=answers["author"],
		publication_year=int(answers["publication_year"]),
		ISBN=answers["ISBN"],
	)

	# Add the book to the library using the add_book method from the Library class
	library.add_book(new_book)
	print(f"Book '{answers['title']}' added successfully.")


def borrow_book():
	"""
	Prompts the user for a book title and borrows it if available.
	"""
	# Ask user for the title of the book to borrow
	questions = [
		inquirer.Text("title", message="Enter the title of the book to borrow"),
	]
	answers = inquirer.prompt(questions)

	# Borrow the book using the borrow_book method from the Library class
	result = library.borrow_book(answers["title"])
	print(result)


def return_book():
	"""
	Prompts the user for a book title and returns it if it was borrowed.
	"""
	# Ask user for the title of the book to return
	questions = [
		inquirer.Text("title", message="Enter the title of the book to return"),
	]
	answers = inquirer.prompt(questions)

	# Return the book using the return_book method from the Library class
	result = library.return_book(answers["title"])
	print(result)


def view_book():
	"""
	Displays all available books (those not currently borrowed) in the library.
	"""
	# Retrieve and display all available books using the view_available_books method from the Library class
	available_books = library.view_available_books()
	if not available_books:
		print("No books available.")
	else:
		print("Available books:")
		for book in available_books:
			print(f"{book[0]} by {book[1]} (Published in {book[2]}) - ISBN: {book[3]}")


def perform_operation(operation):

	if operation == "Add Book":
		add_book()
	elif operation == "Borrow Book":
		borrow_book()
	elif operation == "Return Book":
		return_book()
	elif operation == "View Books":
		view_book()

	if operation != "Close":
		run_menu()


def run_menu():
	operation = main_menu()
	perform_operation(operation)


if __name__ == "__main__":
	run_menu()
