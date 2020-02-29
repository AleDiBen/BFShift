from enum import Enum

class Parameters(Enum):
    ALPHABET = 0
    CUSTOM_ALPHABET = 1
    DECODE = 2
    ENCODE = 3
    HELP = 4
    MESSAGE = 5
    SHIFT = 6
    BRUTEFORCE_ALL = 7
    BRUTEFORCE_ALPHABET = 8
    BRUTEFORCE_SHIFT = 9
    DEBUG = 10
    FLAG_FORMAT = 11

            # -2 : Compatibility logic error
            # -1 : Same parameter
            # 0 : Compatibility fatal error
            # 1 : Ok
            #  alphabet, custom-a, decode, encode, help, message, shift, bf-all, bf-alpha, bf-shift, debug, flag-fmt
matrix = [
                [-1,       -2,       1,      1,     0,      1,      1,      0,      0,          1,      1,     1], #alphabet
                [-2,       -1,       1,      1,     0,      1,      1,      0,      0,          1,      1,     1], #custom-a
                [1,         1,      -1,     -2,     0,      1,      1,      0,      0,          0,      1,     0], #decode
                [1,         1,      -2,     -1,     0,      1,      1,      0,      0,          0,      1,     0], #encode
                [0,         0,       0,      0,    -1,      0,      0,      0,      0,          0,      0,     0], #help
                [1,         1,       1,      1,     0,     -1,      1,      1,      1,          1,      1,     1], #message
                [1,         1,       1,      1,     0,      1,     -1,      0,      1,         -2,      1,     1], #shift
                [0,         0,       0,      0,     0,      1,      0,     -1,     -2,         -2,      1,     1], #bf-all
                [0,         0,       0,      0,     0,      1,      1,     -2,     -1,         -2,      1,     1], #bf-alpha
                [1,         1,       0,      0,     0,      1,     -2,     -2,     -2,         -1,      1,     1], #bf-shift
                [1,         1,       1,      1,     0,      1,      1,      1,      1,          1,     -1,     1], #debug
                [1,         1,       0,      0,     0,      1,      1,      1,      1,          1,      1,    -1]  #flag-fmt
            ]