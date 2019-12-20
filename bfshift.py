#!/usr/bin/env
#
# Author: @AleDiBen
#         @Omnicrist
#

from getopt import getopt, GetoptError
from sys import exit, argv
import string

# Alphabets
alphabets = [
    "!\\\"#$%&'()*+,-./" + string.digits + r":;<=>?@" + string.ascii_uppercase +
    r"[\]^_`" + string.ascii_lowercase + r"{|}~",
    string.printable,
    string.ascii_uppercase,
    string.ascii_lowercase,
    string.ascii_letters,
    string.ascii_uppercase + string.ascii_lowercase,
    string.digits,
    string.hexdigits,
    string.octdigits,
    string.punctuation,
    string.whitespace
]

# Modes
ENCODE, DECODE = 0, 1


def usage():
    print("BruteForce SHIFT cypher by [@AleDiBen]")
    print()
    print("Usage: ./bfshift.py [OPTIONS] string")
    print()
    print("OPTIONS:")
    print(
        "\t-a\t--alphabet\t alphabet code\t\tDefault 0 - See the table below.")
    print("\t-s\t--shift\t\t shift\t\t\t\tDefault 3\n")
    print("\t-d\t--decode\t decode a string")
    print("\t-e\t--encode\t encode a string")
    print("\t-h\t--help\t\t show this message")
    print()
    print("ALPHABETS:")
    print(
        "\tNote: if the line breaks, it's because the alphabet includes the \\n character")
    for index, alphabet in enumerate(alphabets):
        print(f"\t( {index} ):\t{alphabet}")
    print()
    print("EXAMPLE:")
    print("\t./bfshift.py -a 1 -s 14 -e 'this is a message'")
    print("\t./bfshift.py --alphabet=1 --shift=14 --encode 'this is a message'")


def position(ch, alphabet):
    try:
        return alphabet.index(ch)
    except IndexError:
        return -1


def rot(string, alphabet, shift):
    shifted = ""

    for ch in string:
        index = position(ch, alphabet)
        alphabet_length = len(alphabet)
        if ord(ch) is 32:
            shifted += " "
        elif index is -1:
            shifted += ch
        else:
            index += shift
            shifted += alphabet[index % alphabet_length]

    return shifted


def inv_rot(string, alphabet, shift):
    return rot(string, alphabet, -shift)


def main(argv):
    # Default parameters
    alphabet = alphabets[0]
    shift = 3
    mode = ENCODE
    message = "this is a message"

    # Check command line arguments
    if len(argv) is 0:
        usage()
        exit(0)

    # Parse command line arguments
    try:
        inputs = ["alphabet=", "shift=", "decode=", "encode="]
        opts, args = getopt(argv, "ha:d:e:s", inputs)
    except GetoptError:
        usage()
        exit(-1)

    # Check mutual exclusion between decode and encode options
    optnames = [opt[0] for opt in opts]
    if optnames in ("-d", "--decode") and optnames in ("-e", "--encode"):
        print(
            "ERROR: Options -d --decode and -e --encode are mutually exclusive")
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
            if int(arg) > len(alphabets):
                print("ERROR: select a valid alphabet")
                exit(-1)
            alphabet = alphabets[index]
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


if __name__ == '__main__':
    main(argv[1:])
