def Module_Calculator():  # Looping the program
    SN = float(input('Please Enter Student Number:'))
    CT = float(input('Please Enter Common Test Marks:'))  # enter your Common Test marks
    CA = float(input('Please Enter Continuous Assessment Marks:'))  # enter your CA1 marks
    AS = float(input('Please Enter Assignment Marks:'))  # enter your Assessment marked
    Module_Marks = (CT / 60) * 30 + (CA / 75) * 40 + (AS / 80) * 30
    print('{:12s} {:6s} {:13s} {:12s} {:12s}'.format('StudentNo', 'Test', 'Assign', 'CA', 'Final'))
    print('{:<12.2f} {:<6.2f} {:<13.2f} {:<12.2f} {:<12.2f}'.format(SN,CT,AS,CA,Module_Marks))
while True:
    Module_Calculator()