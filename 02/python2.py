filename = "text.txt"
file = open(filename,"r")
twice = 0
thrwice = 0
c = 0
counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for line in file:
    while(c < 26):
        counter[(ord(line[c])-97)] += 1
        c += 1
    print(counter)
    c = 0
    while(c < 26):
        if(counter[c] == 2):
            twice += 1
            break
        c+=1
    c = 0
    while(c < 26):
        if(counter[c] == 3):
            thrwice += 1
            break
        c +=1
    c=0

    counter = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


print(twice)
print(thrwice)
print(twice * thrwice)
