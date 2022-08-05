#LEVEL 3
import subscripts.algorithms.subfunctions as fx


def execute(plaintext, key, dir=-1):

    ciphertext = ""

    origin = fx.ascii_accepted_list
    termin = fx.execute_list_rotation(origin, 0)

    #Shifts are compounded. Eg: 1231 will shift the first char by 12 and the next by 12 + 31 which is 43
    for i in range(1, len(plaintext)+1):
      _ = int((str(key)[(2 * a)-2]) + (str(key)[(2 * a)-1]))
      termin = fx.execute_list_rotation(termin, ((_ % 95) * dir))

      ind = origin.index(plaintext[i])
      ciphertext += termin[ind]

    return ciphertext
