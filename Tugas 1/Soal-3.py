# Masukan Nilai Teori
Nilai_Teori = float(input("Masukan Nilai Teori: "))

# Masukan Nilai Praktek
Nilai_Praktek = float(input("Masukan Nilai Praktek: "))

# Membuat Percabangan
# Jika nilai ujian teori dan praktek minimal 70
if Nilai_Teori >= 70 and Nilai_Praktek >= 70:
   print("Selamat, anda lulus!")

# Jika nilai ujian teori minimal 70 dan nilai ujian praktek kurang dari 70
elif Nilai_Teori >= 70 and Nilai_Praktek < 70:
   print("Anda harus mengulang ujian praktek.")

# Jika nilai ujian teori kurang dari 70 dan nilai ujian praktek minimal 70
elif Nilai_Teori < 70 and Nilai_Praktek >= 70:
   print("Anda harus mengulang ujian teori.")

# Jika nilai ujian teori dan ujian praktek kurang dari 70
else:
   print("Anda harus mengulang ujian teori dan praktek")