filename = "text.txt"
file = open(filename,"r")
sum = 0
for line in file:
    if line[0] == '+':
        sum += int(line[1:])
    if line[0] == '-':
        sum -= int(line[1:])
print (sum)
#test
