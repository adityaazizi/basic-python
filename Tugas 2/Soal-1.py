# Membuat list untuk menyimpan data
listNama = []
listNoTlp = []

# Fungsi Daftar Kontak
def daftarKontak():
   print ("Daftar Kontak: ")
   for x in range(len(listNama)):
      print ("Nama: {}".format(listNama[x]))
      print ("No Telepon: {}".format(listNoTlp[x]))

# Fungsi Tambah Kontak
def tambahKontak():
   listNama.append(str(input("Nama: ")))
   listNoTlp.append(str(input("No Telepon: ")))
   print ("Kontak berhasil ditambahkan")

# Fungsi untuk Keluar
def keluar():
   print ("Program selesai, sampai jumpa!")

# print Selamat Datang
print ("Selamat datang!")   

# Agar program berjalan terus gunakan While Loop
while True:
   # Tampilan Awal
   print(
   '''   
   --Menu--
   1. Daftar Kontak
   2. Tambah Kontak
   3. Keluar
   '''
   )

   # Inputan User untuk menu yang disediakan
   masukan = int(input("Pilih menu: "))

   # Jika User memilih 1. Daftar Kontak
   if masukan == 1:
      daftarKontak()
   
   # Jika User memilih 2. Tambah Kontak
   elif masukan == 2:
      tambahKontak()
   
   # Jika User memilih 3. Keluar
   elif masukan == 3:
      keluar()
      break

   # Jika User memasukan pilihan yang tidak tersedia
   else:
      print ("Menu tidak tersedia")

   