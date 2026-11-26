# TASK RULE (PEDOMAN DALAM MENGERJAKAN PENUGASAN)

## ID Task

Setiap task memiliki ID dengan format:

```text
<inisial nama>_<judul task>_<urutan task>
```

Contoh: `AR_validasi-pilihan_1`

Judul task ditulis tanpa spasi. Jika lebih dari satu kata, pisahkan dengan tanda `-`. Nama file task mengikuti ID, yaitu `<ID task>.md`.

| Inisial | Anggota | Folder |
|---|---|---|
| AR | Aksa Rachman | `task/Aksa Rachman/` |
| DGN | Davin Gusti Nurandi | `task/Davin Gusti Nurandi/` |
| FTZ | Fathyakan Thorique Zidane | `task/Fathyakan Thorique Zidane/` |
| MRHK | Mahesa Rahasia Hati Kahfilano | `task/Mahesa Rahasia Hati Kahfilano/` |

## Pengerjaan

1. Kerjakan penugasan yang ada di folder masing-masing (**JANGAN SALAH PILIH FOLDER YA**).
2. Ikuti panduan **framework git** di [framework_git.md](framework_git.md).
3. Nama branch mengikuti aturan:

   ```text
   <ID task>_branch
   ```

   Contoh: `AR_validasi-pilihan_1_branch`

4. Utamakan dokumentasi. Tiap baris kode harus mudah dipahami; beri komentar yang singkat, padat, dan jelas.
5. Tulis PR sesuai [pull_request_template.md](../.github/pull_request_template.md).
6. Seluruh fungsi bersama sudah memiliki nama, parameter, dan return yang ditetapkan di `shortcuts.py`. Isi logikanya sesuai task yang menjadi tanggung jawabmu tanpa mengubah signature-nya.
7. File bersama (`main.py`, `shortcuts.py`, `database.py`, `README.md`, dan `docs/`) dikerjakan terpusat, bukan bagian dari task individu.

## Bantuan

Jika ada kendala, komunikasikan langsung di group ya.
