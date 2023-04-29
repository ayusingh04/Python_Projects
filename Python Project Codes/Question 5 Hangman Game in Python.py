import random

print('\n\n-----*****----- Welcome to The Game of Hangman !! -----*****-----Welcome\n')
name = input('\nEnter your Good name: ')

hg = ['python', 'computer', 'programming', 'algorithm', 'coding']
print(f"\n\tHello {name} !! Let's start ... \nYou have to guess characters of random word given from this list",hg)
print("\n\t...You have 6 turns to guess the word...")

w = random.choice(hg)
b = '_' * len(w)
turns = 6
gd = []
hangman = [
    """
     ___
    |/      +
    |      
    |      
    |       
    |      
    |
    """,
    """
     ___
    |/      +
    |      (_)
    |      
    |       
    |      
    |
    """,
    """
     ___
    |/      +
    |      (_)
    |       |
    |       |
    |      
    |
    """,
    """
     ___
    |/      +
    |      (_)
    |      /|
    |       |
    |      
    |
    """,
    """
     ___
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      
    |
    """,
    """
     ___
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / 
    |
    """,
    """
     ___
    |/      +
    |      (_)
    |      /|\\
    |       |
    |      / \\
    |
    """
]
while turns > 0 and '_' in b:
    print(f'\n\tWord: {b}')
    print(f'\n\tTurns left: {turns}')
    print(f'\n\tGuessed letters: {", ".join(gd)}')
    print(hangman[6-turns])
    g = input('\n\tGuess a letter: ').lower()
    if not g.isalpha() or len(g) != 1:
        print('\n\tInvalid input! Please enter a single letter.')
        continue
    if g in gd:
        print(f'\n\tYou already guessed {g}!')
        continue
    gd.append(g)
    if g in w:
        print(f'\n\tCorrect! {g} is in the word.')
        b = ''.join([c if c == g or b[i] != '' else '' for i, c in enumerate(w)])
    else:
        print(f'\n\tWrong! {g} is not in the word.')
        turns -= 1
if '_' not in b:
    print(f'\n\tCongratulations {name}, you won! The word was {w}.')
else:
    print(f'\n\tSorry {name}, you lost! The word was {w}.')
    print(hangman[6])

