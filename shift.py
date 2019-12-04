#!/usr/bin/env python3
#
# Author: @AleDiBen
#
# EXAMPLE:
#    ./shift.py -a 1 -s 14 -e 'this is a message'

import getopt, sys

# ASCII Printable characters Alphabet (without space) from 33 to 126
ascii_printable = list("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
letters_upper_lower = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
letters_lower_upper = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
alphanumeric = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
letters_upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
letters_lower = list("abcdefghijklmnopqrstuvwxyz")

all_alphabets = [ascii_printable, letters_upper_lower, letters_lower_upper, alphanumeric, letters_upper, letters_lower]

# DEFAULTS
default_alphabet = 0
default_shift = 3

# MODES
ENCODE = 0
DECODE = 1

def usage():
	print("SHIFT CYPHER by [@AleDiBen]\n")
	print("Usage: ./shift.py [OPTIONS] string\n")
	print("OPTIONS:")
	print("\t-a\t alphabet code\t\tDefault 0 - See the table below."
	print("\t-d\t decode a string")
	print("\t-e\t encode a string")
	print("\t-h\t show this message")
	print("\t-s\t shift\t\t\tDefault 3\n")
	print("ALPHABETS:")
	print("\t( 0 ) ASCII Printable characters")
	print("\t( 1 ) Letters form Uppercase to Lowercase: [A-Z][a-z]")
	print("\t( 2 ) Letters from Lowercase to Uppercase: [a-z][A-Z]")
	print("\t( 3 ) Alphanumeric: [0-9][A-Z][a-z]")
	print("\t( 4 ) Letters Uppercase: [A-Z]")
	print("\t( 5 ) Letters Lowercase: [a-z]\n")
	print("EXAMPLE:")
	print("./shift.py -a 1 -s 14 -e 'this is a message'")
	
def position(ch, alphabet):
	index = 0
	try :
		index = alphabet.index(ch)
	except :
		index = -1
	return index

def rot(string, alphabet, shift):
	shifted = ""
	for ch in string:
		# Skip space character
		if ord(ch) == 32 :
			shifted += " "
		# Skip all characters not defined in the alphabet
		elif position(ch, alphabet) == -1 :
			shifted += ch
		else :
			index = position(ch, alphabet)
			index += shift
			shifted += alphabet[index % len(alphabet)]
	return shifted
	
def invrot(string, alphabet, shift):
	return rot(string, alphabet, -shift)
	
def main(argv):
	# Defaults parameters
	alph = all_alphabets[default_alphabet]
	shft = default_shift
	mode = ENCODE
	mssg = ""
	
	# Parse command line arguments
	try :
		opts, args = getopt.getopt(argv, "ha:d:e:s:", ["alphabet=","shift=","decode=","encode="])
	except getopt.GetoptError :
		usage()
		sys.exit(-1)
		
	if len(argv) == 0 :
		usage()
		sys.exit(0)
		
	# Check mutual exclusion between -d and -e options
	optnames = [opt[0] for opt in opts]
	if ("-d" in optnames and "-e" in optnames) :
		print("ERROR: Options -d and -e are mutually exclusive")
		sys.exit(-1)
		
	for opt, arg in opts :
		if opt == '-h' :
			usage()
			sys.exit(0)
		elif opt in ("-a", "--alphabet") :
			if int(arg) > len(all_alphabets) :
				print("ERROR: select a valid Alphabet code")
				sys.exit(-1)
			alph = all_alphabets[int(arg)]
		elif opt in ("-d", "--decode") :
			mode = DECODE
			mssg = arg
		elif opt in ("-e", "--encode") :
			mode = ENCODE
			mssg = arg
		elif opt in ("-s", "--shift") :
			shft = int(arg)
			
	# compute the result
	result = ""
	if mode == ENCODE :
		result = rot(mssg, alph, shft)
	elif mode == DECODE :
		result = invrot(mssg, alph, shft)
		
	print(result)

# The main function
if __name__ == '__main__' :
	main(sys.argv[1:])
