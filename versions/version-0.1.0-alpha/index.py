
import functions

ascii_accepted = [chr(i) for i in range(32, 126 + 1)]

#ascii_accepted : list of ascii characters
#ascii_shifted : shifted ascii characters
#self.user_input : user's input
#self.user_key : user's key

#shift : if shift exceeds len(ascii_accepted), this modifies the data given by the key

class Encrypt():
  
  def __init__(self, user_input:str, user_key:str):
    self.user_input = user_input
    self.user_key = user_key
    
  def caesar_cipher(self):
    _ = ""
    #configures shifted list
    ascii_shifted = ascii_accepted
    functions.rotate_list(ascii_shifted, self.user_key)
    
    for char in self.user_input:
      _ += functions.replace_char(char, ascii_accepted, ascii_shifted)
    return _

print(Encrypt("hello", 3).caesar_cipher())    
    