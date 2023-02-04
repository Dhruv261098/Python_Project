# Printing every line with number:

f = open('inputFile.txt','r')

count = 0
for line in f:
    print(str(count) + line)
    count = count + 1

print(f.read())
f.close()

