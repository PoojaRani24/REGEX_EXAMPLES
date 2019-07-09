import re

def substitue_text(text):
	pattern=re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+',re.IGNORECASE)
	res=pattern.sub("\g<1> \g<2>",text)
	print(res)


substitue_text("last night Mr. Daisy and Mrs. Amar killed Ms. Chow")