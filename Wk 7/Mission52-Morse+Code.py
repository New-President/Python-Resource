# Programming I

#######################
#     Mission 6.1     #
#     Morse Code      #
#######################

# Background
# ==========
# Tom has a partner to help him with the cases. To
# communicate to each other, they uses Morse code.
# Write a Python program that prompts the user to
# key in a number, convert each digit according to
# the diagram below. Each Morse code of a digit has
# to be separated with 3 spaces. The following shows
# a sample output of the program.
#
# Enter a number to convert:9
# The morse code for 9 is ----.
# >>>
# Enter a number to convert:101
# The morse code for 101 is .----   -----   .----
# >>>


# Important Notes
# ===============
# 1) Comment out ALL input prompts before submitting.
# 2) You MUST use the following variables
#   - num
#   - morse_code


# START CODING FROM HERE
# ======================

# Prompt user to enter the number to convert
num = '13'


# convert to morse code
def convert_code(num):
    num = num.replace("'", "")
    a = {'0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
         '8': '---..', '9': '----.'}
    for i in num:
        morse_code=print(a[i], end='   ')
    return morse_code  # Do not remove this line


# Do not remove the next line
convert_code(num)

# test cases
# input 9        output ----.
# input 101      output .----   -----   .----
# input 0906     output -----   ----.   -----   -....
