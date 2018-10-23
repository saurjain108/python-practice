def anagramfun():
	first = raw_input("Enter first word: ")
	second = raw_input("Enter second word: ")

	if sorted(first.lower())==sorted(second.lower()):
		print( first, " and ", second, "are anagrams")
	else:
		print( first, " and ", second, "are not anagrams")

