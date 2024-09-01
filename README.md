# BookLib

**BookLib** is a Library management System . This project implements key features such as adding books, borrowing books, returning books, and viewing available books. The system is thoroughly tested, with test cases developed to ensure the reliability and correctness of each functionality.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Pre-commit-Hooks](#pre-commit-Hooks)

## Features

- **View Available Books**: Return all the available books in Table
- **Add Books**: Update Table with newly added books
- **Borrow Books**: Manage Borrowed books
- **Return Books**: Handle Return of borrowed books and update table
- **Unique ISBN Enforcement**: Prevents the addition of books with duplicate ISBNs to the library.
- **Pre-commit Hooks**: Ensures code quality with checks for trailing whitespace, YAML syntax, Python code style, and more.
- **Automated Testing**: Includes tests for adding, borrowing, and returning books.

  
## Prerequisites
- Python 3.x
- sqlite3 (comes with Python)
- A virtual environment (optional but recommended)

## Installation

To set up the project, follow these steps:

1. **Clone the repository**:
    
    ```bash
    git clone https://github.com/Khushivyas10/BookLib.git
    cd BookLib
    ```

2. Create and activate a virtual environment:
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
    
   ```bash
    pip install -r requirements.txt
   ```

4. **Set up the database**:
   The system uses an SQLite database. The database will be automatically created when you run 
   the system for the first time.


## Usage

To use **BookLib**, follow these steps:

**Run the application**:
    
   ```bash
    python main.py
   ```



## Testing

To run tests for **Project Name**:

1. **Run the test suite**:
    
   ```bash
    pip install pytest
   ```

## Pre-commit-Hooks
1. **Install pre-commit**:
    
    ```bash
   pip install pre-commit
    ```
    
2. **Pre-commit-hooks used**:
- trailing-whitespace: Removes trailing whitespace.
- check-yaml: Checks YAML files for syntax errors.
- no-commit-to-branch: Prevents committing directly to the main branch.
- check-merge-conflict: Ensures no merge conflicts are committed.
- check-ast: Checks for Python syntax errors.
- black: Formats Python code according to PEP 8.
- isort: Sorts Python imports.
- flake8: Checks Python code for style and potential errors.
- pytest: Runs tests to ensure no code breaks.

