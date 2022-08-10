import tkinter as tk
from tkinter import messagebox

import subscripts.verify as verify
import subscripts.key_product as kp

import subscripts.algorithms.level1 as level1

DEFAULT_FONT = "Helvetica 10"

root = tk.Tk()
root.title("Ryu Encryption (Version-1.1.0-alpha)")
root.geometry("500x285")
root.resizable(False, False)

  
def execute_button_encrypt_menu():
  encrypt_screen = tk.Toplevel()
  encrypt_screen.title("Encryption")
  encrypt_screen.geometry("500x285")
  encrypt_screen.resizable(False, False)
  
  #Label Widget
  ENCRYPT_LABEL_PLAINTEXT = tk.Label(encrypt_screen, text="INPUT\nPlaintext", font=DEFAULT_FONT).place(relx=0.15, rely=0.1, anchor=tk.CENTER)
  ENCRYPT_LABEL_KEY = tk.Label(encrypt_screen, text="INPUT\nKey", font=DEFAULT_FONT).place(relx=0.15, rely=0.3, anchor=tk.CENTER)
  ENCRYPT_LABEL_ENCLEVEL = tk.Label(encrypt_screen, text="INPUT\nEncryption Level", font=DEFAULT_FONT).place(relx=0.15, rely=0.5, anchor=tk.CENTER)
  ENCRYPT_LABEL_CIPHERTEXT = tk.Label(encrypt_screen, text="OUTPUT\nCiphertext", font=DEFAULT_FONT).place(relx=0.15, rely=0.9, anchor=tk.CENTER)

  #Entry Widget
  ENCRYPT_ENTRY_PLAINTEXT = tk.Entry(encrypt_screen, width=35)
  ENCRYPT_ENTRY_KEY = tk.Entry(encrypt_screen, width=35)
  ENCRYPT_ENTRY_ENCLEVEL = tk.Entry(encrypt_screen, width=35)
  ENCRYPT_ENTRY_CIPHERTEXT = tk.Entry(encrypt_screen, width=35)

  ENCRYPT_ENTRY_PLAINTEXT.place(relx=0.32, rely=0.1, anchor=tk.W)
  ENCRYPT_ENTRY_KEY.place(relx=0.32, rely=0.3, anchor=tk.W)
  ENCRYPT_ENTRY_ENCLEVEL.place(relx=0.32, rely=0.5, anchor=tk.W)
  ENCRYPT_ENTRY_CIPHERTEXT.place(relx=0.32, rely=0.9, anchor=tk.W)

  def execute_button_encrypt_algorithm():
    plaintext = ENCRYPT_ENTRY_PLAINTEXT.get()
    key = ENCRYPT_ENTRY_KEY.get()
    enclevel = ENCRYPT_ENTRY_ENCLEVEL.get()
    ciphertext = ""

    if verify.validation_check(key, enclevel):
      shift = kp.return_key_product(key, int(enclevel))
      if int(enclevel) == 1:

        level1.encrypt(plaintext, shift)
        
      elif int(enclevel) == 2:
        pass
      elif int(enclevel) == 3:
        pass
      ENCRYPT_ENTRY_CIPHERTEXT.delete(0, tk.END)
    else:
      messagebox.showerror("Re-enter Data", "The following data entries do not meet the following requirements. Please try again.")
      ENCRYPT_ENTRY_PLAINTEXT.delete(0, tk.END)
      ENCRYPT_ENTRY_KEY.delete(0, tk.END)
      ENCRYPT_ENTRY_ENCLEVEL.delete(0, tk.END)
      ENCRYPT_ENTRY_CIPHERTEXT.delete(0, tk.END)
    
  
  #Button Widget
  ENCRYPT_BUTTON_PERFORM = tk.Button(encrypt_screen, text="Perform\nEncryption", font=DEFAULT_FONT, command=execute_button_encrypt_algorithm).place(relx=0.64, rely=0.7, anchor=tk.CENTER)













