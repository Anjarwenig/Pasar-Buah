import mylib

def tampilkan_pesan_selamat_datang():
    print('Selamat datang di Pasar Buah')

def definisikan_stok_dan_harga():
    stok = {'Apel': 10, 'Jeruk': 8, 'Anggur': 15}
    harga = {'Apel': 10000, 'Jeruk': 15000, 'Anggur': 20000}
    return stok, harga

def dapatkan_data_buah(stok, harga):
    data_buah = {}
    for buah, st in stok.items():
        jumlah, total_harga = mylib.inputbuah(nama=buah, stock=st, harga=harga[buah])
        data_buah[buah] = (jumlah, total_harga)
    return data_buah

def hitung_total(data_buah):
    return sum(total for _, total in data_buah.values())

def tampilkan_detail_belanja(data_buah, total_belanja):
    print("\nDetail belanja:")
    for buah, (jumlah, total_harga) in data_buah.items():
        print(f"{buah}: {jumlah} * {harga[buah]} = {total_harga}")
    print(f"Total Belanja: {total_belanja}")

def proses_pembayaran(total_belanja):
    while True:
        try:
            bayar = int(input('Silahkan masukkan uang anda: '))
            selisih = bayar - total_belanja
            if selisih < 0:
                print(f'Uang anda kurang sebesar Rp.{abs(selisih)}')
                continue
            else:
                print(f'Terima kasih, uang kembalian anda: Rp.{selisih}')
                break
        except ValueError:
            print("Masukkan angka yang valid.")

# Eksekusi program utama
tampilkan_pesan_selamat_datang()
stok, harga = definisikan_stok_dan_harga()
data_buah = dapatkan_data_buah(stok, harga)
total_belanja = hitung_total(data_buah)
tampilkan_detail_belanja(data_buah, total_belanja)
proses_pembayaran(total_belanja)
