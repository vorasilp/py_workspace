import math

result = 1
count = 0

with open("out.txt","w") as f:
    for n in range(2,4200):
        
        if (n%5 == 0):
            count += 1
        if (n%25 == 0):
            count += 1
        if (n%125 == 0):
            count += 1
        if (n%625 == 0):
            count += 1
        if (n%3125 == 0):
            count += 1

        if count == 1000:
            f.write(f"{n} {count} \n")