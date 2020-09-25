import matplotlib.pyplot as plt
import os

array = []
text_file = open('ping.txt', r)
print("Opening file: ", text_file)
lines = text_file.readlines()
for i in range(1, len(lines)):
    first = lines[i].strip().split(' ')
    array.extend(first)

print(len(lines))

matching = [s for s in array if "time=" in s]
print(len(matching))

new_matching = []

for s in matching:
    string_time = s.replace("time=", "")
    #string_time = news.replace("мс", "")
    new_matching.append(string_time)

s = 0 

for i in range(0, len(new_matching)):
    new_matching[i] = float(new_matching[i])
    s+=1

print(new_matching, s)
plt.plot(new_matching)
plt.show()
