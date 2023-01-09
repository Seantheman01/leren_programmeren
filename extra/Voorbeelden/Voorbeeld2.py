bedrag = int(input("Voer bedrag in: "))

aantal_twee_euro = bedrag // 200
print(f"Aantal 2 euro: {aantal_twee_euro}")
restant = bedrag - 200 * aantal_twee_euro 

aantal_één_euro = restant // 100
print(f"Aantal 1 euro: {aantal_één_euro}")
restant = restant - 100 * aantal_één_euro

aantal_vijftig_cent = restant // 50
print(f"Aantal 50 cent: {aantal_vijftig_cent}")
restant = restant - 50 * aantal_vijftig_cent

aantal_twintig_cent = restant // 20
print(f"Aantal 20 cent: {aantal_twintig_cent}")
restant = restant - 20 * aantal_twintig_cent

aantal_tien_cent = restant // 10
print(f"Aantal 10 cent: {aantal_tien_cent}")
restant = restant - 10 * aantal_tien_cent

aantal_vijf_cent = restant // 5
print(f"aantal 5 cent: {aantal_vijf_cent}")
restant = restant - 5 * aantal_vijf_cent

aantal_twee_cent = restant // 2
print(f"aantal 2 cent: {aantal_twee_cent}")
restant = restant - 2 * aantal_twee_cent

aantal_één_cent = restant // 1
print(f"aantal 1 cent: {aantal_één_cent}")
restant = restant - 1 * aantal_één_cent

print(restant)

# kan ook zo:
# print(f"Aantal 2 euro: {aantal_twee_euro}")
# print("Aantal 2 euro:" + str(aantal_twee_euro))
# print(f"Aantal 2 euro:", aantal_twee_euro)
# print("Aantal 2 euo: {}".format(aantal_twee_euro))