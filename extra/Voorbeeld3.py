zin = "hallo wereld"
x = 0

for karakter in zin:
    print(karakter)

# dit kan beginnen met elk getal
for c in  (0, 1, 2): # 3 rondjes
    for d in (0, 1, 2): # 3 rondjes
        for e in (0, 1, 2):
            x = x + 1
            print(zin, "c= ", c, "d=", d, "e= ", e, "x= ", x)