listPemilih = []

def tambah_pemilih():
    idPem = input("Masukan ID Pemilih: ")
    if any(p['id'] == idPem for p in listPemilih):
        print("ID sudah terdaftar.")
        return
    namaPem = input("Masukan Nama Pemilih: ")
    jurPem = input("Masukan Jurusan Pemilih: ")
    
    listPemilih.append({"id": idPem, "nama": namaPem, "jurusan": jurPem, "sudah_memilih": False})
    print("Pemilih berhasil didaftarkan!")

def get_data():
    return listPemilih

def cari_pemilih(id):
    for p in listPemilih:
        if p['id'] == id:
            return p
    return None