# AR_menampilkan-makanan_3: Fungsi Menampilkan Makanan

## Tujuan

Menyediakan satu format tampilan makanan yang dipakai bersama oleh halaman hasil rekomendasi dan I'm Feeling Lucky.

## Context

- Format mengikuti mockup `README.md`: Nama makanan, Harga, Tenant, Lokasi.
- Penomoran dimulai dari `1`, bukan `0`.
- Fungsi ini hanya mencetak, tidak mengembalikan data.

## Steps

- Isi fungsi `menampilkan_makanan(daftar_makanan: list) -> None` di `shortcuts.py` tanpa mengubah signature-nya.
- Tampilkan setiap entri dengan empat field tersebut secara berurutan.
- Gunakan fungsi ini dari `hasil_rekomendasi` dan `im_feeling_lucky` supaya tampilan konsisten.

## Testing

- Satu entri tampil dengan nomor `1`.
- Beberapa entri tampil bernomor urut `1`, `2`, `3`, dan seterusnya.
- List kosong tidak menampilkan entri dan tidak menimbulkan error.
