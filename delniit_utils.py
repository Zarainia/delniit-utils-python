import re
import unicodedata


UPPER_TO_LOWER = {'Λ': 'a', '́Λ': 'á', '̀Λ': 'à', 'B': 'ƃ', 'C': 'c', 'Ç': 'ç', 'Δ': 'ᴧ', 'Σ': 'e', '́Σ': 'é', 'F': 'ſ', 'Ԍ': 'ʒ', 'H': 'н', 'I': 'ı', 'Í': 'í', 'Ì': 'ì', 'Î': 'î', 'Э': 'э', 'L': 'ʟ', 'M': 'м', 'N': 'ɴ', 'O': 'o', 'Ψ': 'ч', 'Ж': 'ж', 'Ӂ': 'ӂ', 'R': 'г', 'S': 's', 'X': 'x', 'T': 'т', 'Ѳ': 'ѳ', 'П': 'п', 'Ф': 'ɸ', 'V': 'v', 'W': 'w', '☐': 'ㇿ', 'Y': 'y', 'Z': 'z'} #: Conversions from capital to lowercase for Delniit letters
LOWER_TO_UPPER = {l:u for u, l in UPPER_TO_LOWER.items()} #: Conversions from lowercase to capital for Delniit letters
SORT_ORDER = [char for letter in UPPER_TO_LOWER.items() for char in letter] #: Order of letters when sorting

ACCENTS_TO_BASE = {'́Λ': 'Λ', 'á': 'a', '̀Λ': 'Λ', 'à': 'a', 'Ç': 'C', 'ç': 'c', '́Σ': 'Σ', 'é': 'e', 'Í': 'I', 'í': 'ı', 'Ì': 'I', 'ì': 'ı', 'Î': 'I', 'î': 'ı', 'Ӂ': 'Ж', 'ӂ': 'ж'}


def delniit_split(text):
	"""
	Return the text split into characters, keeping the combining-accented uppercase letters together with their accents
	
	:param str text: text to split
	:return: split text
	:rtype: list[str]
	"""
	
	return re.findall (r".[\u0300\u0301]?", text)

def delniit_lower(text):
	"""
	Return the text converted to lowercase (by Delniit standards)
	
	:param str text: text to convert
	:return: lowercase text
	:rtype: str 
	"""
	
	return ''.join(UPPER_TO_LOWER.get(char, char) for char in delniit_split(text))

def delniit_upper(text):
	"""
	Return the text converted to uppercase (by Delniit standards)

	:param str text: text to convert
	:return: uppercase text
	:rtype: str 
	"""
	
	return ''.join (LOWER_TO_UPPER.get (char, char) for char in delniit_split(text))

def deaccentify(text):
	"""
	Return the text with Delniit accents converted to base letters

	:param str text: text to convert
	:return: deaccentified text
	:rtype: str 
	"""
	
	return ''.join (ACCENTS_TO_BASE.get (char, char) for char in delniit_split(text))

def delniit_key(text):
	"""
	Return a conversion of the string ``text`` so it can be compared with others processed in the same way in Delniit alphabetical order
	
	:param str text: string to convert to a key
	:return: the text in a format that can be used as a key when sorting or otherwise compared using normal Python functions
	:rtype: list[int]
	"""
	
	return [SORT_ORDER.index(char) for char in delniit_split(text)]

def delniit_sort(to_sort):
	"""
	Return the iterable sorted in Delniit fashion
	
	:param to_sort: iterable to sort
	:return: sorted iterable
	"""
	
	return sorted(to_sort, key=delniit_key)


def split_ipa_letters (ipa, keep_stress=False):
	"""
	Return the text split into characters, keeping the combining-accented uppercase letters together with their accents
	
	:param str text: text to split
	:return: split text
	:rtype: list[str]
	"""
	
	if not keep_stress:
		ipa = ipa.replace('ˈ', '').replace('ˌ', '')
	return re.findall (r"(?:t͡s|d͡z|\w|\u0329ˤ)[\u0303]?", ipa)

if __name__ == "__main__":
	# print(delniit_lower("☐"))
	print(list(UPPER_TO_LOWER.values()))
