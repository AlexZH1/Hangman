import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()


      
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Errate einen Buchstaben:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Diesen Buchstaben hast du schon erraten!", guess)
            elif guess not in word:
                print(guess, "Ist nicht vorhanden.")
                tries-= 1
                guessed_letters.append(guess)
            else:
                print("Gut gemacht!", guess, "ist im Wort!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion= "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Du hast das Wort bereits erraten", guess)
            elif guess != word:
                print(guess, "ist nicht im Wort.")
                tries -= 1
                guessed_words.append(guess)
            else: 
                guessed = True
                word_completion = word
        else:
            print("Nicht gültig!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Gratulation. Du hast gewonnen.")
    else:
        print("Du hast keine Versuche mehr. Das Wort war " + word)
        
        
def display_hangman(tries):
    stages = [  # Kopf, Körper, beide Hände, beide Beine
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # Kopf, Körper, beide Arme, ein Bein
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # Kopf, Körper, beide Arme
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # Kopf, Körper, ein Arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # Kopf, Körper
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                #Kopf
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                #Anfang
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word= get_word()
    play(word)
    while upper (input("Nochmals spielen? (J/N)")) == "J":
        word = get_word()
        play(word)
 
name = raw_input("Wie lautet dein Name?")
print"Hallo, " + name,". Zeit um Hangman zu spielen"
print""
                  
if __name__ == "__main__":
    main()
    
    

#Falls du nicht weisst, von wem das ist, merk dir diesen Namen: Alex Fäh :-)