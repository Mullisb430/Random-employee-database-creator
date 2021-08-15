import random
from words import words


emailEndings = ['gmail.com', 'yahoo.com', 'aol.com', 'hotmail.com']

def generateEmail(name):
    key = random.randint(0, 16)
    if key >= 0 and key <4:
        return name.replace(' ', '') + str(random.randint(100, 999)) + '@' + random.choice(emailEndings)
    elif key >= 4 and key < 7:
        return name[0:name.index(" ")] + str(random.randint(10, 1000)) + random.choice(words) + '@' + random.choice(emailEndings)
    elif key >= 7 and key < 11:
        return random.choice(words) + random.choice(words) + str(random.randint(10, 1000)) + '@' + random.choice(emailEndings)
    elif key >= 11:
        return random.choice(words) + name[name.index(" ")+1:] + str(random.randint(1, 1000)) + '@' + random.choice(emailEndings)

    

def getDate():
    return f'{random.randint(1, 12)}/{random.randint(1, 30)}/{random.randint(2012, 2020)}'