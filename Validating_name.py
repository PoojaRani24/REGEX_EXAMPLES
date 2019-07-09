import re

def validating_name(name):
	regex_name=re.compile(r'^(Mr\.|Mrs\.|Ms\.) (?P<First>[A-Z][A-Za-z]+)(?P<Second> [A-Z][A-Za-z]+)*( [A-Z][A-Za-z]+)*$')
	res=regex_name.fullmatch(name)
	if res:
		print(res.group())
		print(res.group("First"))
		print(res.group('Second'))
	else:
		print("Invalid")


validating_name('Mr. Albus Severus Potter')
validating_name('nnnnnnMr. Albus Severus Pottermmm')
validating_name('Mr. Potter')