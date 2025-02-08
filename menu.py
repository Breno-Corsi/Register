from termcolor import colored
from os import system
from time import sleep
import datetime

def lin(t = 40):
    return '-'*t


def chooseoption(t = 40):
    while True:
        try:
            a = int(input('Choose an option: '))
            break
        except ValueError:
            return chooseoption()

    if a == 1:
        print(lin(t))
        print(colored('SHOWING USER LIST'.center(t), 'yellow'))
        print(lin(t))
        showuserlist(t = t)
        showmenu(t)
        chooseoption(t)

    elif a == 2:
        print(lin(t))
        print(colored('REGISTER NEW USER'.center(t), 'yellow'))
        print(lin(t))
        writeregister()
        showmenu(t)
        chooseoption(t)

    elif a == 3:
        createfile()
        showmenu(t)
        chooseoption(t)

    elif a == 4:
        print(lin(t))
        print(colored('EXITING APPLICATION'.center(t), 'yellow'))
        print(lin(t))
        sleep(2)
        system('cls')
        exit()

    elif a == 5:
        listlength()

    else:
        return chooseoption()


def showmenu(t = 40):
    print(lin(t))
    print('MAIN MENU'.center(t))
    print(lin(t))
    print(colored(1, 'green'), '-', colored('Show user list', 'blue'))
    print(colored(2, 'green'), '-', colored('Register new user', 'blue'))
    print(colored(3, 'green'), '-', colored('Create list', 'blue'))
    print(colored(4, 'green'), '-', colored('Exit', 'blue'))
    print(colored(5, 'green'), '-', colored('Choose list length', 'blue'))
    print(lin(t))
    chooseoption()


def createfile(path = 'register/data/users.txt'):
    import os

    try:
        open(path,'x')
        print(colored('File created successfully!', 'light_green'))
    except FileExistsError:
        print(colored('Error: File already exists.', 'red'))


def showuserlist(path = 'register/data/users.txt', t = 40):

    print(f"{colored('NAME', 'blue'):<30}{colored('BIRTH', 'blue'):<25}{colored('SEX', 'blue')}")
    print(lin())
    a = open(path, 'rt')
    for l in a:
        p = l.split(';')
        p[2] = p[2].replace('\n', '')
        print(f'{p[0]:<20}{p[1]:<15}{p[2]:>5}')


def writeregister(path = 'register/data/users.txt', name = 'unknown', age = 0):

    name = regname()
    birth = regage()
    sex = regsex()

    f = open(path, 'at')
    f.write(f'{name}; {birth}; {sex}\n')
    f.close()

    print('New user sucessfully registered')


def regname():

    name = str(input(colored('Name: ', 'yellow'))).lower().strip()
    r = any(char.isdigit() for char in name)
    if r:
        print(colored('Error: Name shoud not contain numbers.', 'red'))
        regname()
    else:
        return name


def regsex():
    sex = str(input(colored('Sex [M/F]: ', 'yellow'))).upper().strip()

    if sex not in 'MF':
        print(colored('Error: Sex can only be [M] or [F].', 'red'))
        regsex
    else:
        return sex


def regage():

    now = datetime.datetime.now()
    year = now.year
    try:
        birth = int(input(colored('Year of birth: ', 'yellow')))

        if birth > year:
            print(colored('Error: Year of birth cannot be more that current year.', 'red'))
            regage()

        elif birth < year - 120:
            print(colored('Error: Year of birth cannot be less than 150 years ago.', 'red'))
            regage()

        else:
            return birth

    except ValueError:
        return regage()


def listlength():

    try:
        t = int(input('Choose list length: '))
    
    except ValueError:
        print('List Length should be an int between 10 and 100')
        return listlength()

    showmenu(t)
    chooseoption(t)