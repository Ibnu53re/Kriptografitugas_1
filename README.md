# Tugas Kriptografi 1

Classic Ciphers
Berisi 3 aplikasi cipher klasik dalam Python:

## Daftar Aplikasi

| No | Nama File              | Jenis Cipher              | Teknik Dasar     |
|----|------------------------|---------------------------|------------------|
| 1  | `caesar_cipher.py`     | Caesar Cipher             | Substitusi       |
| 2  | `vigenere_cipher.py`   | Vigenère Cipher           | Substitusi       |
| 3  | `rail_fence_cipher.py` | Rail Fence Cipher         | Transposisi      |

---

## 1. Caesar Cipher

### Deskripsi
Caesar Cipher adalah cipher substitusi monoalfabetik yang paling terkenal. Setiap huruf alfabet digeser sejauh `k` posisi ke kanan (untuk enkripsi) atau ke kiri (untuk dekripsi).

### Rumus Matematis
Misalkan setiap huruf dikodekan menjadi bilangan 0–25 (A=0, B=1, ..., Z=25):

- **Enkripsi**: \( c = E(p) = (p + k) \mod 26 \)
- **Dekripsi**: \( p = D(c) = (c - k) \mod 26 \)

di mana `k` adalah kunci rahasia (0 ≤ k ≤ 25).

### Cara Menjalankan
```bash
python3 caesar_cipher.py
```

### Contoh Pengunaan

```
==================================================
  APLIKASI CAESAR CIPHER
  IF4020 Kriptografi - Cipher Klasik
==================================================

Menu:
1. Enkripsi
2. Dekripsi
3. Keluar
Pilih menu (1/2/3): 1
Ketikkan pesan: ADA RENCANA PENYELUNDUPAN NARKOBA DI BANDARA
Masukkan kunci (0-25): 5

Cipherteks: FIFI WJSHFSF SJSDJQZSIDUFS SFWPTEF IN GFSIFWF
```

## 2. Vigenere Cipher

### Deskripsi
Vigenère Cipher termasuk cipher abjad-majemuk (polyalphabetic substitution cipher). Berbeda dengan Caesar yang menggunakan satu kunci untuk semua huruf, Vigenère menggunakan kunci yang berbeda untuk setiap huruf plainteks. Kunci diulang secara periodik sepanjang pesan.

### Rumus Matematis
Enkripsi: $c_i = (p_i + k_i) \mod 26$
Dekripsi: $p_i = (c_i - k_i) \mod 26$

di mana $k_i$ adalah huruf kunci ke-i yang diulang sesuai panjang pesan.

### Cara Menjalankan
```bash
python3 vigenere_cipher.py
```

### Contoh Pengunaan

```
=======================================================
  APLIKASI VIGENÈRE CIPHER
  (Polyalphabetic Substitution Cipher)
  IF4020 Kriptografi - Cipher Klasik
=======================================================

Menu:
1. Enkripsi
2. Dekripsi
3. Keluar
Pilih menu (1/2/3): 1
Ketikkan pesan: MENGANTUK
Masukkan kunci (kata/frase, hanya huruf digunakan): KUNCI

Cipherteks: WIRGPTXEM
```

## 3. Rail Fence Cipher

### Deskripsi
Rail Fence Cipher adalah cipher transposisi. Plainteks ditulis secara zigzag (naik-turun) pada sejumlah rail (baris), kemudian dibaca baris demi baris untuk menghasilkan cipherteks.

### Cara Menjalankan
```bash
python3 rail_fence_cipher.py
```

### Contoh Pengunaan

```
=======================================================
  APLIKASI RAIL FENCE CIPHER
  (Transposition Cipher)
  IF4020 Kriptografi - Cipher Klasik
=======================================================

Menu:
1. Enkripsi
2. Dekripsi
3. Keluar
Pilih menu (1/2/3): 1
Ketikkan pesan: CRYPTOGRAPHY AND DATA SECURITY
Masukkan jumlah rail / baris (minimal 2): 3

Cipherteks: CTAAAEIRPORPYNDTSCRTYGHDAUY
```
