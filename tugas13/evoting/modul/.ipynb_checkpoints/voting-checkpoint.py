from modul import pemilih, calon
def lakukan_voting():
    idPem = input("Masukan ID Pemilih: ")
    dataPem = pemilih.cari_pemilih(idPem)
    if not dataPem:
        print("ID Pemilih TIdak Ditemukan!")
        return
        
    if dataPem['sudah_memilih']:
        print("ID Sudah Memilih!")
        return
    idCal = input("Masukan ID Calon: ")
    dataCal = calon.cari_calon(idCal)
    if not dataCal:
        print("ID Calon Tidak Ditemukan!")
    dataCal['jumlah_suara'] += 1
    dataPem['sudah_memilih'] = True
    print("Voting Berhasil Dilakukan!")

def tampilkan_hasil():
    print("Hasil Sementara:")
    for c in calon.get_data():
        print(f"{c['nama']} ({c['id']}) - {c['jumlah_suara']} suara")