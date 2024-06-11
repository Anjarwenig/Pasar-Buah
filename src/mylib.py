def inputBuah(nama, stock, harga):
    """Fungsi meminta user untuk input jumlah buah 
    dan menghitung harganya.

    Args:
        nama (String): Nama buah yang akan dibeli
        stock (Integer): Stock buah yang akan dibeli
        harga (Integer): Harga buah per kg

    Returns:
        nBuah (Integer): Jumlah buah yang dipesan 
        hargaBuah (Integer): Total harga buah
    """
    '''while True:
        # Input jumlah buah
        nBuah = int(input(f'Masukkan jumlah {nama}: '))

        # Membandingkan antara jumlah permintaan dengan stock
        if nBuah > stock:
            print(f'Jumlah terlalu banyak, stock tersisa {stock} buah')
            continue

        # Berhenti minta input, ketika jumlah permintaan terpenuhi
        break

    # Hitung total harga untuk buah tersebut
    hargaBuah = nBuah * harga

    return nBuah, hargaBuah'''

from tabulate import tabulate 

def string_validation(title):
    while True:
        a= input(title)
        if a.isalpha()==True:
            break
        else:
            print('silahkan inputkan hanya teks:')
    return a.capitalize()


# def integer_validation(title, minval=0, maxval=100): #title karena dalam formulasi idx di baris 78, dalam ger_validation ada textnya
#     while True:
#         a= input(title)
#         try:
#             a=int(a)
#             break
#         except:print('yang anda inputkan bukan bilangan')
#     return a

def integer_validation(title, minval=0, maxval=100):
    while True:
        num=input(title)
        try:
            num=int(num)
            if num>=minval and  num<=maxval:
                break
            else:
                print('Angka yang anda masukkan diluar rentang')
        except:
            print('Yang anda imput buakan bilangan')
    return num





def show(database,header=['index','nama', 'stock', 'price']):
    print(tabulate(database, 
                   headers=header, 
                   tablefmt='grid'))

def add(database):
    name=input('Masukkan nama buah: ')
    stock=input('Masukkan stock buah: ')
    price=input('Masukkan harga buah: ')

#
    for id, buah in enumerate(database):
        if name in buah:
            database[id]= [id, name, stock, price]
            break
        else:
            database.append([id+1, name, stock, price])

    #menampilkan database ter-update
    show(database)

def delete(database):
    #tampilkan database terbaru
    show(database)

    #meminta user input nindeks yang akan dihapus
    idx= integer_validation('masukkan indeks buah yang akan dihapus: ')

    #melakukan proses penghapusan sesuai index
    for buah in database:
        if idx==buah[0]:
            del database[idx]
            break
    else:
        print('buah yang anda cari tidak ada')
    #memperbarui index
    for id, buah in enumerate(database):
        if id ==buah[0]:
            continue
        else:
            database[id] [0]= id
    #show database terbaru

def buy(database):
    # Menyalin database ke dalam penyimpanan sementara
    databaseTemp = database.copy()
    
    # Definisi variabel untuk menyimpan belanjaan
    keranjang = []

    # Proses pembelian
    reorder = None
    while reorder != 'No':
        # Menampilkan database
        show(databaseTemp)

        # Meminta input untuk indeks dan jumlah buah yang ingin dibeli
        id = integer_validation(
            title='Silahkan masukkan indeks buah: ',
            minval=0,
            maxval=len(databaseTemp)-1
            )
        stock = integer_validation(
            title='Silahkan masukkan jumlah buah: ',
            minval=0,
            maxval=databaseTemp[id][2]
            )
        
        # Menambahkan ke dalam keranjang belanja
        keranjang.append([databaseTemp[id][1], stock, databaseTemp[id][3]])

        # Menampilkan keranjang belanja
        show(database=keranjang, header=['Nama', 'Qty', 'Harga'])

        # Konfirmasi reorder
        while True:
            status = string_validation('Mau beli yang lain?: ').lower()
            if status in ['yes', 'y', 'ya']:
                reorder = 'Yes'
            elif status in ['no', 'n', 'tidak']:
                reorder = 'No'
            break

        # Update stock sementara
        databaseTemp[id][2] -= stock

    # Menghitung total harga
    total = 0
    for id, item in enumerate(keranjang):
        # Hitung total harga per buah
        totalHargaBuah = item[1] * item[2]

        # Input total harga ke keranjang
        keranjang[id].append(totalHargaBuah)

        # Sum seluruh harga
        total += totalHargaBuah

    # Menampilkan keranjang belanja
    show(database=keranjang, header=['Nama', 'Qty', 'Harga', 'Total Harga'])

    # Menampilkan uang yang harus dibayar
    print(f'Uang yang harus Anda bayarkan adalah Rp.{total}')

    # Proses pembayaran
    pembayaran(total)

    # Update database
    database = databaseTemp.copy()


#menghitung total harga
def pembayaran(totalHarga):
    while True:
        # Input jumlah uang
        bayar = int(input('Silahkan masukkan uang Anda: '))

        # Hitung selisih antara bayar dengan total
        selisih = totalHarga - bayar

        # Bandingkan antara uang dengan total harga
        if selisih > 0: 
            print(f'Uang Anda kurang sebesar Rp.{selisih}')
            continue
        
        # Ucapkan terima kasih ketika selesai pembayaran
        else:
            print(f'''Terimakasih. Uang kembalian Anda: {abs(selisih)}''')
            break
