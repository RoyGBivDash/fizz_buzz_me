#!/usr/bin/env python

def fizz_buzz(number):
    """Return a string representing the number, or 'fizz'/'buzz'/'fizzbuzz'"""
    if (number % 3) == 0 and (number % 2)== 0:
        answer = 'fizzbuzz'
    elif (number % 3) == 0:
        answer = 'fizz'
    elif (number % 2) == 0:
        answer = 'buzz'
    else:
        answer = number

    return(answer)

def main():
    """Print sample output of fizz_buzz function"""
    NUMBER = 20
    print("Sample fizz_buzz output for 1 to {0}:".format(NUMBER))
    for i in range(1, NUMBER):
        print(fizz_buzz(i))


##########################

if __name__ == '__main__':
    main()
