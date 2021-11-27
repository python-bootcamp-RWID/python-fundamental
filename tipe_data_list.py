# struktur data List dianalogikan seperti stack / tumpukan , memiliki konsep LIFO

daftar_buku = ['Seven Habits', 'How to Influencer People', 'First Things First']

print("tampilkan daftar buku")
for index, buku in enumerate(daftar_buku):
    print(f"buku ke {index} - {buku}")

print("menampilkan data list dengan for range")
for i in range(0, len(daftar_buku)):
    print(f"buku {i + 1} {daftar_buku[i]}")

daftar_buku = [1, "danil syah", "-313", 3.14, True]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

daftar_buku = ['Seven Habits', 'How to Influencer People', 'First Things First']

# menambahkan elemen baru
daftar_buku.append("Belajar bahasa pemrograman pyhon")
print("\ntambahkan buku baru")

for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# menghapus element list
print("\n")
daftar_buku.clear()
print("data daftar buku di hapus")
print(daftar_buku)

# edit data element
print("\nGanti element")
daftar_buku = ['Seven Habits',
               'How to Influencer People',
               'First Things First',
               "pemrograman python", "algoritma dan ",
               "struktur data"]
daftar_buku[0] = "Eight Habits"
print(daftar_buku)

# mengambil satu element
buku = daftar_buku.pop(1)
print(daftar_buku)
print(f"buku yang diambil : {buku}")

# data diambil dari paling terakhir
daftar_buku.pop()
print(daftar_buku)

# pembacaan data dari akhir ke awal
daftar_buku.pop(-1)
print(daftar_buku)

# list comprehension
print("\nPerintah del list comprehension start")
daftar_buku = ['Seven Habits', 'How to Influencer People', 'First Things First', "pemrograman python", "algoritma dan "
                                                                                                       "struktur data"]

print(daftar_buku)
del daftar_buku[0:-2]  # START:END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("-" * 50)
daftar_buku = ['Seven Habits',
               'How to Influencer People',
               'First Things First',
               "pemrograman python",
               "algoritma dan struktur data",
               "Buku pemrograman",
               "Golang"
               ]
print(daftar_buku)
del daftar_buku[0::3]  # START:END:STEP
daftar_buku_new = daftar_buku
print(daftar_buku_new)

print("-" * 50)
print("membuat list baru")
daftar_pemrograman = ["PHP", "JavaScript", "Golang", "Ruby", "Python"]
daftar_pemrograman_new = daftar_pemrograman[:]  # mengcopy data list daftar_pemrograman
for i in range(0, len(daftar_pemrograman)):
    print(daftar_pemrograman[i])

print("\nMembuat list daftar pemrograman baru")
del daftar_pemrograman[:]
for i in range(0, len(daftar_pemrograman_new)):
    print(daftar_pemrograman_new[i])

print("-"*50)
print("membuat List baru dengan comprehension : ganjil")
daftar_pemrograman = ["PHP", "JavaScript", "Golang", "Ruby", "Python","C++"]
print(daftar_pemrograman)
daftar_pemrograman_baru = daftar_pemrograman[0::2]
for i in range(0, len(daftar_pemrograman_baru)):
    print(daftar_pemrograman_baru[i])

print("-"*50)
print("Membuat List baru dengan comprehension : genap")
daftar_pemrograman = ["PHP", "JavaScript", "Golang", "Ruby", "Python","C++","Lua","Scala"]
print(daftar_pemrograman)
daftar_pemrograman_baru = daftar_pemrograman[1::2]
for i in range(0, len(daftar_pemrograman_baru)):
    print(daftar_pemrograman_baru[i])

print("-"*50)
print("Membuat List baru dengan comprehension : menampilkan data dari ujung")
daftar_pemrograman = ["PHP", "JavaScript", "Golang", "Ruby", "Python","C++","Lua","Scala"]
print(daftar_pemrograman)
daftar_pemrograman_baru = daftar_pemrograman[0:-4:2]
for i in range(0, len(daftar_pemrograman_baru)):
    print(daftar_pemrograman_baru[i])


