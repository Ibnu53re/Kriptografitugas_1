#!/usr/bin/env python3
"""
Aplikasi Vigenère Cipher (Polyalphabetic Substitution)
Berdasarkan materi IF4020 Kriptografi - Ragam Cipher Klasik
Cipher abjad-majemuk: setiap huruf plainteks digeser dengan kunci yang berbeda.

Enkripsi: c_i = (p_i + k_i) mod 26
Dekripsi: p_i = (c_i - k_i) mod 26
di mana k_i diulang sesuai panjang kunci.
"""

def prepare_key(key: str, length: int) -> str:
    """Ulangi kunci sampai panjangnya sama dengan pesan (hanya huruf)."""
    key = ''.join(c for c in key.upper() if c.isalpha())
    if not key:
        raise ValueError("Kunci harus mengandung minimal satu huruf!")
    return (key * (length // len(key) + 1))[:length]


def vigenere_encrypt(plaintext: str, key: str) -> str:
    """Enkripsi dengan Vigenère Cipher."""
    letters = [c for c in plaintext if c.isalpha()]
    key_stream = prepare_key(key, len(letters))

    ciphertext = ""
    key_idx = 0
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            p = ord(char) - start
            k = ord(key_stream[key_idx]) - ord('A')
            c = (p + k) % 26
            ciphertext += chr(c + start)
            key_idx += 1
        else:
            ciphertext += char
    return ciphertext


def vigenere_decrypt(ciphertext: str, key: str) -> str:
    """Dekripsi dengan Vigenère Cipher."""
    letters = [c for c in ciphertext if c.isalpha()]
    key_stream = prepare_key(key, len(letters))

    plaintext = ""
    key_idx = 0
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            c = ord(char) - start
            k = ord(key_stream[key_idx]) - ord('A')
            p = (c - k) % 26
            plaintext += chr(p + start)
            key_idx += 1
        else:
            plaintext += char
    return plaintext


def main():
    print("=" * 55)
    print("  APLIKASI VIGENÈRE CIPHER")
    print("  (Polyalphabetic Substitution Cipher)")
    print("  IF4020 Kriptografi - Cipher Klasik")
    print("=" * 55)

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
        kunci = input("Masukkan kunci (kata/frase, hanya huruf digunakan): ").strip()
        if not any(c.isalpha() for c in kunci):
            print("Kunci harus mengandung minimal satu huruf alfabet!")
            continue

        try:
            if pilihan == "1":
                hasil = vigenere_encrypt(pesan, kunci)
                print(f"\nCipherteks: {hasil}")
            else:
                hasil = vigenere_decrypt(pesan, kunci)
                print(f"\nPlainteks: {hasil}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
