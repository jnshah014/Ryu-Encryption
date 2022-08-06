
# Ryu Encryption

## 1) Introduction
This repository contains the all the current versions of the 'Ryu Encryption' software. 'Ryu Encryption' is a lightweight tool to encrypt small amounts of data and currently offers 3 encryption levels.

### 1.1) Description
My aim for this project was to create an encryption software that offered 3 different levels of security, each of which uses a different process to encrypt data (and conversely decrypt data). The strength (and computational power needed) of the algorithms increase with the level. I aimed to create a user interface using Python's `tkinter` module to allow the user to enter inputs and access outputs. Level 1 was to use a Caesar Cipher, Level 2 was to use a Grid Cipher and Level 3 was to use a Cumulative Cyclic Caesar Cipher (please see below for more information). I aim to set myself a total of 5 hours - an hour per day - to complete this project. Please see my checklist below of the subtasks I had to complete.

#### User-based Objective
To provide a lightweight and fast tool to encrypt small amounts of data.

#### Personal Objective
To learn how to create a GUI as well as full-stack development.

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
*N.B. This is the official name for this Cipher*

Caesar Cipher is a type of 'Substitution Cipher' whereby each character in the plaintext is replaced by a character that is a fixed number of positions down a character set. Normally, the character set used is the English Latin-script alphabet. My character set (shown below) is in the form of a python list called `ascii_accepted_list`; it contains the letters for the ascii values 32 `[SPACE]` up to the value 126 `~` (tilde). The user-inputed key is converted to a number between 1 and 94 by the `key_product.py` script. Although there are 95 characters in the list, this range ensures that the characters are at least shifted by 1 place. A range of 0 to 95 would allow 2/96ths of the shifts to be by 0 places, hence making the algorithm redundant. 

```
ascii_accepted_list = [chr(i) for i in range(32, 126 + 1)]
```

For more information visit [Wikipedia's](https://en.wikipedia.org/wiki/Caesar_cipher) page.

#### Level 2 (Grid Cipher)
*N.B. This is **not** the official name for this Cipher*

#### Level 3 (Cumulative Cyclic Caesar Cipher)
*N.B. This is **not** the official name for this Cipher*

This Cipher is similar to the Caesar Cipher but is more intricate and is best explained with an example. Let the `plaintext = "hello"` and the key (after processing by the `key_product.py` script) to be `key = 126798`. Then break `key` down into pairs of numbers: `12, 67, 98`. Next shift the whole of `plaintext` by the first number (`12`). Then shift the whole of `plaintext` again, apart from the first letter, by the second number (`67`). This pattern is repeated until there are no more pair of numbers, and the shift cycles back to the first number (`12`). This process repeats until the end of `plaintext`, in this case 5 times.

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

## 2) Current System in place
```python
def import(self):
  print(self.__init__)
  return nL
```

## 3) Plan
### 3.1) Structured English
### 3.2) Pseudocode
### 3.3) Program Flowchart

## 4) Code Explanation
### 4.1) Code
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
