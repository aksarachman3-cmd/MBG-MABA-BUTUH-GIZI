# AR_check-lokasi_2: Fungsi Check Lokasi

## Tujuan

Menyediakan fungsi filter lokasi dan halaman Penentuan Lokasi yang memakai data lokasi dari `database.py`.

## Context

- Sumber lokasi adalah `database.py`: Masjid Alwassat, GKU 2, TB3, TB2, KOICA. Jangan memakai GKU 1 atau ASRAMA.
- Menu Penentuan Lokasi memakai urutan tersebut sebagai pilihan 1-5, dengan pilihan 6 = Kembali.
- Halaman Penentuan Lokasi memanggil `check_lokasi` setelah user memilih lokasi.
- `check_lokasi` menerima data yang sudah difilter sebelumnya sehingga filter bisa dirangkai.

## Steps

- Isi fungsi `check_lokasi(lokasi: str, data: list) -> list` di `shortcuts.py`: kembalikan entri yang field lokasinya sama dengan `lokasi`.
- Isi fungsi `penentuan_lokasi() -> str | None` di `shortcuts.py`: tampilkan menu, validasi pilihan 1-6, kembalikan nama lokasi atau `None` untuk Kembali.
- Gunakan `sc.validasi_pilihan(a, b)` untuk memblok input yang tidak valid.

## Testing

- Filter hanya mengembalikan entri dengan lokasi yang cocok.
- Filter mengembalikan list kosong jika tidak ada entri yang cocok.
- Memilih 6 mengembalikan `None`; memilih 0 atau 7 ditolak.
