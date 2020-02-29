# ----- BFShift.py -----
#
# Author: @AleDiBen
#         @Omnicrist
#

# Alphabets
import string
from getopt import getopt, GetoptError
from os import path
from parameters import *

debug = False
LOG_SIZE = 40
ENCODE = 0
DECODE = 1
BRUTEFORCE_ALPHABET = 2
BRUTEFORCE_SHIFT = 3
BRUTEFORCE = 4

alphabets = [
    "!\"#$%&'()*+,-./" + string.digits + r":;<=>?@" + string.ascii_uppercase +
    r"[\]^_`" + string.ascii_lowercase + r"{|}~",
    string.digits + string.ascii_letters + string.punctuation,
    string.ascii_uppercase,
    string.ascii_lowercase,
    string.ascii_letters,
    string.ascii_uppercase + string.ascii_lowercase,
    string.hexdigits,
    string.punctuation
]


def logger(function):
    from functools import wraps
    import inspect

    @wraps(function)
    def wrapper(*args, **kwargs):
        if debug:
            params = []
            arg_spec = inspect.getfullargspec(function).args
            for arg_name, arg_value in zip(arg_spec, args):
                if type(arg_value) is str:
                    if len(arg_value) < 2 * LOG_SIZE:
                        params.append(arg_name + ":" + arg_value)
                    else:
                        params.append(arg_name + ":" + arg_value[:LOG_SIZE] + "  . . .  " + arg_value[-LOG_SIZE:])
                else:
                    params.append(arg_name + ":" + str(arg_value))

            func_signature = function.__name__ + '(' + ', '.join(params) + ')'

            print("LOGGER:\t" + func_signature)
            ret_value = function(*args, **kwargs)

            print("LOGGER:\t" + function.__name__ + "{}".format(
                " returned " + (ret_value if ret_value is not None else "None")))
            return ret_value
        else:
            return function(*args, **kwargs)

    return wrapper

@logger
def check_parameters_list(l : list):
    if len(l) == 1 and l[0] not in ("-h", "--help", "-m", "--message"):
        return False

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            val = matrix[l[i].value][l[j].value]
            if val == -2:
                return val, f"LOGIC ERROR: {l[i]} and {l[j]} should not be used together"
            if val == -1:
                return val, f"ERROR: {l[i]} and {l[j]} are the same parameter"
            if not val:
                return val, f"ERROR: {l[i]} and {l[j]} are mutually exclusive"
    return True, ""

@logger
def rot(message, alphabet, shift):
    shifted = ""

    for char in message:
        if char in alphabet:
            if debug:
                pre_shift = alphabet.index(char)
                post_shift = pre_shift + shift
                alph_length = len(alphabet)
                moduled = post_shift % alph_length
                shifted_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
                print("char: {}    PREshift: {}    POSTshift: {}    alph-length: {}    moduled: {}    shifted: {}"
                        .format(char, pre_shift, post_shift, alph_length, moduled, shifted_char))

            shifted += alphabet[(alphabet.index(char) + shift) % len(alphabet)]
        else:
            shifted += char
            if debug:
                print("char: {}\t\t\t\t\t\t\t\t\t    shifted: {}".format(char, "NOT IN ALPHABET, NOT PROCESSED"))

    return shifted


def inv_rot(message, alphabet, shift):
    return rot(message, alphabet, -shift)

def check_input_parameters(opts):
    opt_list = []

    for opt, _ in opts:
        if opt in ("-h", "--help"):
            opt_list.append(Parameters.HELP)
        elif opt in ("-a", "--alphabet"):
            opt_list.append(Parameters.ALPHABET)
        elif opt in ("--bruteforce-alphabet",):
            opt_list.append(Parameters.BRUTEFORCE_ALPHABET)
        elif opt in ("-b", "--bruteforce-all"):
            opt_list.append(Parameters.BRUTEFORCE_ALL)
        elif opt in ("--bruteforce-shift",):
            opt_list.append(Parameters.BRUTEFORCE_SHIFT)
        elif opt in ("-c", "--custom-alphabet"):
            opt_list.append(Parameters.CUSTOM_ALPHABET)
        elif opt in ("-d", "--decode"):
            opt_list.append(Parameters.DECODE)
        elif opt in ("--debug",):
            opt_list.append(Parameters.DEBUG)
        elif opt in ("-e", "--encode"):
            opt_list.append(Parameters.ENCODE)
        elif opt in ("--flag-format",):
            opt_list.append(Parameters.FLAG_FORMAT)

    return opt_list

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
    print("SYNTAX : python bfshift.py [OPTIONS] -m \"A MESSAGE\" ")
    print("OPTIONS: ")
    print("  -a --alphabet\t\t\t the alphabet number chosen from the list below")
    print("  -c --custom-alphabet\t\t specify your own alphabet using a string or a file")
    print("  -d --decode\t\t\t decode mode")
    print("  -e --encode\t\t\t encode mode")
    print("  -h --help\t\t\t print the usage")
    print("  -m --message\t\t\t a message to encode/decode")
    print("  -s --shift\t\t\t amount of shift to encode/decode a message")
    print("     --bruteforce-alphabet\t try to decode using all alphabets")
    print("     --bruteforce-shift\t\t try to decode using all possible shifts")
    print("     --debug\t\t\t enable logging for debug purposes")
    print("     --flag-format\t\t filter results that contain a specific format")
    print("EXAMPLES:")
    print("  python bfshift.py -m this_is_a_message")
    print("  python bfshift.py -e -m this_is_a_message")
    print("  python bfshift.py -d -m wklvblvbdbphvvdjh")
    print("  python bfshift.py -a 3 -s 7 -m this_is_a_message")
    print("  python bfshift.py -a 3 -e -s 7 -m \"hsalab{this_is_a_message}\"")
    print("  python bfshift.py -a 3 -d -s 7 -m \"ozhshi{aopz_pz_h_tlzzhnl}\"")
    print("  python bfshift.py -a 3 --bruteforce-shift -m \"ozhshi{aopz_pz_h_tlzzhnl}\"")
    print("  python bfshift.py -a 3 --bruteforce-shift --flag-format \"hsalab{\" -m \"ozhshi{aopz_pz_h_tlzzhnl}\"")
    print("  python bfshift.py --bruteforce-alphabet -s 7 --flag-format \"hsalab{\" -m \"ozhshi{aopz_pz_h_tlzzhnl}\"")
    print("\n\n BUILT-IN ALPHABETS")
    print("--------------------")
    for index, alph in enumerate(alphabets):
        print("  " + str(index) + ")  " + alph)
    print()

