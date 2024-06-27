import random

name= input('what is your name')

print(f'Good luck {name}')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


word = random.choice(words)

print('Guess the words')

guesses = ''

changes= len(word) + 2

while changes>0:
    
    counts = 0

    for char in word:
        if char in guesses:
           
           print(char, end='')
        else:
           
           print('_',end=" ")
           counts += 1
    if counts == 0:
        print('you win')

        print(f'the word is{word}')
        break
    print()
    guess = input('guess the character')
    guesses += guess

    if guess not in word:
        changes -= 1

        print('worng')

        if changes == 0:
            print('you lose')

 




