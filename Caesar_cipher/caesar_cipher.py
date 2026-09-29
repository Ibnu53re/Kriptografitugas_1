
```python
#!/usr/bin/env python3
"""
Aplikasi Caesar Cipher
Berdasarkan materi IF4020 Kriptografi - Ragam Cipher Klasik
Oleh: Dr. Ir. Rinaldi, M.T

Enkripsi: c = (p + k) mod 26
Dekripsi: p = (c - k) mod 26
"""

def caesar_encrypt(plaintext: str, k: int) -> str:
    """Enkripsi pesan dengan Caesar Cipher (geser k huruf ke kanan)."""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            c = (ord(char) - start + k) % 26
            ciphertext += chr(c + start)
        else:
            ciphertext += char  # karakter non-huruf dibiarkan
    return ciphertext


def caesar_decrypt(ciphertext: str, k: int) -> str:
    """Dekripsi pesan dengan Caesar Cipher (geser k huruf ke kiri)."""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            p = (ord(char) - start - k) % 26
            plaintext += chr(p + start)
        else:
            plaintext += char
    return plaintext


def main():
    print("=" * 50)
    print("  APLIKASI CAESAR CIPHER")
    print("  IF4020 Kriptografi - Cipher Klasik")
    print("=" * 50)

    while True:
        print("\nMenu:")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "3":
            print("Terima kasih! Program selesai.")
            break

        if pilihan not in ("1", "2"):
            print("Pilihan tidak valid!")
            continue

        pesan = input("Ketikkan pesan: ")
        try:
            k = int(input("Masukkan kunci (0-25): "))
            if not (0 <= k <= 25):
                print("Kunci harus antara 0 sampai 25!")
                continue
        except ValueError:
            print("Kunci harus berupa bilangan bulat!")
            continue

        if pilihan == "1":
            hasil = caesar_encrypt(pesan, k)
            print(f"\nCipherteks: {hasil}")
        else:
            hasil = caesar_decrypt(pesan, k)
            print(f"\nPlainteks: {hasil}")


if __name__ == "__main__":
    main()
