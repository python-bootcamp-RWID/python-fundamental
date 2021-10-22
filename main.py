"""
Semua sintaksis dasar bahasa pemrograman terdiri dari :
1. sekuensial : langkah berurutan
2. percabangan : langkah melompat jika kondisi terpenuhi
3. perulangan : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
"""

# Sekuensial
print('start')
print('Ibu berkata, "pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya beli di toko ?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6')
print('Maka budi berangkat ke toko')
print('Dan mulai berbelanja')
print('budi menanyakan ketersediaan susu, jika susu tidak tersedia, maka budi pulang')
susu = 'ada'
telor = 'kosong'
if susu == 'ada':
    if telor == 'ada':
        print('beli 1 botol susu dan 6 telor')
    else:
        print('beli 1 botol susu')
else:
    print('pulang ke rumah')


print('budi menanyakan apakah ada telur ?')
print('jika kondisi telur tidak tersedia maka budi hanya membeli satu botol susu')
print('jika kondisi terlur teredia, maka budi membeli enam butir telur')
print('budi kembali pulang kerumah')
print('end')