def pilih_barang_prioritas(daftar_barang, kapasitas_maksimal):
    barang_terurut = sorted(daftar_barang, key=lambda x: x[1], reverse=True)
    
    barang_terpilih = []
    total_beban = 0
    total_prioritas = 0
    
    for barang in barang_terurut:
        nama, prioritas, berat = barang
        if total_beban + berat <= kapasitas_maksimal:
            barang_terpilih.append(barang)
            total_beban += berat
            total_prioritas += prioritas
            
    return barang_terpilih, total_beban, total_prioritas

items = [
    ("Laptop Kantor", 95, 3),
    ("Dokumen Penting", 90, 1),
    ("Buku Referensi", 60, 2),
    ("Peralatan Mandi", 40, 1),
    ("Jaket Tebal", 50, 2)
]

KAPASITAS = 5
terpilih, beban, skor = pilih_barang_prioritas(items, KAPASITAS)

print("Barang yang dipilih:")
for item in terpilih:
    print(f"- {item[0]} (Prioritas: {item[1]}, Ukuran: {item[2]})")
print(f"Total Beban: {beban}, Total Skor Prioritas: {skor}")