import re

# Function to validate
# ISBN Code
# Taken from  https://www.geeksforgeeks.org/regular-expressions-to-validate-isbn-code/


def is_valid_ISBN_code(str):

	# Regex to check valid ISBN Code
	regex = "^(?=(?:[^0-9]*[0-9]){10}(?:(?:[^0-9]*[0-9]){3})?$)[\\d-]+$"

	# Compile the ReGex
	p = re.compile(regex)

	# If the string is empty
	# return false
	if str == None:
		return False

	# Return if the string
	# matched the ReGex
	if re.search(p, str):
		return True
	else:
		return False
