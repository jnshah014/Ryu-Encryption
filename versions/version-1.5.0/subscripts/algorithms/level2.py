#LEVEL 2
import subscripts.algorithms.subfunctions as fx

def execute(plaintext, key, dir=-1):  #-1 encrypt; 1 decrypt

    ciphertext = ""

    origin = fx.ascii_accepted_grid

    termin = fx.execute_list_rotation(origin, (dir * key[0]))  #First rotation
    for i in range(0, len(termin)):
        termin[i] = fx.execute_list_rotation(termin[i], (dir * key[1]))

    for i in range(0, len(plaintext)):
        for j in range(0, len(origin)):
            for k in range(0, len(origin[j])):
                if plaintext[i] == origin[j][k]:
                    ciphertext += termin[j][k]

    return ciphertext
