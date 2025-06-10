listCalon = []

def tambah_calon():
    idCal = input("Masukan ID Calon: ")
    if any (c['id'] == idCal for c in listCalon):
        print("ID sudah terdaftar.")
        return
    namaCal = input("Masukan Nama Calon: ")
    vimiCal = input("Masukan Nama Visi Misi: ")

    listCalon.append({"id": idCal, "nama": namaCal, "visi": vimiCal, "jumlah_suara": 0})
    print("Calon berhasil didafarkan!")

def get_data():
    return listCalon

def cari_calon(id):
    for c in listCalon:
        if c['id'] == id:
            return c
    return None