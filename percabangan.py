# Sekuensial
print('Ibu berkata, "pergi ke toko"')
print('Budi menjawab,"Baik, apa yang harus saya lakukan di toko?" ')
print('Ibu menjawab, "Beli satu botol susu!"')
print('maka budi berangkat ke toko')
print("dan mulai berbelanja")

# percabangan
milk_bottle_count = 173
jumlah_telur = 10
print(f"Jumlah botol {milk_bottle_count} botol")
print(f"jumlah telur {jumlah_telur} butir")

if milk_bottle_count > 0 :
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("budi membeli 1 botol susu dan membeli 6 butir telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang kerumah")
print("menyerahkan hasil ke ibu")