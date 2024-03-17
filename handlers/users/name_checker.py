
letters = 'abcdefghijklmnopqrstuvwxyz'

def name_checker(name):
    if len(name) == 2:
        for i in name[0]:
            if i.lower() not in letters:
                return False
        for i in name[1]:
            if i.lower() not in letters:
                return False
        if name[0].istitle() and name[1].istitle():
            return True
        else:
            return False
    else:
        return False
