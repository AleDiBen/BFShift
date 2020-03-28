#!/usr/bin/python3

import string
from getopt import getopt, GetoptError
from os import path
from sys import argv
from parameters import *

# GLOBAL VARIABLES
alphabet_id = 0
bf_method = None
custom_alphabet = None
debug = False
flag_format = ""
message = ""
mode = Modes.ENCODE
shift_amount = 13

dgts = string.digits
uppr = string.ascii_uppercase
lowr = string.ascii_lowercase
alphabets = [
	# All printable ASCII characters from 32 to 126
	" !\"#$%&\'()*+,-./" + dgts + r":;<=>?@" + uppr + "[\\]^_`" + lowr + "{|}~",
	# Letters: lower case + upper case
	string.ascii_letters,
	# Letters: upper case + lower case
	uppr + lowr,
	# Digits + lower case letters + upper case letters
	dgts + string.ascii_letters,
	# Only punctuation
	string.punctuation,
	# Hex Digits
	string.hexdigits
]


def usage():
    print("                                                      ")
    print(" ██████╗ ███████╗███████╗██╗  ██╗██╗███████╗████████╗ ")
    print(" ██╔══██╗██╔════╝██╔════╝██║  ██║██║██╔════╝╚══██╔══╝ ")
    print(" ██████╔╝█████╗  ███████╗███████║██║█████╗     ██║    ")
    print(" ██╔══██╗██╔══╝  ╚════██║██╔══██║██║██╔══╝     ██║    ")
    print(" ██████╔╝██║     ███████║██║  ██║██║██║        ██║    ")
    print(" ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝    ")
    print("                                            @AleDiBen ")
    print("                                            @Omnicrist")
    print("                                                      ")
    print(" !A super simple BruteForce script for shift ciphers! ")
    print("                                                      ")
    print("SYNTAX : python bfshift.py [OPTIONS] -m A_STRING_XXX  ")
    print("\nOPTIONS: ")
    print("  -a --alphabet\t\t\t the alphabet number chosen from the list below")
    print("  -c --custom-alphabet\t\t specify your own alphabet using a string")
    print("  -d --decode\t\t\t decode mode")
    print("  -e --encode\t\t\t encode mode")
    print("  -h --help\t\t\t print the usage")
    print("  -m --message\t\t\t a message to encode/decode")
    print("  -s --shift\t\t\t amount of shift to encode/decode a message")
    print("     --bf-all\t\t try to decode using all alphabets and possible shifts")
    print("     --bf-alphabets\t try to decode using all alphabets")
    print("     --bf-shift\t\t try to decode using all possible shifts")
    print("     --debug\t\t\t enable logging for debug purposes")
    print("     --flag-format\t\t filter results that contain a specific format")
    print("\nDEFAULT OPTIONS:")
    print("  alphabet : 0")
    print("  shift    : 13")
    print("  mode     : encode")
    print("\nEXAMPLES:")
    print("  python bfshift.py -m this_is_a_message")
    print("  python bfshift.py -e -m this_is_a_message")
    print("  python bfshift.py -d -m '\"uv!lv!lnlzr!!ntr'")
    print("  python bfshift.py -a 3 -s 7 -m this_is_a_message")
    print("  python bfshift.py -a 3 -e -s 7 -m 'hsalab{this_is_a_message}'")
    print("  python bfshift.py -a 3 -d -s 7 -m 'ozhshi{Aopz_pz_h_tlzzhnl}'")
    print("  python bfshift.py -a 3 --bf-shift -m 'ozhshi{Aopz_pz_h_tlzzhnl}'")
    print("  python bfshift.py -a 3 --bf-shift --flag-format 'hsalab{' -m 'ozhshi{Aopz_pz_h_tlzzhnl}'")
    print("  python bfshift.py --bf-alphabets -s 7 --flag-format 'hsalab{' -m 'ozhshi{Aopz_pz_h_tlzzhnl}'")
    print("  python bfshift.py --bf-all --flag-format 'hsalab{' -m 'ozhshi{Aopz_pz_h_tlzzhnl}'")
    print("\nBUILT-IN ALPHABETS")
    print("----------------------------------------")
    for index, alph in enumerate(alphabets):
        print("  " + str(index) + ")  " + alph)
    print("----------------------------------------")


