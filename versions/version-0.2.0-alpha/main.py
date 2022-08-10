
import functions

ascii_accepted = [chr(i) for i in range(32, 126 + 1)]

print(ascii_accepted)

ascii_shifted = ascii_accepted

functions.rotate_list(ascii_shifted, 5)

print(ascii_accepted)
print(ascii_shifted)
print(ascii_accepted)
