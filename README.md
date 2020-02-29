# BFShift
A super simple encode/decode/bruteforce script for shift ciphers by @AleDiBen & @Omnicrist.

## Description
This Python 3 script to encode/decode/bruteforce arbitrary strings using a shift cipher (i.e. Caesar Cipher, ROT-13, etc.).

## Features
The following features are supported
- [x] Encode/Decode a message
- [x] Perform a Bruteforce attack using different alphabets and/or shift amounts
- [x] Specify your own custom alphabet
- [x] Load a custom alphabet from a text file
- [x] Specify a flag format in order to filter results
- [x] Run the script in Debug Mode
- [ ] Multi-threading

## Supported Alphabets
0. !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~
1. 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
2. ABCDEFGHIJKLMNOPQRSTUVWXYZ
3. abcdefghijklmnopqrstuvwxyz
4. abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
5. ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
6. 0123456789abcdefABCDEF
7. !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~

## Supported Shifts
From 1 to chosen alphabet lenght minus one.

## Examples
> Linux Version: encoding and decoding a message
```
python3 bfshift.py -a 1 -s 14 -e 'this is a message'
HvwG wG o AsGGous

python3 bfshift.py -a 1 -s 14 -d 'HvwG wG o AsGGous'
this is a message
```

> Windows Version (cmd.exe): encoding and decoding a message
```
python.exe bfshift.py -a 1 -s 14 -e -m "this is a message"
HvwG wG o AsGGous

python.exe bfshift.py -a 1 -s 14 -d -m "HvwG wG o AsGGous"
this is a message
```

*...may the security be with you...*
