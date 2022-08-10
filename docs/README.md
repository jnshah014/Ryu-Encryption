
# Ryu Encryption

## 1) Introduction
This repository contains the all the current versions of the 'Ryu Encryption' software. 'Ryu Encryption' is a lightweight tool to encrypt small amounts of data and currently offers 3 encryption levels.

### 1.1) Description
My aim for this project was to create an encryption software that offered 3 different levels of security, each of which uses a different process to encrypt data (and conversely decrypt data). The strength (and computational power needed) of the algorithms increase with the level. I aimed to create a user interface using Python's `tkinter` module to allow the user to enter inputs and access outputs. Level 1 was to use a Caesar Cipher, Level 2 was to use a Grid Cipher and Level 3 was to use a Cumulative Cyclic Caesar Cipher (please see below for more information). I aimed to set myself a total of 5 hours - an hour per day - to complete this project. Please see my checklist below of the subtasks I had to complete.

#### User-based Objective
To provide a lightweight and fast tool to encrypt small amounts of data.

#### Personal Objective
To learn how to create a GUI as well learning full-stack development.

### 1.2) Subtasks
- Frontend GUI
  - Main Menu
  - Encryption Screen
  - Decryption Screen
  - Input / Output Fields
- Input Validation Checks
- Backend Algorithms
  - Level 1
  - Level 2
  - Level 3
  - Character Shift Function 

### 1.3) Encryption Levels
#### Level 1 (Caesar Cipher)
N.B. This is the official name for this Cipher

Caesar Cipher is a type of 'Substitution Cipher' whereby each character in the plaintext is replaced by a character that is a fixed number of positions down a character set. Normally, the character set used is the English Latin-script alphabet. My character set (shown below) is in the form of a python list called `ascii_accepted_list`; it contains the letters for the ascii values 32 `[SPACE]` up to the value 126 `~` (tilde) and my program executes an error message if there are characters outside this range. The user-inputed key is converted to a number between 1 and 94 by the `key_product.py` script. Although there are 95 characters in the list, this range ensures that the characters are at least shifted by 1 place. A range of 0 to 95 would allow 2/96ths of the shifts to be by 0 places, hence making the algorithm redundant. 

```python
ascii_accepted_list = [chr(i) for i in range(32, 126 + 1)]
```

