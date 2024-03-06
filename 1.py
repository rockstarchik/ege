f = open("26-3.txt")
s = f.readline()
v, n = s.split()
v = int(v)
sp = []
for s in f:
    sp.append(int(s))
sp.sort()
summ = 0
i = 0
while summ + sp[i] <= v:
    summ = summ + sp[i]
    i += 1
k = v - (summ - sp[i-1])
print(i)
for i in range(i-1, len(sp)):
    if sp[i] <= k:
        maxi = sp[i]
print(maxi)
    
        

