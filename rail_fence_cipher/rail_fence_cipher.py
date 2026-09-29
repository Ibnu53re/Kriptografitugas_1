#!/usr/bin/env python3
"""
Aplikasi Rail Fence Cipher (Transposition Cipher)
Berdasarkan materi IF4020 Kriptografi - Ragam Cipher Klasik

Plainteks ditulis secara zigzag (naik-turun) pada sejumlah 'rail' (baris),
kemudian dibaca baris demi baris untuk menghasilkan cipherteks.
"""

def rail_fence_encrypt(plaintext: str, rails: int) -> str:
    """Enkripsi dengan Rail Fence Cipher."""
    if rails < 2:
        return plaintext

    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 = turun, -1 = naik

    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction

    ciphertext = ''.join(''.join(row) for row in fence)
    return ciphertext


def rail_fence_decrypt(ciphertext: str, rails: int) -> str:
    """Dekripsi dengan Rail Fence Cipher."""
    if rails < 2:
        return ciphertext

    n = len(ciphertext)
    # Hitung berapa karakter di setiap rail
    fence_len = [0] * rails
    rail = 0
    direction = 1
    for _ in range(n):
        fence_len[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction

    # Isi fence dengan karakter cipherteks
    fence = []
    idx = 0
    for length in fence_len:
        fence.append(list(ciphertext[idx:idx + length]))
        idx += length

    # Baca secara zigzag
    plaintext = []
    rail = 0
    direction = 1
    for _ in range(n):
        plaintext.append(fence[rail].pop(0))
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction = -direction

    return ''.join(plaintext)


def main():
    print("=" * 55)
    print("  APLIKASI RAIL FENCE CIPHER")
    print("  (Transposition Cipher)")
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
        try:
            rails = int(input("Masukkan jumlah rail / baris (minimal 2): "))
            if rails < 2:
                print("Jumlah rail minimal 2!")
                continue
        except ValueError:
            print("Jumlah rail harus bilangan bulat!")
            continue

        if pilihan == "1":
            hasil = rail_fence_encrypt(pesan, rails)
            print(f"\nCipherteks: {hasil}")
        else:
            hasil = rail_fence_decrypt(pesan, rails)
            print(f"\nPlainteks: {hasil}")


if __name__ == "__main__":
    main()
