# AR_validasi-pilihan_1: Fungsi Validasi Pilihan

## Tujuan

Membuat fungsi pembantu yang memvalidasi pilihan angka dari user sebelum dipakai halaman mana pun.

## Context

- Fungsi ini dipakai oleh semua halaman, jadi tidak boleh meminta input sendiri.
- Parameter `a` adalah pilihan yang sudah berupa bilangan bulat, `b` adalah batas atas rentang.
- Rentang yang valid adalah `1` sampai `b` (inklusif).
- Gunakan notasi `sc.validasi_pilihan(a, b)`; tulisan `sc.validasi-pilihan(a,b)` tidak valid dalam Python.

## Steps

- Isi fungsi `validasi_pilihan(a: int, b: int) -> bool` di `shortcuts.py` tanpa mengubah signature-nya.
- Kembalikan `True` hanya jika `a` berupa `int` dan `1 <= a <= b`.
- Kembalikan `False` untuk nilai di luar rentang atau bukan bilangan bulat.

## Testing

- Input `1` dan `b` harus menghasilkan `True`.
- Input `0`, `b + 1`, dan nilai negatif harus menghasilkan `False`.
- Input bukan bilangan bulat harus menghasilkan `False`.