@logger
def main(argv):
    # Default parameters
    alphabet = None
    message = None
    shift = None
    flag = None
    mode = BRUTEFORCE

    # Check command line arguments
    if len(argv) == 0:
        usage()
        exit(0)

    # Parse command line arguments
    try:
        inputs = ["alphabet=", "shift=", "decode", "encode", "message=",
                  "custom-alphabet=", "bruteforce-alphabet", "debug",
                  "bruteforce-shift", "flag-format=", "bruteforce-all"]
        opts, args = getopt(argv, "ha:dem:s:c:b", inputs)
    except GetoptError:
        usage()
        exit(-1)

    # Check mutual exclusion between options

    return_value, control = check_parameters_list(check_input_parameters(opts))
    if return_value <= 0:
        print(control)
        exit(-1)


    # Process command line arguments
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            exit(0)
        elif opt in ("-a", "--alphabet"):
            try:
                index = int(arg)
            except TypeError:
                print("ERROR: provide a valid shift")
                exit(-1)
            if index > len(alphabets):
                print("ERROR: select a valid alphabet")
                exit(-1)
            alphabet = alphabets[index]
        elif opt in ("-c", "--custom-alphabet"):
            if len(arg) < 3:
                print("ERROR: provide at least a 3 chars alphabet")
                exit(-1)
            if path.isfile(arg):
                with open(arg, 'r') as f: content = f.read()
                alphabet = content
            else:
                alphabet = arg
        elif opt in ("--flag-format",): flag = arg
        elif opt in ("--debug",):
            global debug
            debug = True
        elif opt in ("--bruteforce-alphabet",): mode = BRUTEFORCE_ALPHABET
        elif opt in ("--bruteforce-shift",): mode = BRUTEFORCE_SHIFT
        elif opt in ("-b", "--bruteforce-all"): mode = BRUTEFORCE
        elif opt in ("-d", "--decode"): mode = DECODE
        elif opt in ("-e", "--encode"): mode = ENCODE
        elif opt in ("-m", "--message"): message = arg
        elif opt in ("-s", "--shift"):
            try: shift = int(arg)
            except ValueError:
                print("ERROR: provide a valid shift")
                exit(-1)

    # Compute the result
    if mode is ENCODE: print(rot(message, alphabet, shift))
    elif mode is DECODE: print(inv_rot(message, alphabet, shift))
    elif mode is BRUTEFORCE_ALPHABET:
        check = False
        for alph in alphabets:
            if flag:
                string = inv_rot(message, alph, shift)
                if string.__contains__(flag):
                    check = True
                    print(string)
            else:
                print(inv_rot(message, alph, shift))
        if not check:
            print(f"There was no string containing {flag}")
    elif mode is BRUTEFORCE_SHIFT:
        check = False
        for index in range(len(alphabet)):
            if flag:
                string = inv_rot(message, alphabet, index)
                if string.__contains__(flag):
                    check = True
                    print(string)
            else:
                print(inv_rot(message, alphabet, index))
        if not check:
            print(f"There was no string containing {flag}")
    elif mode is BRUTEFORCE:
        check = False
        for alph in alphabets:
            for index in range(len(alph)):
                if flag:
                    string = inv_rot(message, alph, index)
                    if string.__contains__(flag):
                        check = True
                        print(string)
                else:
                    print(inv_rot(message, alph, shift))
        if not check:
            print(f"There was no string containing {flag}")


if __name__ == '__main__':
    from sys import argv
    main(argv[1:])
