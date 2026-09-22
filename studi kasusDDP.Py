def hitung_biaya_parkir(jenis_kendaraan, jam_masuk, jam_keluar):
    durasi = jam_keluar - jam_masuk

    if durasi < 0:
        durasi += 24

    jenis = jenis_kendaraan.lower()
    if jenis == "mobil":
        tarif_per_jam = 5000
    elif jenis == "motor":
        tarif_per_jam = 3000
    else:
        tarif_per_jam = 0

    total_biaya = durasi * tarif_per_jam

    return durasi, total_biaya

jenis_kendaraan = "Mobil"
jam_masuk = 8  
jam_keluar = 12

lama_parkir, total_biaya = hitung_biaya_parkir(jenis_kendaraan, jam_masuk, jam_keluar)

print("========================================")
print("          STRUK BIAYA PARKIR            ")
print("========================================")
print(f"Jenis Kendaraan : {jenis_kendaraan}")
print(f"Jam Masuk       : {jam_masuk}:00 WIB")
print(f"Jam Keluar      : {jam_keluar}:00 WIB")
print(f"Lama Parkir     : {lama_parkir} jam")
print(f"Total Biaya     : Rp {total_biaya:,}")
print("========================================")