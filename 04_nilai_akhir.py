nama = input("Masukkan nama: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (0.20 * nilai_tugas) + (0.30 * nilai_uts) + (0.50 * nilai_uas)

print(f"\nNama: {nama}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")