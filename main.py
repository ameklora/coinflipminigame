import random
chosen_side = str(input('Heads or tails? (H, T): ')) #choosing the side of coin
rand_side = random.randint(1, 2) #flipping the coin (1 = heads, 2 = tails)
if rand_side == 1: #win check
    print('Side is Heads')
    if chosen_side.lower() == 'h' or chosen_side.lower() == 'heads':
        print('Congrats, You won!')
    elif chosen_side.lower() == 't' or chosen_side.lower() == 'tails':
        print('You lose.')
    else:
        print('You typed wrong side')
if rand_side == 2:
    print('Side is Tails')
    if chosen_side.lower() == 'h' or chosen_side.lower() == 'heads':
        print('You lose.')
    elif chosen_side.lower() == 't' or chosen_side.lower() == 'tails':
        print('Congrats, You won!')
    else:
        print('You typed wrong side')
