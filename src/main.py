#Print('selamat di Pasar Buah')

#minta input user
nApel = int(input('masukkan jumlah Apel:'))
nJeruk = int(input('masukkan jumlah Jeruk:'))
nAnggur = int(input('masukkan jumlah Anggur:'))

#Definisikan harga buah
hargaApel=10000
hargaJeruk=15000
hargaAnggur=20000

#Hitung Total Harga
totalhargaApel = nApel*hargaApel
totalhargaJeruk = nJeruk*hargaJeruk
TotalhargaAnggur = nAnggur*hargaAnggur

#hitung total harga belanja
totalbelanja = totalhargaApel+totalhargaJeruk+TotalhargaAnggur

#tampilkan rincian belanja
print(f'''
detail belanja
 Apel:{nApel}*{hargaApel} = {totalhargaApel}
Jeruk: {nJeruk}*{hargaJeruk}= {totalhargaJeruk}
Anggur: {nAnggur}*{hargaAnggur}= {TotalhargaAnggur}
''')