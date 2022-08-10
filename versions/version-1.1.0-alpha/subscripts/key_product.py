
#Script aim is to take a key and turn it into a secondary input for an encryption module

def return_key_product(key, enclevelnum):
  
  sum = 0
  for i in range(0, len(key)):
    sum += ord(key[i])

  if enclevelnum == 1:
    
    if sum % 95 == 0:
      return 1
    else:
      return sum % 95
      
  elif enclevelnum == 2:
    pass
  elif enclevelnum == 3:
    pass