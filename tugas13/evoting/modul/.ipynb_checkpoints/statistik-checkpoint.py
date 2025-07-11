from modul import pemilih, calon

def tampilkan_statistik():
    data_pemilih = pemilih.get_data()
    total = len(data_pemilih)
    sudah = sum(1 for p in data_pemilih if p['sudah_memilih'])
    persen = (sudah / total) * 100 if total > 0 else 0

    print(f"\n Statistik Pemilu:")
    print(f"Total Pemilih: {total}")
    print(f"Sudah Memilih: {sudah}")
    print(f"Persentase Partisipasi: {persen:.2f}%")

    semua_calon = calon.get_data()
    if semua_calon:
        pemenang = max(semua_calon, key=lambda x: x['jumlah_suara'])
        print(f"Calon Terpopuler Sementara: {pemenang['nama']} ({pemenang['jumlah_suara']} suara)")
