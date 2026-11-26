# DGN_hasil-rekomendasi_3: Membuat Hasil Rekomendasi Page

## Tujuan

Menampilkan seluruh hasil rekomendasi yang sudah difilter dan menanyakan apakah user ingin memesan untuk esok hari.

## Context

- Parameter `daftar_makanan` sudah berisi hasil filter dari `main.py`.
- Gunakan `sc.menampilkan_makanan(daftar_makanan)` agar formatnya sama dengan I'm Feeling Lucky.
- Jawaban yang diterima hanya Y atau N (huruf besar/kecil dibolehkan).

## Steps

- Isi fungsi `hasil_rekomendasi(daftar_makanan: list) -> bool` di `shortcuts.py`.
- Tampilkan daftar dengan bernomor mulai dari 1.
- Tanyakan `Apakah Anda ingin memesan untuk besok (Y/N) ?` dan ulangi sampai jawaban valid.
- Kembalikan `True` untuk Y dan `False` untuk N.

## Testing

- Daftar terisi tampil sesuai format empat field.
- Daftar kosong tidak menimbulkan error.
- Jawaban Y mengembalikan `True`, N mengembalikan `False`, jawaban lain ditolak.
