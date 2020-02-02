import hashlib

# array of characters and digits we are adding to strings
character = ["*", "~", "!", "#"]
digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

COMMON_WORDS = open('words', 'r').read()
PASSWORD_LISTS = open('password_list.txt', 'r').read()

# loop in number of username/passwords
for hash_value in PASSWORD_LISTS.split('\n'):
    isFound = False
    username, hashedPass = hash_value.split(":")
    #print(username + ":" + hashedPass)

    # loop for number of words in words.txt file
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
            for symbol in character:
                new_temp_guess = symbol + str(temp_guess)
                guessHash = hashlib.sha256(bytes(new_temp_guess, 'utf-8')).hexdigest()
                # compare hash of substituted string and password hash, if true then isFound is true
                if guessHash == hashedPass:
                    print(new_temp_guess + " -> " + username + ":" + hashedPass + "\n")
                    symbol = None
                    guess = None
                    isFound = True

        else:
            guessHash = hashlib.sha256(bytes(temp_guess, 'utf-8')).hexdigest()
            if guessHash == hashedPass:
                print(temp_guess + " -> " + username + ":" + hashedPass + "\n")
                guess = None
                isFound = True
    if not isFound:
        print("password for user " + username + " can not found.\n")


