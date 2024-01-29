#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
	#return sorted dict items
	for key, value in sorted(a_dictionary.items()):
		print("{}: {}".format(key, a_dictionary[key]))
		