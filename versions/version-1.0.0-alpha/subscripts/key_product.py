
#Script aim is to take a key and turn it into a secondary input for an encryption module

def return_key_product(key, enclevel):
  
  sum = 0
  for i in range(0, len(key)):
    sum += ord(key[i])

  if enclevel