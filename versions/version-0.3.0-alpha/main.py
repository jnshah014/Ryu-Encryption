import tkinter as tk

DEFAULT_FONT = "Helvetica 12"

root = tk.Tk()
root.title("Ryu Encryption (Version-0.2.0-alpha)")
root.geometry("500x285")
root.resizable(False, False)

def execute_button_encrypt():
  encrypt_screen = tk.Toplevel()
  encrypt_screen.title("Encryption")
  encrypt_screen.geometry("750x250")
  encrypt_screen.resizable(False, False)

  #Label Widget
  ENCRYPT_LABEL_PLAINTEXT = tk.Label(encrypt_screen, text="INPUT\nPlaintext", font=DEFAULT_FONT).place(relx=0.05, rely=0, anchor=tk.NW)
  ENCRYPT_LABEL_KEY = tk.Label(encrypt_screen, text="INPUT\nKey", font=DEFAULT_FONT).place(relx=0.25, rely=0, anchor=tk.NW)
  ENCRYPT_LABEL_ENCLEVEL = tk.Label(encrypt_screen, text="INPUT\nEncryption Level", font=DEFAULT_FONT).place(relx=0.40, rely=0, anchor=tk.NW)
  ENCRYPT_LABEL_CIPHERTEXT = tk.Label(encrypt_screen, text="OUTPUT\nCiphertext", font=DEFAULT_FONT).place(relx=0.80, rely=0, anchor=tk.NW)

  #Entry Widget
  ENCRYPT_ENTRY_PLAINTEXT = tk.Entry(encrypt_screen).place(relx=0.05, rely=0.5, anchor=tk.NW)
  

def execute_button_decrypt():
  decrypt_screen = tk.Toplevel()
  decrypt_screen.title("Decryption")
  decrypt_screen.geometry("750x250")
  decrypt_screen.resizable(False, False)

BUTTON_ENCRYPT = tk.Button(root, text="Encrypt", padx=500, pady=60, command=execute_button_encrypt)
BUTTON_ENCRYPT.pack()

BUTTON_DECRYPT = tk.Button(root, text="Decrypt", padx=500, pady=60, command=execute_button_decrypt)
BUTTON_DECRYPT.pack()

"""
window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()
"""
root.mainloop()
