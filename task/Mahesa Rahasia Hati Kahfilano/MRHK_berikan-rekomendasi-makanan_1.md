# MRHK_berikan-rekomendasi-makanan_1: Membuat Berikan Rekomendasi Makanan Page

## Tujuan

Membuat halaman yang memilih satu pertimbangan dari daftar yang masih tersedia, lalu mengarahkan ke halaman penentuan yang sesuai.

## Context

- Jangan menulis pertimbangan secara manual. Ambil dari `daftar_pertimbangan` yang ada di `shortcuts.py`.
- Teks "pertimbangan pertama", "pertimbangan kedua", dan "pertimbangan ketiga" bersifat otomatis. Cocokkan `counter` dengan `urutan`.
- Nomor menu dimulai dari 1, bukan 0.
- Validasi hanya menerima angka 1 sampai `len(daftar_pertimbangan)`.
- Setelah dipilih, pertimbangan tersebut dihapus dari `daftar_pertimbangan`.

## Steps

- Isi fungsi `berikan_rekomendasi_makanan() -> str` di `shortcuts.py`: tidak menerima parameter.
- Tampilkan pertimbangan yang masih tersedia dengan perulangan `for`.
- Tampilkan pilihan Kembali sebagai opsi terakhir.
- Validasi input dengan `sc.validasi_pilihan(a, b)` yang mengembalikan `True` jika valid dan `False` jika tidak.
- Kembalikan nilai `daftar_pertimbangan[indeks]`, misalnya `"Lokasi"`, bukan hasil ketikan user.
- Hapus elemen yang dipilih dari `daftar_pertimbangan` sebelum fungsi selesai.

## Testing

- *Validation test*: input di luar rentang ditolak.
- *Switching pages*: pilihan Lokasi, Harga, dan Isi Piring mengarah ke halaman yang benar.
- *Fresh data*: daftar pertimbangan dikembalikan ke kondisi awal oleh `sc.reset_state()`.
- *Tampilan pertimbangan*: nomor mulai dari 1; contoh tampilan salah adalah `0. Lokasi`.
- *Menghapus pertimbangan*: pertimbangan yang sudah dipilih tidak muncul lagi.
