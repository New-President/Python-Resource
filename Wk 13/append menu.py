path = "C:\\Users\\ziren\\OneDrive - Ngee Ann Polytechnic\\Desktop\\School\\PR1\\Wk 13\\PRG1_data\\"
datafile = open(path + "prices.txt", "w")
prices = [["kopi", 0.4],
          ["teh", 0.4],
          ["milo", 0.5],
          ["soft drinks", 1.20]]

for i in prices:
    datafile.write('{}: ${:.2f}\n'.format(i[0], i[1]))
datafile.close()
