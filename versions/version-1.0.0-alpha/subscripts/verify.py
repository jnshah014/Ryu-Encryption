
#Enclevel has to be 1, 2 or 3
#Key length has to be greater than / equal to 8 characters
#There must be at least 1 non-alphanumeric character

non_alphanumeric_char = [chr(i) for i in range(33, 47 + 1)] + [chr(j) for j in range(58, 64 + 1)] + [chr(k) for k in range(91, 96 + 1)] + [chr(l) for l in range(123, 126 + 1)] + ['£']

def validation_check(k, enc):
  non_alpha_in = False
  if enc in ["1", "2", "3"]:
    if len(k) >= 8:

      for i in range(0, len(k)):
        if k[i] in non_alphanumeric_char:
          non_alpha_in = True

      return non_alpha_in
        
    else:
      return False
  else:
    return False
