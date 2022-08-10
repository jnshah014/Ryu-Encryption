
ascii_accepted_list = [chr(i) for i in range(32, 126 + 1)]

ascii_accepted_grid = [
  [chr(i) for i in range(32, 50 + 1)],
  [chr(i) for i in range(51, 69 + 1)],
  [chr(i) for i in range(70, 88 + 1)],
  [chr(i) for i in range(89, 107 + 1)],
  [chr(i) for i in range(108, 127)],
]

#List Rotation Designed by Sup#2.0
#GitHub: https://github.com/Sup2point0
def execute_list_rotation(source, shift):
  return source[-shift:] + source[:-shift]