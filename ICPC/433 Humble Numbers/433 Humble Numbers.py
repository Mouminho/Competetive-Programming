import sys
limit = 5842
""" 'limit': die höchste Zahl, die wir betrachten werden"""
humble_numbers_liste = [0] * (limit + 1)
""" 'humble_numbers_liste' : liste aller humble numbers zwischen 1 und 5842, initialisiert mit nullen """
def generator():
    """ 'generator' : function to generate all humble numbers between 1 and 5842 by multiplications
    with the prime factors 2, 3, 5 & 7. """
humble_numbers_liste[1] = 1
""" value of first index is 1"""
mult2 = 1
""" 'mult2': index its value will be multiplicated with 2 """
mult3 = 1
""" 'mult3': index its value will be multiplicated with 3 """
mult5 = 1
""" 'mult5': index its value will be multiplicated with 5 """
mult7 = 1
""" 'mult7': index its value will be multiplicated with 7 """
for i in range(2, limit + 1): 
    """
    for loop to calculate the values of the indexes of list 'humble_numbers_liste'
    """
    humble_numbers_liste[i] = min(min(2 * humble_numbers_liste[mult2], 3 * humble_numbers_liste[mult3]), min(5 * humble_numbers_liste[mult5], 7 * humble_numbers_liste[mult7]))
    if humble_numbers_liste[i] == 2 * humble_numbers_liste[mult2]:
        mult2 += 1
    if humble_numbers_liste[i] == 3 * humble_numbers_liste[mult3]:
        mult3 += 1
    if humble_numbers_liste[i] == 5 * humble_numbers_liste[mult5]:
        mult5 += 1
    if humble_numbers_liste[i] == 7 * humble_numbers_liste[mult7]:
        mult7 += 1
def Ausgabe(): 
    """
    function 'Ausgabe' to write the output in the correct & wished format 
    """
    generator()
    """
    Aufruf für die funktoin 'generator' 
    """
    for line in sys.stdin:
        """
        for loop to print the outputs 
        """
        input_ = int(line)
        if input_ == 0:
            """ if input is 0 then terminate """
            break
        if input_ % 100 > 10 and input_ % 100 < 20:
            """ if the last 2 digits on th right are between 11 & 19 then write 'th' """
            print("The {}th humble number is {}.".format(input_, humble_numbers_liste[input_])) 
        elif input_ % 10 == 1:
            """ if the last digit on the right is 1 then write 'st' """
            print("The {}st humble number is {}.".format(input_, humble_numbers_liste[input_])) 
        elif input_ % 10 == 2:
            """ if the last digit on the right is 2 then write 'nd' """
            print("The {}nd humble number is {}.".format(input_, humble_numbers_liste[input_])) 
        elif input_ % 10 == 3:
            """ if the last digit on the right is 3 then write 'rd' """
            print("The {}rd humble number is {}.".format(input_, humble_numbers_liste[input_])) 
        else:
            """ otherwise write 'th' """
            print("The {}th humble number is {}.".format(input_, humble_numbers_liste[input_]))
Ausgabe()
"""
Aufruf für die funktion 'Ausgabe', welche zuerst die funktion 'generator' aufruft
"""