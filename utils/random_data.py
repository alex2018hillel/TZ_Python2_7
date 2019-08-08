import string
from itertools import islice, imap, repeat
from os import urandom

#def rand_string(param):
    #chars = set(string.ascii_uppercase + string.digits)
    #char_gen = (c for c in imap(urandom, repeat(1)) if c in chars)
    #return ''.join(islice(char_gen, 10))
    #print(''.join(islice(char_gen, 10)))
    #pass


class Random_data:

    def rand_string(self):
        chars = set(string.ascii_uppercase + string.digits)
        char_gen = (c for c in imap(urandom, repeat(1)) if c in chars)
        return ''.join(islice(char_gen, 10))
        pass


