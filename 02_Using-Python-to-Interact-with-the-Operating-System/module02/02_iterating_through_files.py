
with open("spider.txt") as file:
    for line in file:
        print(line.upper())
        

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())