For more information visit [Wikipedia's](https://en.wikipedia.org/wiki/Caesar_cipher) page.

#### Level 2 (Grid Cipher)
N.B. This is **not** the official name for this Cipher

This Cipher is best explained with an example.

The orginal character set would appear like a 2-dimensional grid like below:
```
[a b c]
[d e f]
[g h i]
```
The key (after processing by the `key_product.py` script) appears as a tuple of two numbers. Eg: `(2, 1)`. The first number, shifts the letters **up** by the number of places represented by the number. The second number shifts the letters **right** by the number of places represented by the number.
```
Initial     New
[a b c]     [i g h]
[d e f] --> [c a b]
[g h i]     [f d e]
```
Then each letter in the plaintext becomes the letter that is now in its place in the new grid. Eg: `a --> i`, `b --> g`, `c --> h` etc.

#### Level 3 (Cumulative Cyclic Caesar Cipher) - READ AGAIN AND EXPLAIN BETTTER
N.B. This is **not** the official name for this Cipher

This Cipher is similar to the Caesar Cipher but is more intricate and is best explained with an example. Let the `plaintext = "hello"` and the key (after processing by the `key_product.py` script) to be `key = 126798`. Then break `key` down into pairs of numbers: `12, 67, 98`. Next shift the whole of `plaintext` by the first number (`12`). Then shift the whole of `plaintext` again, apart from the first letter, by the second number (`67`). This pattern is repeated until there are no more pair of numbers, and the shift cycles back to the first number (`12`). This process repeats until the end of `plaintext`, in this case 5 times.

Essentially:
1. "h" is shifted by 12
2. "e" is shifted by 12 + 67
3. "l" is shifted by 12 + 67 + 98
4. "l" is shifted by 12 + 67 + 98 + 12
5. "o" is shifted by 12 + 67 + 98 + 12 + 67

### 1.4) User Requirements
- GUI
  - Ability for the User to access the Main Screen
  - Ability for the User to access the Encryption Screen
  - Ability for the User to access the Decryption Screen
  - Inability for the User to resize any Screens
- Validation
  - Ability for the User to recieve a Warning when their Key does not match the following conditions:
    - 8 characters or over in length
    - Contains at least 1 non-alphanumeric character
- Algorithms
  - Ability for the User to Encrypt Data using Level 1
  - Ability for the User to Decrypt Data using Level 1
  - Ability for the User to Encrypt Data using Level 2
  - Ability for the User to Decrypt Data using Level 2
  - Ability for the User to Encrypt Data using Level 3
  - Ability for the User to Decrypt Data using Level 3

___

## 2) Current System in place and users
There are many different encryption algorithms in place, such as MD5 to verify file integrity, SHA-256 to allow the blockchain to function and TripleDES in ATM machines. All of which are used commonly by a large amount of people. However, many use complex algorithms which take a lot of computational power and the Ryu Encryption Software poses an alternative. Although the algorithms are open source, each encryption / decryption requires **2 different inputs** allowing for security with the input text having no size restriction and the key having limited restrictions (some to ensure that the key is hard to guess). This counters rainbow tables whilst still being lightweight and rapid.

___

## 3) System Design Plan
Below is my plan for the first encryption algorithm (excluding 'GUI Input / Output Fields' and 'Key Processing').

### 3.1) Structured English
1. `ascii_accepted` is a list that has the ascii values from 32 up to 126
2. **INPUT** `plaintext` and `key`
3. `ciphertext` is set to a blank string
4. set `ascii_shifted` to `ascii_accepted`
5. The following loop runs `key` times on `ascii_shifted`:
    - Take the last of the list and store it in `_` (a temporary variable)
    - Each element in the list should be assigned to the index of the next element in the list
    - The first element of the list should be set as `_`
6. The following loop runs the length of `plaintext` number of times:
    - Set `i` as the loop counter
    - Find the index of `i`th letter in `plaintext` in `ascii_accepted` via a Linear Search or Python's `.index()` method
    - Add to `ciphertext` the letter that appears in the this index in the `ascii_shifted` list
7. **OUTPUT** `ciphertext`    

### 3.2) Pseudocode (Cambridge International A & AS Level Syntax)
N.B. `ascii_val()` denotes a function like Python's `chr()` where a number is converted to an ASCII character. It is not part of Cambridge International's Syntax but it is necessary for this program to function.
```python
DECLARE ascii_accepted : ARRAY[0:94] OF CHAR
DECLARE ascii_shifted : ARRAY[0:94] OF CHAR
DECLARE plaintext : STRING
DECLARE ciphertext : STRING
DECLARE key : INTEGER

DECLARE _ : STRING
DECLARE i: INTEGER
DECLARE j : INTEGER

FOR i ⬅ 32 TO 126
  ascii_accepted[i - 32] ⬅ ascii_val(i)
  ascii_shifted[i - 32] ⬅ ascii_val(i)
NEXT i

ciphertext = ""

INPUT plaintext
INPUT key

_ = ""
FOR i ⬅ 1 TO key
  _ = ascii_shifted[94]
  FOR j 0 TO 93 THEN
    ascii_shifted[j + 1] ⬅ ascii_shifted[j]
  NEXT j
  ascii_shifted[0] ⬅ _
NEXT i

FOR i ⬅ 1 TO LEN(plaintext)
  FOR j ⬅ 0 TO 94
    IF ascii_accepted[j] == plaintext[i - 1] THEN
      ciphertext ⬅ ciphertext + ascii_shifted[j]
    ENDIF
  NEXT j
NEXT i

OUTPUT ciphertext

```

### 3.3) Program Flowchart
N.B. The following flowchart was scripted using the **Pilot V5 Assorted Hi-techpoint pens**. Pick them up from Amazon [here](https://www.amazon.co.uk/Assorted-Colour-Hi-Tecpoint-Rollerball-Colours/dp/B00LXANW2O/ref=sr_1_6?crid=9JKPUDX1VSDU&keywords=v5%2Bhi-tecpoint&qid=1660127791&sprefix=v5%2Bhi-tecpoint%2Caps%2C62&sr=8-6).

![Ryu Encryption Program Flowchart by jnshah014](https://github.com/jnshah014/Ryu-Encryption/blob/main/docs/program_flowchart.jpg "Ryu Encryption Program Flowchart by jnshah014")
___

## 4) Python Scripts
### 4.1) Code Explanation
#### 4.1.1) Script Hierarchy
- `main.py` - the script that is run, importing Python's `tkinter` module to render and process the GUI
- `subscripts` - contains all the backend scripts
  - `key_product.py` - processes the user-inputted key to one that can be interpreted by the encryption algorithms
  - `verify.py` - contains a function that returns `True` if all the user data-entry requirements are met
  - `algorithms` - contains all the encryption algorithms
    - `level1.py`
    - `level2.py`
    - `level3.py`
    - `subsfunctions.py` - contain functions that have processes that are common to all three encryption algorithms

```python
#main.py
import tkinter as tk
from tkinter import messagebox

import subscripts.verify as verify
import subscripts.key_product as kp

import subscripts.algorithms.level1 as level1
import subscripts.algorithms.level2 as level2
import subscripts.algorithms.level3 as level3
```

### 4.2) Changelog
- **Version-0.1.0-alpha:** Tested with some Caesar Cipher Functions
- **Version-0.2.0-alpha:** Created Home-Screen, Trialed Encryption-Screen
- **Version-0.3.0-alpha:** Updated Encryption-Screen
- **Version-0.4.0-alpha:** Input Validation
- **Version-0.5.0-alpha:** Updated Decryption-Screen
- **Version-1.0.0-alpha:** Started derivation of the key's product
- **Version-1.1.0-alpha:** Worked on derivation of the key's product
- **Version-1.2.0:** Completed Level 1 Encryption
- **Version-1.3.0:** Started Level 1 Decryption
- **Version-1.4.0:** Finished Level 1
- **Version-1.5.0:** Finished Level 2
- **Version-1.6.0:** Started Level 3
- **Version-1.7.0:** Finished Level 3 by reworking `key_product.py`

## 5) Error Testing

## 6) Review
### 6.1) Feedback from other users
### 6.2) Success of the project
### 6.3) Plans for the future
