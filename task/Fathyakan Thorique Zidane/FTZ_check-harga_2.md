# FTZ_check-harga_2: Fungsi Check Harga

## Tujuan

Menyediakan fungsi filter makanan berdasarkan rentang harga yang dipilih user.

## Context

- Harga di `database.py` berupa bilangan bulat dalam rupiah, misalnya `16000`.
- Batas atas rentang bersifat eksklusif agar tidak ada harga yang masuk dua rentang.
- `check_harga` menerima data yang sudah difilter sebelumnya sehingga filter bisa dirangkai.

## Steps

- Isi fungsi `check_harga(rentang: int, data: list) -> list` di `shortcuts.py` tanpa mengubah signature-nya.
- Petakan `rentang` sebagai berikut: 1 = `< 10000`, 2 = `10000 - < 15000`, 3 = `15000 - < 20000`, 4 = `20000 - < 25000`, 5 = `25000 - < 30000`, 6 = `>= 30000`.
- Kembalikan list entri yang harganya memenuhi rentang tersebut.

## Testing

- Harga `10000` masuk rentang 2, bukan rentang 1.
- Harga `15000` masuk rentang 3, bukan rentang 2.
- Harga `30000` masuk rentang 6.
- Rentang tanpa entri yang cocok mengembalikan list kosong.
