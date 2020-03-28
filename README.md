# BFShift
A super simple encode/decode/bruteforce script for shift ciphers by @AleDiBen & @Omnicrist.

## Description
This Python 3 script to encode/decode/bruteforce arbitrary strings using a shift cipher (i.e. Caesar Cipher, ROT-13, etc.).

## Features / TO-DO
The following features are supported
- [x] Encode/Decode a message
- [x] Perform a Bruteforce attack using different alphabets and/or shift amounts
- [x] Specify your own custom alphabet
- [x] Specify a flag format in order to filter results
- [x] Run the script in Debug Mode
- [ ] Multi-threading? May be useless

## Supported Alphabets
Code | Alphabet
----- | ---------
0 | [SPACE]!"#$%&'()\*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^\_\`abcdefghijklmnopqrstuvwxyz{\|}~
1 | 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()\*+,-./:;<=>?@[\\]^\_\`{\|}~
2 | ABCDEFGHIJKLMNOPQRSTUVWXYZ
3 | abcdefghijklmnopqrstuvwxyz
4 | abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
5 | ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
6 | 0123456789abcdefABCDEF

## Supported Shifts
From 1 to chosen alphabet lenght minus one.

## Examples
> Linux Version: encoding and decoding a message
```
python3 bfshift.py -m this_is_a_message
\"uv!lv!lnlzr!!ntr

python3 bfshift.py -d -m '"uv!lv!lnlzr!!ntr'
this is a message

python3 bfshift.py -a 3 --bf-shift -m 'ozhshi{Aopz_pz_h_tlzzhnl}'
nygrgh{znoy_oy_g_skyygmk}
mxfqfg{ymnx_nx_f_rjxxflj}
lwepef{xlmw_mw_e_qiwweki}
...
rCkvkl{DrsC_sC_k_woCCkqo}
qBjujk{CqrB_rB_j_vnBBjpn}
pAitij{BpqA_qA_i_umAAiom}

python3 bfshift.py --bf-alphabets -s 7 --flag-format 'hsalab{' -m 'ozhshi{Aopz_pz_h_tlzzhnl}'
hsalab{this_is_a_message}
hsalab{this_is_a_message}
hsalab{this_is_a_message}
```

> Windows Version (cmd.exe): encoding and decoding a message
```
python.exe bfshift.py -m this_is_a_message
\"uv!lv!lnlzr!!ntr

python.exe bfshift.py -a 3 --bf-shift -m "ozhshi{Aopz_pz_h_tlzzhnl}"
nygrgh{znoy_oy_g_skyygmk}
mxfqfg{ymnx_nx_f_rjxxflj}
lwepef{xlmw_mw_e_qiwweki}
...
rCkvkl{DrsC_sC_k_woCCkqo}
qBjujk{CqrB_rB_j_vnBBjpn}
pAitij{BpqA_qA_i_umAAiom}

python.exe bfshift.py --bf-alphabets -s 7 --flag-format "hsalab{" -m "ozhshi{Aopz_pz_h_tlzzhnl}"
hsalab{this_is_a_message}
hsalab{this_is_a_message}
hsalab{this_is_a_message}

```

*...may the security be with you...*
