# FTZ_penentuan-harga_3: Membuat Penentuan Harga Page

## Tujuan

Membuat halaman pemilihan rentang harga yang mengembalikan nomor rentang untuk dipakai `check_harga`.

## Context

- Menu mengikuti mockup `README.md`: enam rentang harga dan pilihan 7 = Kembali.
- Rentang ditulis dengan batas atas eksklusif, misalnya `10.000 - < 15.000`.
- Validasi memakai `sc.validasi_pilihan(a, b)`.

## Steps

- Isi fungsi `penentuan_harga() -> int | None` di `shortcuts.py`: tidak menerima parameter.
- Tampilkan menu dengan prompt `Masukkan pilihan (1-7) =`.
- Ulangi input sampai valid.
- Kembalikan nomor rentang 1-6, atau `None` jika user memilih Kembali.

## Testing

- Input 1-6 mengembalikan nomor rentang yang sesuai.
- Input 7 mengembalikan `None`.
- Input 0, 8, atau bukan angka ditolak.