"""
def execute_button_decrypt_menu():
  decrypt_screen = tk.Toplevel()
  decrypt_screen.title("Decryption")
  decrypt_screen.geometry("500x285")
  decrypt_screen.resizable(False, False)
  
  #Label Widget
  DECRYPT_LABEL_CIPHERTEXT = tk.Label(decrypt_screen, text="INPUT\nCiphertext", font=DEFAULT_FONT).place(relx=0.15, rely=0.1, anchor=tk.CENTER)
  DECRYPT_LABEL_KEY = tk.Label(decrypt_screen, text="INPUT\nKey", font=DEFAULT_FONT).place(relx=0.15, rely=0.3, anchor=tk.CENTER)
  DECRYPT_LABEL_ENCLEVEL = tk.Label(decrypt_screen, text="INPUT\nEncryption Level", font=DEFAULT_FONT).place(relx=0.15, rely=0.5, anchor=tk.CENTER)
  DECRYPT_LABEL_PLAINTEXT = tk.Label(decrypt_screen, text="OUTPUT\nPlaintext", font=DEFAULT_FONT).place(relx=0.15, rely=0.9, anchor=tk.CENTER)

  #Entry Widget
  DECRYPT_ENTRY_PLAINTEXT = tk.Entry(decrypt_screen, width=35)
  DECRYPT_ENTRY_KEY = tk.Entry(decrypt_screen, width=35)
  DECRYPT_ENTRY_ENCLEVEL = tk.Entry(decrypt_screen, width=35)
  DECRYPT_ENTRY_CIPHERTEXT = tk.Entry(decrypt_screen, width=35)  

  DECRYPT_ENTRY_PLAINTEXT.place(relx=0.32, rely=0.9, anchor=tk.W)
  DECRYPT_ENTRY_KEY.place(relx=0.32, rely=0.3, anchor=tk.W)
  DECRYPT_ENTRY_ENCLEVEL.place(relx=0.32, rely=0.5, anchor=tk.W)
  DECRYPT_ENTRY_CIPHERTEXT.place(relx=0.32, rely=0.1, anchor=tk.W)

  def execute_button_decrypt_algorithm():
    ciphertext = DECRYPT_ENTRY_CIPHERTEXT.get()
    key = DECRYPT_ENTRY_KEY.get()
    enclevel = DECRYPT_ENTRY_ENCLEVEL.get()
    plaintext = ""

    if verify.validation_check(key, enclevel):
      if enclevel == "1":
        print("1 " + ciphertext + " " + key)
      elif enclevel == "2":
        print("2 " + ciphertext + " " + key)
      elif enclevel == "3":
        print("3 " + ciphertext + " " + key)
      DECRYPT_ENTRY_PLAINTEXT.delete(0, tk.END)
    else:
      messagebox.showerror("Re-enter Data", "The following data entries do not meet the following requirements. Please try again.")
      DECRYPT_ENTRY_CIPHERTEXT.delete(0, tk.END)
      DECRYPT_ENTRY_KEY.delete(0, tk.END)
      DECRYPT_ENTRY_ENCLEVEL.delete(0, tk.END)
      DECRYPT_ENTRY_PLAINTEXT.delete(0, tk.END)
  
  
  #Button Widget
  DECRYPT_BUTTON_PERFORM = tk.Button(decrypt_screen, text="Perform\nDecryption", font=DEFAULT_FONT, command=execute_button_decrypt_algorithm).place(relx=0.64, rely=0.7, anchor=tk.CENTER)
"""  

BUTTON_ENCRYPT = tk.Button(root, text="Encrypt", padx=500, pady=60, command=execute_button_encrypt_menu)
BUTTON_ENCRYPT.pack()

BUTTON_DECRYPT = tk.Button(root, text="Decrypt", padx=500, pady=60, command=execute_button_decrypt_menu)
BUTTON_DECRYPT.pack()


root.mainloop()
