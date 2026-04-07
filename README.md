# Caesar Cipher Tool 🔐

A command-line based Caesar Cipher encryption and decryption tool built in Python. Supports both console input and file-based batch processing.

## Features
- Encrypt and decrypt messages using a custom shift number
- Read input from console or process an entire text file
- Handles non-alphabetic characters (spaces, numbers, symbols) without changes
- Input validation for mode selection and file existence
- Writes batch results to `result.txt`

## How to Run

Make sure Python 3 is installed, then run:
```bash
python Caesar.py
```

## How to Use

1. Choose to **encrypt (e)** or **decrypt (d)**
2. Choose input method — **console (c)** or **file (f)**
3. Enter your message or filename
4. Enter a shift number
5. View your result or check `result.txt` for file output

## Example

| Input | Shift | Output |
|-------|-------|--------|
| HELLO WORLD | 4 | LIPPS ASVPH |
| LIPPS ASVPH | 4 | HELLO WORLD |

## Technologies Used
- Python 3
- Core concepts: Functions, Loops, File I/O, String Manipulation

## Author
Dewmi Umegha
