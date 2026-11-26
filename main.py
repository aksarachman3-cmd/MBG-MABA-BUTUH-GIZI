"""Alur kerja utama program MBG (Maba Butuh Gizi).

Seluruh halaman dan fungsi pembantu berada di shortcuts.py. File ini hanya
mengatur state tiap sesi, routing antar halaman, dan urutan pemanggilan fungsi.
"""

from database import database
import shortcuts as sc


def jalankan_program() -> None:
    """Jalankan sesi program dari home page sampai user memilih Exit."""
    while True:
        sc.reset_state()
        hasil = list(database)

        pilihan = sc.home_page()
        if pilihan == 1:
            for _ in range(len(sc.urutan)):
                if not sc.daftar_pertimbangan:
                    break

                pertimbangan = sc.berikan_rekomendasi_makanan()
                if pertimbangan == "Lokasi":
                    lokasi = sc.penentuan_lokasi()
                    if lokasi is None:
                        break
                    hasil = sc.check_lokasi(lokasi, hasil)
                elif pertimbangan == "Harga":
                    rentang = sc.penentuan_harga()
                    if rentang is None:
                        break
                    hasil = sc.check_harga(rentang, hasil)
                elif pertimbangan == "Isi Piring":
                    komponen = sc.penentuan_isi_piring()
                    if komponen is None:
                        break
                    hasil = sc.check_isi_piring(komponen, hasil)
                else:
                    break
            else:
                if sc.hasil_rekomendasi(hasil):
                    sc.pemesanan()
        elif pilihan == 2:
            if sc.im_feeling_lucky():
                sc.pemesanan()
        elif pilihan == 3:
            break
        else:
            break


if __name__ == "__main__":
    jalankan_program()
