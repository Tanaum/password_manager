import sys
import csv
import pandas as pd
from tabulate import tabulate
import cowsay

def main():
    while True:
        print(commands())
        print(optionss())


def optionss():
    command = input('> ').lower().strip()
    if command == 'a':
        return addd()
    elif command == 's':
        return show()
    elif command == 'd':
        return deletee()
    elif command == 'e':
        cowsay.daemon('Goodbye <3')
        sys.exit()

def commands():
    try:
        with open('commands.csv', 'r') as file:
            reader = csv.DictReader(file)
            return tabulate(reader,tablefmt="grid")
    except FileNotFoundError:
        sys.exit('File does not exist')

def addd():
    app = input("Enter app or website's name: ")
    password = input("Enter account's password: ")

    with open("passwords.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["app", "pw"])
        writer.writerow({"app": app, "pw": password})
    return 'App/website and password have been stored'


def show():
    try:
        with open('passwords.csv', 'r') as file:
            reader = csv.DictReader(file)
            return tabulate(reader,tablefmt="fancy_outline", showindex="always")
    except FileNotFoundError:
        sys.exit('File does not exist')

def deletee():
    try:
        print(show())
        index = int(input('Row number: '))
        df = pd.read_csv('passwords.csv')
        df = df.drop(df.index[index])
        df.to_csv('passwords.csv', index=False)
        return 'Row has been deleted'
    except ValueError:
        sys.exit('Enter a valid number')
    except IndexError:
        sys.exit('Enter a valid number')
    
if __name__ == '__main__':
    main()