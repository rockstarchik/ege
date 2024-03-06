mini = 10000
maxi = 0
kol = 0
file = open("9-162 (1).txt")
for s in file:
    sp = [int(x) for x in s.split()]
    spp = []
    spm = []
    mini = min(sp)
    maxi = max(sp)
    for i in range(len(sp)):
        if sp.count(sp[i]) != 1:
            spp.append(sp[i])
        if sp[i] != maxi and sp[i] != mini:
            spm.append(sp[i])
        if len(spm) == 2 and len(spp) != 0:
            if 2*(mini**2) > spm[0] * spm[1] :
                kol = kol + 1
print(kol)
