# DGN_pemesanan_2: Membuat Pemesanan Page

## Tujuan

Membuat halaman pemesanan untuk memilih waktu pengambilan makanan esok hari.

## Context

- Halaman ini dipanggil setelah user menjawab Y di Hasil Rekomendasi atau I'm Feeling Lucky.
- Tersedia lima slot waktu: 9.00-10.00, 10.00-11.00, 11.00-12.00, 12.00-13.00, 13.00-14.00.
- Pilihan 6 adalah Kembali.

## Steps

- Isi fungsi `pemesanan() -> int | None` di `shortcuts.py`: tidak menerima parameter.
- Tampilkan menu sesuai mockup `README.md` dengan prompt `Masukkan pilihanmu (1-6) =`.
- Validasi input dengan `sc.validasi_pilihan(a, b)`.
- Kembalikan nomor slot 1-5, atau `None` jika user memilih Kembali.

## Testing

- Input 1-5 mengembalikan nomor slot yang sesuai.
- Input 6 mengembalikan `None`.
- Input 0, 7, atau bukan angka ditolak.
