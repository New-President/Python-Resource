#Programming I

########################
#     Mission 5.2      #
#  Loop even integers  #
########################

#Background
#==========
#Write a program that uses while loop to total up the even integers from 1 to 20.


#Important Notes
#===============
#You MUST use the following variables
#   - total
#   - number



#START CODING FROM HERE
#======================

#Set number value
number = 20


#Check closest object
def total_num(number):
    a=2
    total=0
    while a <number+1:
        total=total+a
        a=a+2
    
    print('The total is {}'.format(total)) #Modify to display the total
    
    return total #Do not remove this line

    
#Do not remove the next line
total_num(number)


#output 110
