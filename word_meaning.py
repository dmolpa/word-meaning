'''prompts for word and search for meaning in JSON dictionary'''
from json import load # we import only one function that we need
from difflib import get_close_matches

DATA = load(open("data.json")) #imported function 'load' put DATA from json into a list we called 'DATA'

def ifalltrue(key_word): #needed to call it again if the user will want to retype his word when 'get_close_matches' guess wrong. restart not needed
    '''
    expect a string as input.
    1. looks for abbreviations
    2. looks for proper nouns
    3. looks for lowercase word meanings
    4. else: call 'translate' function
    '''
    if key_word.upper() in DATA:
        return DATA[key_word.upper()]
    elif key_word.title() in DATA:
        return DATA[key_word.title()]
    elif key_word.lower() in DATA:
        return DATA[key_word.lower()]
    return translate(key_word) # starts 'translateparens' that will try to solve the input

def translate(key_word):
    '''
    expect a string, treats it as key to find value/meaning in dictionary.
    if input is not an acceptable string - tries to guess and ask user 'y' or 'n'.
    'y' or 'n' can be lower or upper case. Else: returns "unacceptable input".
    if there is no close match - returns "The word doesn't exist."
    '''
    if len(get_close_matches(key_word, DATA.keys())) > 0:
        y_n = input("Did you mean %s? Enter Y if yes, or N if no: " % get_close_matches(key_word, DATA.keys())[0])
        y_n = y_n.upper() # 'y' or 'Y' will be ok
        if y_n == "Y":
            return DATA[get_close_matches(key_word, DATA.keys())[0]]
        elif y_n == "N":
            newi = input('So what did you mean? Retype your word, please: ') #if get_close_matches guessed wrong user try again
            return ifalltrue(newi) #and we start it all over again with a new input
        else:
            return "Unacceptable input."
    else:
        return "The word doesn't exist."

if __name__ == "__main__":         # if file opened directly - run the code

    WORD = input("Enter a word: ") # start
    output = ifalltrue(WORD)       # calling 'ifalltrue'
    print("*"*14)                  # mark between separate block
    if type(output) == list:       # if there's more than one definition
        for item in output:        # printing by line
            print(item)
            print("*"*14)
    else:
        print(output)              # for single meaning
