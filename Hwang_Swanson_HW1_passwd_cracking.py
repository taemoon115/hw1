import hashlib
import itertools

# array of characters and digits we are adding to strings
character = ["*", "~", "!", "#"]
digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers = '0123456789'
y = ''

COMMON_WORDS = open('words', 'r').read()
PASSWORD_LISTS = open('password_list.txt', 'r').read()

# loop in number of username/passwords
for hash_value in PASSWORD_LISTS.split('\n'):
    isFound = False
    username, hashedPass = hash_value.split(":")

    # find if password is 4 digit number with character first
    for c in itertools.product(numbers, repeat=4):
        pin = y + ''.join(c)
        for a in character:
            temp_pin = a + pin
            guessHash = hashlib.sha256(bytes(temp_pin, 'utf-8')).hexdigest()
            if guessHash == hashedPass:
                print(temp_pin + " -> " + username + ":" + hashedPass + "\n")
                isFound = True
                c = None
                break


    # loop for number of words in words.txt file
    if not isFound:
        for guess in COMMON_WORDS.split('\n'):
            temp_guess = guess
            # substitute if string length is 7
            if len(temp_guess) == 7:
                temp_guess = temp_guess.capitalize()
                for end_digit in digit:
                    new_temp_guess = temp_guess + end_digit
                    guessHash = hashlib.sha256(bytes(new_temp_guess, 'utf-8')).hexdigest()
                    # compare hash of substituted string and password hash, if true then isFound is true
                    if guessHash == hashedPass:
                        print(new_temp_guess + " -> " + username + ":" + hashedPass + "\n")
                        end_digit = None
                        guess = None
                        isFound = True
            # substitute if string length is 5
            elif len(temp_guess) == 5:
                temp_guess = temp_guess.replace('a', '@').replace('l', '1')
                guessHash = hashlib.sha256(bytes(temp_guess, 'utf-8')).hexdigest()
                # compare hash of substituted string and password hash, if true then isFound is true
                if guessHash == hashedPass:
                    print(temp_guess + " -> " + username + ":" + hashedPass + "\n")
                    guess = None
                    isFound = True
            else:
                guessHash = hashlib.sha256(bytes(temp_guess, 'utf-8')).hexdigest()
                if guessHash == hashedPass:
                    print(temp_guess + " -> " + username + ":" + hashedPass + "\n")
                    guess = None
                    isFound = True
    # if password not found then try to find if it is 7 digit number
    # since this case takes longest time
    if not isFound:
        for c in itertools.product(numbers, repeat=7):
            pin = y + ''.join(c)
            guessHash = hashlib.sha256(bytes(pin, 'utf-8')).hexdigest()
            if guessHash == hashedPass:
                print(pin + " -> " + username + ":" + hashedPass + "\n")
                isFound = True
                break
    # if nothing found then just print out password couldn't be found
    if not isFound:
        print("password for user " + username + " can not found.\n")






