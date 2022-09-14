import math

pupil = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t"]
GROUP1 = []
GROUP2 = []

for i in range(math.ceil(len(pupil)/2)):
    GROUP1.append(pupil[2*i])
    if 2*i+1 < len(pupil):
        GROUP2.append(pupil[2*i+1])

print(GROUP1)
print(GROUP2)