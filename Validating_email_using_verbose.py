import re

def validate_email(email):
	#regex_email=re.compile(r'^[a-z0-9_\.-]+@([0-9a-z\.-]*)\.([a-z\.]{2,6}*)$')
	regex_email=re.compile(r"""
		^([a-z0-9_\.-]+)             #first part of email
		@                          #single @ sign
		([0-9a-z\.-]+)             #Domain name
		\.                         #single .
		([a-z\.]{2,6})$           #com/net/org etc       
		""",re.VERBOSE | re.IGNORECASE)

	res=regex_email.fullmatch(email)
	if res:
		print(res.group())
	else:
		print("Invalid")

validate_email("kitty@gmail.com")
validate_email("Kitty@gmail.com")
validate_email("kitty@gmail.com.pudjdkd")
validate_email("kitty@gmail")

