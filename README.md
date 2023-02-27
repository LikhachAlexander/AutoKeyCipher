# AutoKeyCipher
Program that encodes and decodes using AutoKey cipher.

Before run install all requirements
`pip install requirements.txt`

Default names for output files: `encoded.txt` / `decoded.txt`.

Usage examples:

* `python main.py --help` - help

* `python main.py encode input.txt key.txt` - encoding with standard A-Z alphabet

* `python main.py decode encoded.txt key.txt` - decoding with standard A-Z alphabet

* `python main.py encode --alphabet alphabet.txt input.txt key.txt` - encoding with custom alphabet

* `python main.py decode --alphabet alphabet.txt encoded.txt key.txt` - decoding with custom alphabet
