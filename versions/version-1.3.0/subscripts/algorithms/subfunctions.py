
ascii_accepted = [chr(i) for i in range(32, 126 + 1)]

#List Rotation Designed by Sup#2.0
#GitHub: https://github.com/Sup2point0
def execute_list_rotation(source, shift):
  return source[-shift:] + source[:-shift]