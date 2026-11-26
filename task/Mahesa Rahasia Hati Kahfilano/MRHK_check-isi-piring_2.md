# MRHK_check-isi-piring_2: Fungsi Check Isi Piring

## Tujuan

Menyediakan fungsi filter makanan berdasarkan komponen isi piring yang diminta user.

## Context

- Setiap entri `database.py` memiliki field gizi `[nasi, protein hewani, protein nabati, sayur]`.
- Pemetaan nomor komponen: 1 = nasi (index 0), 2 = protein hewani (index 1), 3 = protein nabati (index 2), 4 = sayur (index 3).
- Semua komponen yang diminta harus bernilai `True`.
- `check_isi_piring` menerima data yang sudah difilter sebelumnya sehingga filter bisa dirangkai.

## Steps

- Isi fungsi `check_isi_piring(komponen: list[int], data: list) -> list` di `shortcuts.py` tanpa mengubah signature-nya.
- Ubah tiap nomor komponen menjadi index field gizi yang sesuai.
- Kembalikan entri yang memenuhi semua komponen yang diminta.

## Testing

- Komponen `[1]` hanya mengembalikan entri dengan nasi.
- Komponen `[1, 4]` hanya mengembalikan entri dengan nasi dan sayur.
- Kombinasi komponen yang tidak ada pada data mengembalikan list kosong.
