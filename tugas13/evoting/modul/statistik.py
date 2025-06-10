from modul import pemilih, calon

def tampilkan_statistik():
    dataPem = pemilih.get_data()
    total = len(dataPem)
    sudah = sum(1 for p in dataPem if p['sudah_memilih'])
    persen = (sudah / total) * 100 if total > 0 else 0

    print(f"\n Statistik Pemilu:")
    print(f"Total Pemilih: {total}")
    print(f"Sudah Memilih: {sudah}")
    print(f"Persentase Partisipasi: {persen:.2f}%")

    semua_calon = calon.get_data()
    if semua_calon:
        pemenang = max(semua_calon, key=lambda x: x['jumlah_suara'])
        print(f"Hasil Voting Sementara: {pemenang['nama']} ({pemenang['jumlah_suara']} suara)")
