# FRAMEWORK GIT (SIKLUS PENGERJAAN TASK)

Setiap task dikerjakan dengan siklus berikut. **Ulangi dari langkah 2 untuk setiap task baru.**

## Aturan Utama
- **Jangan commit langsung ke branch `main`.** Semua pekerjaan dilakukan di branch task masing-masing.
- Satu branch untuk satu task.
- Hanya ubah file di folder masing-masing.

## Persiapan Awal (Cukup Sekali)

Clone repository ke komputer:

```bash
git clone <link-repository>
cd <nama-folder>
```

## Siklus Pengerjaan Task

### 1. Update `main` ke versi terbaru

Lakukan ini sebelum mulai task baru supaya tidak ketinggalan pekerjaan teman.

```bash
git checkout main
git pull origin main
```

### 2. Buat branch baru

Nama branch mengikuti aturan di `task_rule.md`:

```bash
git checkout -b <ID task>_branch
```

Contoh:

```bash
git checkout -b AR_penentuan-harga_1_branch
```

### 3. Kerjakan task

Kerjakan penugasan di folder masing-masing. Jangan lupa beri komentar pada kode.

Cek file apa saja yang berubah:

```bash
git status
```

### 4. Commit perubahan

Tambahkan file dari folder kamu, lalu commit dengan pesan yang jelas:

```bash
git add <folder-masing-masing>/
git commit -m "<ID task>: deskripsi singkat perubahan"
```

Contoh:

```bash
git commit -m "AR_penentuan-harga_1: tambah menu pilihan range harga"
```

Commit boleh dilakukan beberapa kali selama mengerjakan task.

### 5. Push branch ke GitHub

Push pertama kali:

```bash
git push -u origin <ID task>_branch
```

Push berikutnya cukup:

```bash
git push
```

### 6. Buat Pull Request (PR)

1. Buka repository di GitHub, lalu klik **Compare & pull request**.
2. Pastikan base-nya `main` dan compare-nya branch kamu.
3. Isi PR sesuai `PR_template.md`.
4. Klik **Create pull request**.

### 7. Review dan revisi

- Minta anggota lain untuk mereview PR kamu.
- Jika ada revisi, perbaiki di branch yang sama, lalu `git add`, `git commit`, dan `git push` lagi. PR akan terupdate otomatis.

### 8. Merge

Setelah PR disetujui, klik **Merge pull request** di GitHub.

### 9. Bersihkan dan kembali ke `main`

```bash
git checkout main
git pull origin main
git branch -d <ID task>_branch
```

Lanjut ke task berikutnya mulai dari langkah 1.

## Jika Terjadi Conflict

Jika muncul conflict saat `git pull` atau merge, **jangan dipaksa**. Komunikasikan di group terlebih dahulu.