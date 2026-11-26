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


def home_page() -> int:
    """Tampilkan menu utama dan baca pilihan user.

    Return: pilihan (1 = rekomendasi, 2 = I'm Feeling Lucky, 3 = Exit).
    """

    print("===========================")
    print("MBG (MABA BUTUH GIZI)")
    print("===========================")
    print()
    print("Selamat Datang di MBG! (Bukan Makan Bergizi Gratis)")
    print()
    print("Pilihlah opsi berikut untuk melanjutkan:")
    print("1. Berikan Rekomendasi Makanan")
    print("2. I'm Feeling Lucky (Random)")
    print("3. Exit")
    print()

    while True:
        try:
            pilihan=int(input("Masukkan pilihan (1-3): "))
            if 1<=pilihan<=3:
                return pilihan
            print("Masukkan angka dengan batasan 1-3")
        except ValueError:
            print("Masukan harus berupa angka")
    


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


def penentuan_harga() -> int | None:
    """Tampilkan menu rentang harga (1-6) dan pilihan Kembali (7).

    Return: nomor rentang 1-6, atau None jika user memilih Kembali.
    """


def check_harga(rentang: int, data: list) -> list:
    """Filter data berdasarkan nomor rentang harga.

    Pemetaan rentang: 1 = <10000, 2 = 10000-14999, 3 = 15000-19999,
    4 = 20000-24999, 5 = 25000-29999, 6 = >=30000.

    Return: list entri yang harganya masuk rentang; list kosong jika tidak ada.
    """


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


def hasil_rekomendasi(daftar_makanan: list) -> bool:
    
    """Tampilkan hasil rekomendasi lalu tanyakan pemesanan untuk esok hari.

    Return: True jika user menjawab Y, False jika menjawab N.
    """


def im_feeling_lucky() -> bool:
    """Pilih satu makanan secara acak dari database, tampilkan, lalu tanyakan
    pemesanan untuk esok hari.

    Return: True jika user menjawab Y, False jika menjawab N.
    """


def pemesanan() -> int | None:
    """Tampilkan lima slot waktu pengambilan (1-5) dan Kembali (6).

    Return: nomor slot 1-5, atau None jika user memilih Kembali.
    """
