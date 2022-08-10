#Script aim is to take a key and turn it into a secondary input for an encryption module

from math import floor

def return_key_product(key, enclevelnum):

  level2_upshift = 0
  level2_rightshift = 0
  
  sum = 0
  for i in range(0, len(key)):
    sum += ord(key[i])

  if enclevelnum == 1:
    
    if sum % 95 == 0:
      return 1
    else:
      return sum % 95
      
  elif enclevelnum == 2:
    if len(str(sum)) % 2 == 1: #odd length
      _ = floor(len(str(sum)) / 2)
    else:
      _ = (len(str(sum)) / 2)
    
    level2_upshift = int(str(sum)[0:_])
    level2_rightshift = int(str(sum)[_:])

    return ((level2_upshift % 4) + 1, (level2_rightshift % 18) + 1)
    
  elif enclevelnum == 3:
    pass