#LEVEL 1
import subscripts.algorithms.subfunctions as fx


def execute(plaintext, key):

    ciphertext = ""

    origin = fx.ascii_accepted_list
    termin = fx.execute_list_rotation(origin, key)

    for i in range(0, len(plaintext)):
        _ = origin.index(plaintext[i])
        ciphertext += termin[_]

    return ciphertext
