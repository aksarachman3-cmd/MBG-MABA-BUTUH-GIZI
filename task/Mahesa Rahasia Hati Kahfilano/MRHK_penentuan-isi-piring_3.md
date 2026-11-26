# MRHK_penentuan-isi-piring_3: Membuat Penentuan Isi Piring Page

## Tujuan

Membuat halaman pemilihan komponen isi piring yang bisa dipilih lebih dari satu.

## Context

- Menu mengikuti mockup `README.md`: Nasi, Protein hewani, Protein nabati, Sayur, dan Kembali.
- Pilihan 5 = Kembali tidak boleh digabung dengan nomor lain.
- Format input beberapa nomor dalam satu baris, dipisah spasi, misalnya `1 4`.
- Validasi tiap nomor memakai `sc.validasi_pilihan(a, b)`.

## Steps

- Isi fungsi `penentuan_isi_piring() -> list[int] | None` di `shortcuts.py`: tidak menerima parameter.
- Tampilkan menu dengan prompt `Masukkan pilihan (1-5) =` dan keterangan bahwa pilihan bisa multiple.
- Ulangi input sampai semua nomor valid.
- Kembalikan daftar nomor yang dipilih, atau `None` jika user memilih Kembali.

## Testing

- Input `1` mengembalikan `[1]`.
- Input `1 4` mengembalikan `[1, 4]`.
- Input `5` mengembalikan `None`; input `1 5` ditolak.
- Input `0`, `6`, atau duplikasi nomor ditolak.
