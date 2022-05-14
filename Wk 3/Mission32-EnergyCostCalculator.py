#Programming I

#######################################
#            Mission 3.2              #
#   Calculate Daily Total Energy Cost #
#######################################

#Background
#==========
#The total energy cost is calculated using this formula: 
#Total Energy Cost ($) = Total Energy consumed (kW) x 0.2356

#Write a Python program that displays a table of energy in watts/hour
#for various appliances and prompt user to enter the daily hours for
#each appliance. The program then displays the table again with the
#daily hours and calculated value of the total daily energy cost.


#Important Notes
#===============
#1) Comment out ALL input prompts before submitting.
#2) You MUST (at least) use the following variables:
#   - appliance_list
#   - hr_list
#   - hrs_input
#   - total_energy_cost

#START CODING FROM HERE
#======================
#Create a list named appliance_list with the 3 appliances
#shown in the screenshot in Coursemology
appliance_list = ['Electric Fan','Air Con','Refrigerator']

#Prompt and obtain input for average daily consumption for appliances
#hrs_input = input('here:')

#Perform Calculation of Total Daily Energy Cost
def calculateEnergyCost(appliance_list,hrs_input):
    #Code to parse the input string in hrs_input (Hint: Use the split() function)
    hr_list = hrs_input.split(';')
    hr_list = list(map(float, hr_list))

    print(hr_list) #Modify to display list of appliances and daily hours used
    
    total_energy = hr_list[0]*0.07+hr_list[1]*1.2+hr_list[2]*0.2#Calculate total energy of all appliances
    
    total_energy_cost = total_energy*0.2356#Formula to calculate total energy cost
    
    print(total_energy) #Modify to display the daily energy consumed
    print(total_energy_cost) #Modify to display the calculated total energy cost

    return total_energy_cost #Do not remove this line

    
#Do not remove the next line
calculateEnergyCost(appliance_list,hrs_input)

#input [['Electric Fan',70],['Air Con', 1200],['Refrigerator', 200]],'5;4;24' output 2.34422
