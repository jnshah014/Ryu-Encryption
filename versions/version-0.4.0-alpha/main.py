import tkinter as tk
from tkinter import messagebox
import verify

DEFAULT_FONT = "Helvetica 10"

root = tk.Tk()
root.title("Ryu Encryption (Version-0.4.0-alpha)")
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

    if verify.validation_check():  
      if enclevel == "1":
        print("Hello " + plaintext + " " + key)
      elif enclevel == "2":
        print("G'day mate " + plaintext + " " + key)
      elif enclevel == "3":
        print("Suiii " + plaintext + " " + key)
      ENCRYPT_ENTRY_CIPHERTEXT.delete(0, tk.END)
    else:
      messagebox.showerror("Re-enter Data", "The following data entries do not meet the following requirements. Please try again.")
      ENCRYPT_ENTRY_PLAINTEXT.delete(0, tk.END)
      ENCRYPT_ENTRY_KEY.delete(0, tk.END)
      ENCRYPT_ENTRY_ENCLEVEL.delete(0, tk.END)
      ENCRYPT_ENTRY_CIPHERTEXT.delete(0, tk.END)
    
  
  #Button Widget
  ENCRYPT_BUTTON_PERFORM = tk.Button(encrypt_screen, text="Perform\nEncryption", font=DEFAULT_FONT, command=execute_button_encrypt_algorithm).place(relx=0.64, rely=0.7, anchor=tk.CENTER)

def execute_button_decrypt_menu():
  decrypt_screen = tk.Toplevel()
  decrypt_screen.title("Decryption")
  decrypt_screen.geometry("750x250")
  decrypt_screen.resizable(False, False)

BUTTON_ENCRYPT = tk.Button(root, text="Encrypt", padx=500, pady=60, command=execute_button_encrypt_menu)
BUTTON_ENCRYPT.pack()

BUTTON_DECRYPT = tk.Button(root, text="Decrypt", padx=500, pady=60, command=execute_button_decrypt_menu)
BUTTON_DECRYPT.pack()


root.mainloop()
