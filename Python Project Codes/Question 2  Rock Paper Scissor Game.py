import random 

print('\n------*****-----Welcome to Game The of Rock Paper and Scissor-----*****-----\n\n')

x = 'Y'

while x == 'Y' or x == 'y':
    c1 = random.choice(['Rock','Paper','Scissor'])
    c2 = input('\n Enter your choice: ')
    if (c1 == 'Rock' and c2 == 'Scissor') or (c1 == 'Paper' and c2 == "Rock") or (c1 == 'Scissor' and c2 == 'Paper'):
        print('\n              Computer Wins... !!')
    elif c1 == c2:
        print("\n              It is a Tie Game...")
    else:
        print('\n              You Wins...')
    x = input("\n Do you want to continue This Game (Y/N): ")
