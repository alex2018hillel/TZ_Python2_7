import re

class New_Cashier_Does_Not_Know_About_Space_or_Shift():

    text = u"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"
    strings = ['burger', 'fries', 'chicken', 'pizza', 'sandwich', 'milkshake', 'coke', ]
    new_string = " "

    for string in strings:
        regex = re.compile(string)

        for match in re.finditer(regex, text):
            s = match.start()
            e = match.end()
            word =text[s:e]
            word = word.title()
            new_string = new_string + word + " "
    print(new_string)
