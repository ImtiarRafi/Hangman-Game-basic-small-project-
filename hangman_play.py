import random
from hangmanword import words

def get_word():
    word = random.choice(words)
    # Ensure the chosen word has no dash or space
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():

    picked_word = get_word()
    word_count = list(picked_word)
    guessed_letter = []
    guess_count = 0

    chance = 6

    while guess_count < len(word_count) and chance > 0:

        print('Already guessed letters: ', ' '.join(guessed_letter))

        myword = [m if m in guessed_letter else '-' for m in picked_word]
        print('Now Word is : ',' '.join(myword))

        guess = input('Enter your guess : ').upper()
        guess_count += 1

        if guess in word_count:
            print('Great Guess. Try another one')
            if guess not in guessed_letter:
                guessed_letter.append(guess)

        elif guess in guessed_letter:
            print('You already guessed it')
            chance -= 1

        else:
            print('Your guess is wrong')
            guessed_letter.append(guess)
            chance -= 1

    if '-' not in myword:
        print("Congratulations! You've guessed the word:", picked_word)
    else:
        print("Sorry, you're out of chances. The word was:", picked_word)

hangman()
