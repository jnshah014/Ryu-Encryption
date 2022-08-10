
#List turns to list rotated by N places
def rotate_list(a_list, shift):
  net_shift = abs(shift) % len(a_list)
  for i in range(net_shift):
    if shift < 0:
      popped = a_list.pop(-1)
      a_list.insert(0, popped)
    if shift > 0:
      popped = a_list.pop(0)
      a_list.append(popped)

def replace_char(char, a_list, b_list):
  index = a_list.index(char)
  new_char = b_list[index]
  return new_char
