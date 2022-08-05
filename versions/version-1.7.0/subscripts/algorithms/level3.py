#LEVEL 3
import subscripts.algorithms.subfunctions as fx


def execute(plaintext, key, dir=-1):

    ciphertext = ""

    key_len = len(key)
    origin = fx.ascii_accepted_list
    termin = fx.execute_list_rotation(origin, 0)

    for i in range(0, len(plaintext)):
        _ = ((10 * key[i % key_len][0]) + key[i % key_len][1]) % 95
        termin = fx.execute_list_rotation(termin, (_ * dir))

        ind = origin.index(plaintext[i])
        ciphertext += termin[ind]

    return ciphertext