def printdbg(message, level=DebugMessages.INFO):
	global debug
	if debug:
		if level == DebugMessages.INFO:
			print("[  INFO  ]", message)
		elif level == DebugMessages.WARNING:
			print("[WARNING!]", message)
		elif level == DebugMessages.ERROR:
			print("[ ERROR! ]", message)
		elif level == DebugMessages.FATAL:
			print("[ FATAL! ]", message)


def printerr(message):
	print("[  ERROR!  ]", message)

# Parse options
def parse_opts(opts):
	global alphabet_id
	global bf_method
	global custom_alphabet
	global debug
	global flag_format
	global message
	global mode
	global shift_amount
	alphabet_error = False
	shift_error = False
	opt_list = []

	for opt, val in opts:
		if opt in ("-a", "--alphabet"):
			opt_list.append(Parameters.ALPHABET)
			try: 
				alphabet_id = int(val)
			except ValueError:
				alphabet_error = True
		elif opt in ("-b", "--bf-all"):
			opt_list.append(Parameters.BRUTEFORCE_ALL)
			bf_method = BruteForceMethod.ALL
			mode = Modes.DECODE
		elif opt in ("--bf-alphabets",):
			opt_list.append(Parameters.BRUTEFORCE_ALPHABET)
			bf_method = BruteForceMethod.ALPHABET
			mode = Modes.DECODE
		elif opt in ("--bf-shift",):
			opt_list.append(Parameters.BRUTEFORCE_SHIFT)
			bf_method = BruteForceMethod.SHIFT
			mode = Modes.DECODE
		elif opt in ("-c", "--custom-alphabet"):
			opt_list.append(Parameters.CUSTOM_ALPHABET)
			last_id = len(alphabets)
			alphabets.append(str(val))
			custom_alphabet = str(val)
			alphabet_id = last_id
		elif opt in ("-d", "--decode"):
			opt_list.append(Parameters.DECODE)
			mode = Modes.DECODE
		elif opt in ("--debug",):
			opt_list.append(Parameters.DEBUG)
			debug = True
		elif opt in ("-e", "--encode"):
			opt_list.append(Parameters.ENCODE)
			mode = Modes.ENCODE
		elif opt in ("--flag-format",):
			opt_list.append(Parameters.FLAG_FORMAT)
			flag_format = str(val)
		elif opt in ("-h", "--help"):
			opt_list.append(Parameters.HELP)
			usage()
		elif opt in ("-m", "--message"):
			message = str(val)
			if message == "":
				printerr("EMPTY MESSAGE")
				exit(-1)
			opt_list.append(Parameters.MESSAGE)
		elif opt in ("-s", "--shift"):
			opt_list.append(Parameters.SHIFT)
			try: 
				shift_amount = int(val)
			except ValueError:
				shift_error = True

	printdbg("------------------------------PARSING THE ARGUMENTS-----------------------------")
	if alphabet_id > len(alphabets) or alphabet_error:
		printdbg("Not a valid alphabet index", DebugMessages.WARNING)
		printdbg("Switching to default alphabet")
		alphabet_id = 0

	if shift_error:
		printdbg("Not a valid shift amount", DebugMessages.WARNING)
		printdbg("Switching to default shift amount", DebugMessages.INFO)
		shift_amount = 13

	if Parameters.BRUTEFORCE_ALPHABET in opt_list and Parameters.BRUTEFORCE_SHIFT in opt_list:
		printdbg("Detected --bf-alphabets and --bf-shift options", DebugMessages.WARNING)
		printdbg("Suggestion: you can simply use --bf-all")
		printdbg("Switching to BRUTEFORCE_ALL method")
		bf_method = BruteForceMethod.ALL

	printdbg("PARSING OK")
	return opt_list

