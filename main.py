f = open(".//input.txt", "r")
lines = f.readlines()

data = []
for line in lines:
    data.append(line.strip('\n'))

print(data)
