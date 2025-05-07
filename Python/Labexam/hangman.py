import random

def hangman(word):
    maxAttempts = 7
    attempts = 0
    wordToGuess = '_' * len(word)
    guessedLetters = []

    while attempts < maxAttempts and '_' in wordToGuess:
        print('\nWord to guess: ' + ' '.join(wordToGuess))
        guess = input('Guess a character: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessedLetters:
            print("You already guessed that letter.")
            continue

        guessedLetters.append(guess)

        if guess in word:
            print('Correct Guess!')
            for i in range(len(word)):
                if word[i] == guess:
                    wordToGuess = wordToGuess[:i] + guess + wordToGuess[i+1:]
        else:
            print('Incorrect Guess!')
            attempts += 1
            if maxAttempts - attempts > 0:
                print('Number of wrong attempts left: ' + str(maxAttempts - attempts))

    if '_' not in wordToGuess:
        print('\nCongrats! You guessed the word correctly! The word is: ' + word)
    else:
        print('\nSorry :( You didn’t guess the word correctly! The word was: ' + word)
    print('NOTE: A maximum of 7 wrong attempts are allowed.')

# Word list
words = ['annoy', 'python', 'apple', 'planet']
word = random.choice(words)

# Start game
hangman(word)
