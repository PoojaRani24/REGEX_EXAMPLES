import re

def validate_phone_number(phone_number):
	regex_phone_number=re.compile(r'^(\(\d{3}\)|\d{3}) \d{3}-\d{4}$')
	res=regex_phone_number.search(phone_number)
	if res:
		return res.group()
	else:
		return False


print(validate_phone_number('(567) 567-5678'))
print(validate_phone_number('567-5678'))
print(validate_phone_number('567 567-5678'))
print(validate_phone_number('My name is Khan'))
