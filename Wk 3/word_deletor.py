def replacement():
    a = str(input('Enter Original String:'))#input original sentence
    b = str(input('Substring to delete:'))#inut words to delete
    c = a.replace(b, "")#process of deleting the word
    print(c)# output new sentence
while True:
    replacement()#loop