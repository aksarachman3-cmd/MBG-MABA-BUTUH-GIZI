"""Kontrak seluruh fungsi bersama MBG (Maba Butuh Gizi).

Isi setiap fungsi masih berupa placeholder. Anggota tinggal mengisi logika
di dalam fungsi yang menjadi tanggung jawab task-nya masing-masing.
"""

counter = 0
urutan = ["Pertama", "Kedua", "Ketiga"]
daftar_pertimbangan = ["Lokasi", "Harga", "Isi Piring"]


def reset_state() -> None:
    """Kembalikan counter ke 0, isi ulang urutan dan daftar_pertimbangan.

    Return: None.
    """


def validasi_pilihan(a: int, b: int) -> bool:
    """Cek apakah pilihan a berada di rentang 1 sampai b (inklusif).
    Return: True jika 1 <= a <= b, False selainnya (termasuk bukan int).
    """
    return type(a) is int and 1 <= a <= b


def home_page() -> int:
    """Tampilkan menu utama dan baca pilihan user.

    Return: pilihan (1 = rekomendasi, 2 = I'm Feeling Lucky, 3 = Exit).
    """

    print("===========================")
    print("MBG (MABA BUTUH GIZI)")
    print("===========================")
    print()
    print("Selamat Datang di MBG!")
    print()
    print("1. Berikan Rekomendasi Makanan")
    print("2. I'm Feeling Lucky (Makanan Random)")
    print("3. Exit")
    print()

    while True:
        try: #tes validasi input
            pilihan=int(input("Masukkan pilihan (1-3) = "))
            if validasi_pilihan(pilihan,3):
                return pilihan
        except ValueError: #alternatif untuk input di luar range yang tidak valid
            print("Pilihan harus berupa angka 1-3")
    


def berikan_rekomendasi_makanan() -> str:
    """Tampilkan sisa daftar_pertimbangan, baca pilihan, lalu hapus yang dipilih.

    Return: nilai dari daftar_pertimbangan[indeks] (mis. "Lokasi"), bukan literal
    hasil ketikan user. Teks "pertimbangan pertama/kedua/ketiga" diambil dari
    urutan[counter].
    """


def penentuan_lokasi() -> str | None:
    """Tampilkan menu lokasi unik dari database.py (1-5) dan pilihan Kembali (6).

    Return: nama lokasi yang dipilih, atau None jika user memilih Kembali.
    """


def check_lokasi(lokasi: str, data: list) -> list:
    """Filter data makanan sehingga hanya entri dengan lokasi yang cocok tersisa.

    Return: list entri baru dengan lokasi == lokasi; list kosong jika tidak ada.
    """
    hasil = []
    for i in range(len(data)):
        if(data[i][1]==lokasi):
            hasil.append(data[i])
    return hasil


def penentuan_harga() -> int | None:
    """Tampilkan menu rentang sharga (1-6) dan pilihan Kembali (7).

    Return: nomor rentang 1-6, atau None jika user memilih Kembali.
    """
    print("===========================")
    print("     Penentuan Harga")
    print("===========================\n")
    print("1. < 10.000")
    print("2. 10.000 - < 15.000")  
    print("3. 15.000 - < 20.000")  
    print("4. 20.000 - < 25.000")  
    print("5. 25.000 - < 30.000")  
    print("6. >= 30.000")
    print("7. Kembali\n")

    while True:  # Mengulang sampai pengguna memasukkan pilihan 1-7
        teks = input("Masukkan pilihan (1-7) = ").strip()  # Membaca input teks dan menghapus spasi di pinggirnya

        if teks.isdigit():  # Mengecek apakah semua karakter input berupa angka bulat positif
            pilihan = int(teks)  # Mengubah teks angka menjadi tipe data int
            if validasi_pilihan(pilihan, 7):  # Memeriksa apakah pilihan berada di rentang 1 sampai 7
                if pilihan == 7:  # Jika memilih Kembali
                    return None  # Mengembalikan None
                return pilihan  # Mengembalikan nomor rentang 1-6

        print("Input tidak valid! Masukkan angka 1-7.")  # Ditampilkan jika bukan angka atau di luar 1-7, lalu loop ulang


