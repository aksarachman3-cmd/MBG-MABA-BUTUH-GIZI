# FTZ_im-feeling-lucky_1: Membuat I'm Feeling Lucky Page

## Tujuan

Memberikan satu rekomendasi makanan acak dari seluruh data dan menanyakan apakah user ingin memesan untuk esok hari.

## Context

- Pilihan diambil secara acak dari `database.py`, bukan dari hasil filter pertimbangan.
- Tampilan mengikuti mockup `README.md` dan memakai `sc.menampilkan_makanan(...)`.
- Jawaban yang diterima hanya Y atau N.

## Steps

- Isi fungsi `im_feeling_lucky() -> bool` di `shortcuts.py`: tidak menerima parameter.
- Pilih satu entri secara acak dari `database`.
- Tampilkan entri tersebut, lalu tanyakan `Apakah Anda ingin memesan untuk besok (Y/N) ?`.
- Kembalikan `True` untuk Y dan `False` untuk N.

## Testing

- Entri yang tampil benar-benar berasal dari `database.py`.
- Beberapa kali pemanggilan menunjukkan variasi pilihan.
- Jawaban Y/N valid; jawaban lain ditolak.