# Check mutex between options, check if an
# option is repeated two or more times
def check_opts(l: list):

	if Parameters.HELP in l:
		return False

	if Parameters.MESSAGE not in l:
		printerr("Missing message option")
		return False

	printdbg("\r          ")
	printdbg("-------------------------------COMPATIBILITY CHECK------------------------------")
	for i in range(len(l)):
		for j in range(i + 1, len(l)):
			code = matrix[l[i].value][l[j].value]
			iparam_name = f"{l[i]}".replace("Parameters.", "")
			jparam_name = f"{l[j]}".replace("Parameters.", "")
			printdbg(f"{iparam_name} compatible with {jparam_name} ?? " + str(code == 0))
			if code == Errors.SAME_OPT.value:
				printerr(f"Repeated options {iparam_name}")
			elif code == Errors.MUTEX.value:
				printerr(f"The option {iparam_name} is not compatible with the option {jparam_name}")
			
			if code < 0:
				return False

	return True


def encode_message(message, alphabet, shift):
	shifted = ""
	for char in message:
		if char in alphabet:
			shifted += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
		else:
			shifted += char

	return shifted


def decode_message(message, alphabet, shift):
    return encode_message(message, alphabet, -shift)


def bruteforce(message, alphabets=None, shifts=None):
	results = ""
	for a in alphabets:
		if shifts == None:
			shifts = range(1, len(a))
		for s in shifts:
			results += decode_message(message, a, s) + "\n"

	return results[:-1]


# MAIN
if __name__ == "__main__":
	arguments = argv[1:]

	if len(arguments) == 0:
		usage()
		exit(0)

	try:
		inputs = ["alphabet=", "bf-all", "bf-alphabets", "bf-shift", "custom-alphabet=", "debug", "decode", "encode", "flag-format=", "help", "message=", "shift="]
		opts, _ = getopt(arguments, "a:bc:def:hm:s:", inputs)
	except GetoptError:
		printerr("Invalid input arguments. Check the usage with option -h.")
		exit(0)

	# PARSE ARGUMENTS + VALUES CHECKING
	parsed_opts = parse_opts(opts)
	
	# MUTEX CHECK
	opts_ok = check_opts(parsed_opts)

	if opts_ok:
		if Parameters.HELP in parsed_opts:
			usage()
			exit(0)

		strmode = f"{mode}".replace("Modes.", "")
		printdbg("\r          ")
		printdbg("-------------------------------PRE EXECUTION CHECK------------------------------")
		printdbg("Parsed options  : " + ', '.join(f"{x}".replace("Parameters.", "") for x in parsed_opts))
		printdbg("Custom alphabet : " + str(custom_alphabet))
		printdbg("Message         : " + message)
		printdbg("Mode            : " + strmode)
		printdbg("\r          ")
		printdbg("------------------------------------EXECUTION-----------------------------------")
		
		result = ""
		if mode == Modes.ENCODE:
			printdbg("Using alphabet  : " + str(alphabets[alphabet_id]))
			printdbg("Using shift     : " + str(shift_amount))
			result = encode_message(message, alphabets[alphabet_id], shift_amount)
		elif mode == Modes.DECODE:
			possible_strings = ""
			printdbg("BF Method       : " + str(bf_method).replace("BruteForceMethod.", ""))
			if (bf_method == None):
				result = decode_message(message, alphabets[alphabet_id], shift_amount)
			elif bf_method == BruteForceMethod.ALL:
				printdbg("Using alphabet  : All ("+ str(len(alphabets)) +") alphabets")
				printdbg("Using shift     : All possible shifts")
				possible_strings = bruteforce(message, alphabets)
			elif bf_method == BruteForceMethod.ALPHABET:
				printdbg("Using alphabet  : All ("+ str(len(alphabets)) +") alphabets")
				printdbg("Using shift     : All possible shifts")
				possible_strings = bruteforce(message, alphabets, [shift_amount])
			elif bf_method == BruteForceMethod.SHIFT:
				printdbg("Using alphabet  : " + str(alphabets[alphabet_id]))
				shift_amount = len(alphabets[alphabet_id])
				printdbg("Using shift     : from 1 to " + str(shift_amount))
				possible_strings = bruteforce(message, [alphabets[alphabet_id]], range(1, shift_amount))

			if flag_format != "":
				arr_possible_strings = possible_strings.split("\n")
				for s in arr_possible_strings:
					if flag_format in s:
						result += s + "\n"
				result = result[:-1]
			else:
				result = possible_strings

		printdbg("\r          ")
		print(result)

	exit(0)
	
		