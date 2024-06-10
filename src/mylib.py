def inputbuah(nama, stock, harga):
    while True:
        try:
            nbuah = int(input(f'Masukkan jumlah {nama} buah: '))
        except ValueError:
            print("Input harus berupa angka.")
            continue
        
        if nbuah > stock:
            print(f'Jumlah terlalu banyak, stok tersisa {stock} buah')
            continue
        break

    hargabuah = nbuah * harga

    return nbuah, hargabuah