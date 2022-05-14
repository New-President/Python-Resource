# Programming I

#######################
#     Mission 6.2     #
#       Digipet       #
#######################

# Background
# ==========
# With the Pokémon going all rage these days, Tom wants to create
# his own digital pet. In the digital pet, there are options to
# check the status of the pet, feed the pet, play with the pet, or
# let the pet rests. In the status section, player can see the pet’s
# level of hungriness, happiness, and energy. Each status can have
# a maximum level of 5 stars indicating full, or minimum 5 dots if
# the level is empty. If the player feeds the pet, the hungriness
# level will go up by 1 star, meanwhile causing the other 2 status
# to drop by 1 star. If the player plays with the pet, the happiness
# will go up by 1 star, while the other 2 will go down by 1 star.
# Likewise, if the player let the pet rests, the energy goes up by
# 1 star, and the other 2 indicators will drop by 1 star.
#
# Write a Python program that allows the player to interact with
# the digital pet as described above.


# Important Notes
# ===============
# 1) Comment out ALL input prompts before submitting.
# 2) You MUST use the following variables


# START CODING FROM HERE
# ======================

def start_pet():
    print('Digipet')
    b = '***..'
    c = '***..'
    d = '***..'
    while True:
        print('(1) Feed')
        print('(2) Play')
        print('(3) Rest')
        print('(4) Status')
        a = int(input('Please select an option:'))
        if a == 1:
            print('nom nom nom')
            b = b.replace('.', '*', 1)
            b = sorted(b)
            b = ''.join(b)
            c = c.replace('*', '.', 1)
            c = sorted(c)
            c = ''.join(c)
            d = d.replace('*', '.', 1)
            d = sorted(d)
            d = ''.join(d)
        elif a == 2:
            print('XD')
            b = b.replace('*', '.', 1)
            b = sorted(b)
            b = ''.join(b)
            c = c.replace('.', '*', 1)
            c = sorted(c)
            c = ''.join(c)
            d = d.replace('*', '.', 1)
            d = sorted(d)
            d = ''.join(d)
        elif a == 3:
            print('Zzzzz')
            b = b.replace('*', '.', 1)
            b = sorted(b)
            b = ''.join(b)
            c = c.replace('*', '.', 1)
            c = sorted(c)
            c = ''.join(c)
            d = d.replace('.', '*', 1)
            d = sorted(d)
            d = ''.join(d)
        elif a == 4:
            print('hungry  {:>5}'.format(b))
            print('happiness  {:>5}'.format(c))
            print('energy  {:>5}'.format(d))
        else:
            print('Warning: PLS ONLY SELECT NUMBERS 1-4')


# Do not remove the next line
start_pet()