def check_harga(rentang: int, data: list) -> list:
    """Filter data berdasarkan nomor rentang harga.

    Pemetaan rentang: 1 = <10000, 2 = 10000-14999, 3 = 15000-19999,
    4 = 20000-24999, 5 = 25000-29999, 6 = >=30000.

    Return: list entri yang harganya masuk rentang; list kosong jika tidak ada.
    """
    hasil = [] #Sebagai list kosong untuk hasil saringan
    for item in data: #Looping untuk setiap item dalam data
        harga = item [3] #Buat ngambil nilai harga dalam item (harga dimasukin di urutan ke-4)
        #Mengecek rentang dan harga apaka memenuhi salah satu syarat
        if rentang == 1 and harga < 10000:
            hasil.append(item)
        elif rentang == 2 and 10000 <= harga < 15000:
            hasil.append(item)
        elif rentang == 3 and 15000 <= harga < 20000:
            hasil.append(item)
        elif rentang == 4 and 20000 <= harga < 25000:
            hasil.append(item)
        elif rentang == 5 and 25000 <= harga < 30000:
            hasil.append(item)
        elif rentang == 6 and harga >= 30000:
            hasil.append(item)
    return hasil #Mengembalikan item yang lolos, atau kosong jika tidak ada yang cocok

def penentuan_isi_piring() -> list[int] | None:
    """Tampilkan menu isi piring (1-4, bisa multiple) dan Kembali (5).

    Return: daftar nomor komponen yang dipilih (mis. [1, 4]), atau None jika
    user memilih Kembali.
    """


def check_isi_piring(komponen: list[int], data: list) -> list:
    """Filter data sehingga semua komponen yang diminta bernilai True.

    Pemetaan komponen: 1 = nasi, 2 = protein hewani, 3 = protein nabati,
    4 = sayur (index 0-3 pada field gizi tiap entri).

    Return: list entri yang memenuhi semua komponen; list kosong jika tidak ada.
    """


def menampilkan_makanan(daftar_makanan: list) -> None:
    """Cetak daftar makanan bernomor mulai dari 1 dengan format empat field:
    Nama makanan, Harga, Tenant, Lokasi.

    Return: None.
    """
    for i in range(len(daftar_makanan)):
        print(f"{i+1}. Nama makanan : {daftar_makanan[i][2]}")
        print(f"     Harga         : {daftar_makanan[i][3]}")
        print(f"     Tenant        : {daftar_makanan[i][0]}")
        print(f"     Lokasi        : {daftar_makanan[i][1]}")


def hasil_rekomendasi(daftar_makanan: list) -> bool:
    
    """Tampilkan hasil rekomendasi lalu tanyakan pemesanan untuk esok hari.

    Return: True jika user menjawab Y, False jika menjawab N.
    """ 

import random
from database import database #mengambil daftar data makanan dari file database.py


def im_feeling_lucky() -> bool:
    """Pilih satu makanan secara acak dari database, tampilkan, lalu tanyakan
    pemesanan untuk esok hari.

    Return: True jika user menjawab Y, False jika menjawab N.
    """
    makanan_acak = random.choice(database) #memilih satu makanan acak dari list database
    #membuat tampilan output im feeling lucky
    print("===========================")
    print("    I'm Feeling Lucky")
    print("===========================\n")
    print("Makanan siangmu kali ini adalah ........\n")
    menampilkan_makanan([makanan_acak]) #memanggil fungsi menampilkan makanan dengan makanan acak 
    while True:
        jawaban = input("\nApakah Anda ingin memesan untuk besok (Y/N) ? ").strip().upper()
        if jawaban == "Y":
            return True
        if jawaban == "N":
            return False
        print("Input tidak valid! Masukkan Y atau N.") #Memberi tahu bahwa inputan tidak sesuai, dan mengulang loop


def pemesanan() -> int | None:
    """Tampilkan lima slot waktu pengambilan (1-5) dan Kembali (6).

    Return: nomor slot 1-5, atau None jika user memilih Kembali.
    """
    print("===========================")
    print("Pemesanan Makanan")
    print("===========================")
    print()
    print("Pilih Waktu Pengambilan:")
    print("1. 9.00-10.00")
    print("2. 10.00-11.00")
    print("3. 11.00-12.00")
    print("4. 12.00-13.00")
    print("5. 13.00-14.00")
    print("6. Kembali")
    print()
    try:
        pilihan=int(input("Masukkan pilihanmu (1-6) = "))
        if validasi_pilihan(pilihan,5):
            return pilihan
        elif pilihan==6:
            pilihan=None
            return pilihan
    except ValueError:
        print("Pilihan harus berupa angka 1-6")
