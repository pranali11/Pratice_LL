a1  = [1,2,3]
a2 = [9,4,5]

dict1 = {}
for i in range(len(a1)):
    if dict1[a1[i]]:
        dict1[a1[i]] = true

print(dict1)
def commonthere(a1, a2):
    for val in a2:
        if val in a1:
            return("True")

    return("False")


print(commonthere(a1,a2))

