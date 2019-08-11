import string
from itertools import islice, imap, repeat
from os import urandom

class Random_data:

    def rand_string(self):
        chars = set(string.ascii_uppercase + string.digits)
        char_gen = (c for c in imap(urandom, repeat(1)) if c in chars)
        return ''.join(islice(char_gen, 10))
        pass

    randoms_a = [rand_string(10) for x in range(0, 15)]
    randoms_b = [rand_string(10) for x in range(0, 15)]


    # Write to *.txt file (option)
    with open(r"C:\1.txt", "w") as file:
        for line in randoms_a:
            file.write(line + '\n')
    with open(r"C:\2.txt", "w") as file:
        for line in randoms_b:
            file.write(line + '\n')
    for i in range(len(randoms_b)):
        theme = randoms_a[i]
        text = randoms_b[i]
