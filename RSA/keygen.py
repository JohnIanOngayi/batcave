#!/usr/bin/python3

import random
from euclid import euler

if __name__ == "__main__":
    def pick_random():
        range_p = random.randint(0, 10000)
        range_q = random.randint(0, 10000)
        
        while range_p != range_q:
            p = random.randint(0, range_p)
            q = random.randint(0, range_q)

        return p, q
    
    def key_gen():
        p, q = pick_random()
        n = p * q
        phi = (p - 1) * (q - 1)
        
        # to evaluate encryption
        e = random.randint(2, ((p - 1)(q - 1)))
        
        #to evaluate decryption
        max_ed = 1
        for i in range(1, (n * phi)):
            if (e * i) % phi == 1:
                if (e * i) > max_ed:
                    max_ed = (e * i)
                d = i
                
        return n, e, d
                
    
    def encrypter(string):
        n, e, d = key_gen()
        string_tuple = ()
        result_dict = {
            "keys": (n, e, d),
            "cipher": string_tuple
        }
        
        for character in string:
            #digits apply formula as is
            if character.isdigit():
                i = (character ** e) % n
                
            #letters change to ASCII digit apply formula then change to ASCII
            else:
                i = chr((ord(i) ** e) % n)
                
            y = list(result_dict["cipher"])
            y.append(i)
            result_dict["cipher"] = tuple(y)
            
        return result_dict
    
    def decyrptor(result_dict):
        n, e, d = result_dict["keys"]
        actual_text = ""
        
        for character in result_dict["cipher"]:
            #if digit apply formula as is
            if character.isdigit():
                decrypt = ((character ** d) % n) % 1
                text += decrypt * n
                
            else:
                decrypt = (((ord(character) ** d) % n) % 1)
                text += chr(decrypt * ord(character))
                
            return text