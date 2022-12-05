mijn_dict = {
    123456789: "Jouke Corbijn",
    123456788: "Jan Janssen",
    123456787: "Ogulcan Dinc",
    123456786: "Renson Kooij"  
}
print(mijn_dict)

for val in mijn_dict.values():
    print(val) # hiermee print die de values
    
for ke in mijn_dict.keys():
    print(ke) # hiermee print die de keys
    
print(dir(mijn_dict))


mijn_lijst = [1]

print(dir(mijn_lijst))