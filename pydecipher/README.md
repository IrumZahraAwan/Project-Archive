pydecipher
==========

A Python (2 & 3) library that attempts different encryption algorithms to decrypt a cipher-text. (Currently limited to Ceasarian Shift Cipher and Vigenère Cipher)

The key component of this program is an evaluation program that determines the similarities between a given string and the expected language (without using a dictionary of words). It currently achieves this by comparing the string's letter frequency to the expected letter frequency.

With this function, the program is then able to attempt to various methods of deciphering to find a seemingly English (or any supported language) sentence.

For Ceasarian Shift, it naively compares all 26 possible rotations. For Vigenère, it works out the most likely length of the key by performing a pattern analysis, splits the text up according to the length and passes each component to the Ceasarian Shift function.

To Do:

1. Support an increasing number of encryption schemes.
2. Allow for further assistance from the user. Eg, if part of the key is known.
3. Modularise each set of decryption functions further.

To install as a module (may be out of date while in development - best to use GitHub) [REMOVED - no longer available from pip]:
```bash
pip install pydecipher
```

To install as a script:
https://github.com/noahingham/pydecipher/archive/master.zip

Usage:
```bash
cipher.py [-l language] [-n number of results] [-f path/to/file]
```

As a module:
```python
import pydecipher
plaintext = pydecipher.shift(ciphertext)
othertext = pydecipher.vigenere(ciphertext)
```

Tested in Python 2.7.2 and Python 3.3.2, but it should work with other versions.

See it in action:

![alt tag](http://i.imgur.com/mY0jjP7.png)
