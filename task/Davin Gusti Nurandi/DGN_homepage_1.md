# DGN_homepage_1: Membuat Home Page

## Tujuan

Membuat home page yang responsif, menerima input dengan baik, dan mengarahkan ke halaman lanjutan sesuai pilihan user.

## Context

- Di halaman ini user bersifat fresh. `main.py` memanggil `sc.reset_state()` sebelum memanggil `home_page()`.
- User hanya boleh menginput angka 1-3.
- Pilihan 1 menuju Berikan Rekomendasi Makanan, 2 menuju I'm Feeling Lucky, 3 keluar.

## Steps

- Isi fungsi `home_page() -> int` di `shortcuts.py`: tidak menerima parameter dan mengembalikan variabel `pilihan`.
- Tampilkan menu sesuai mockup `README.md`.
- Validasi input dengan `sc.validasi_pilihan(a, b)` yang mengembalikan `True` jika valid dan `False` jika tidak.
- Ulangi permintaan input sampai user memberikan pilihan yang valid.

## Testing

- *Validation test*: masukan di luar 1-3 ditolak.
- *Switching pages*: pilihan 1, 2, dan 3 mengarah ke halaman yang benar.
- *Fresh data*: tidak ada pertimbangan atau hasil filter yang tersisa dari sesi sebelumnya.
