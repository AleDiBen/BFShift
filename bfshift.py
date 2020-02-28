# ----- BFShift.py -----
#
# Author: @AleDiBen
#         @Omnicrist
#

# Alphabets
import string
import sys
from getopt import getopt, GetoptError

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

    return wrapper


@logger
def rot(message, alphabet, shift):
    shifted = ""

    for char in message:
        if char in alphabet:
            # pre_shift = alphabet.index(char)
            # post_shift = pre_shift + shift
            # alph_length = len(alphabet)
            # moduled = post_shift % alph_length
            # shifted_char = alphabet[
            #     (alphabet.index(char) + shift) % len(alphabet)]
            shifted += alphabet[(alphabet.index(char) + shift) % len(alphabet)]

            # print(
            #     "char: {}    PREshift: {}    POSTshift: {}    alph-length: {}    moduled: {}    shifted: {}".format(
            #         char, pre_shift, post_shift, alph_length, moduled,
            #         shifted_char))
        else:
            shifted += char
            # print("char: {}\t\t\t\t\t\t\t\t\t    shifted: {}".format(char, "NOT IN ALPHABET, NOT PROCESSED"))

    return shifted


def inv_rot(message, alphabet, shift):
    return rot(message, alphabet, -shift)


def usage():
    print("Here is where we should tell you how to use this, TODO")
    for index, alph in enumerate(alphabets):
        print("\t" + str(index) + "\t" + alph)


LOG_SIZE = 40
ENCODE = 0
DECODE = 1
BRUTEFORCE_ALPHABET = 2
BRUTEFORCE_SHIFT = 3


def main(argv):
    # Default parameters

    alphabet = alphabets[0]
    shift = 3
    mode = ENCODE
    message = ""

    # Check command line arguments
    if len(argv) is 0:
        usage()
        exit(0)

    # Parse command line arguments
    try:
        inputs = ["alphabet=", "shift=", "decode=", "encode=",
                  "custom-alphabet=", "bruteforce-alphabet=",
                  "bruteforce-shift="]
        opts, args = getopt(argv, "ha:d:e:s:c:", inputs)
    except GetoptError:
        usage()
        exit(-1)

    # Check mutual exclusion between decode and encode options
    optnames = [opt[0] for opt in opts]
    if optnames in ("-d", "--decode") and optnames in ("-e", "--encode"):
        print( "ERROR: Options -d --decode and -e --encode are mutually exclusive")
        exit(-1)

    if optnames in ("-c", "--custom-alphabet") and optnames in ("-a", "--alphabet"):
        print("ERROR: Options -c --custom-alphabet and -a --alphabet are mutually exclusive")
        exit(-1)

    if optnames in ("--bruteforce-alphabet",) and optnames in ("-c", "--custom-alphabet", "-a", "--alphabet", "-d", "--decode", "-e", "--encode"):
        print("ERROR: Options --bruteforce-alphabet and -c --custom-alphabet -a --alphabet -d --decode -e --encode are mutually exclusive")
        exit(-1)

    if optnames in ("--bruteforce-shift",) and optnames in ("-d", "--decode", "-e", "--encode", "-s", "--shift"):
        print("ERROR: Options --bruteforce-shift and -d --decode -e --encode -s --shift are mutually exclusive")
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
            alphabet = arg
        elif opt in ("--bruteforce-alphabet",):
            mode = BRUTEFORCE_ALPHABET
            message = arg
        elif opt in ("--bruteforce-shift",):
            mode = BRUTEFORCE_SHIFT
            message = arg
        elif opt in ("-d", "--decode"):
            mode = DECODE
            message = arg
        elif opt in ("-e", "--encode"):
            mode = ENCODE
            message = arg
        elif opt in ("-s", "--shift"):
            try:
                shift = int(arg)
            except TypeError:
                print("ERROR: provide a valid shift")

    # Compute the result
    if mode is ENCODE:
        print(rot(message, alphabet, shift))
    elif mode is DECODE:
        print(inv_rot(message, alphabet, shift))
    elif mode is BRUTEFORCE_ALPHABET:
        for alph in alphabets:
            print(inv_rot(message, alph, shift))
    elif mode is BRUTEFORCE_SHIFT:
        for index in range(len(alphabet)):
            print(inv_rot(message, alphabet, index))


if __name__ == '__main__':
    main(sys.argv[1:])
