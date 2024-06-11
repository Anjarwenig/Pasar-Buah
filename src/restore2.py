from tabulate import tabulate
'''1.Menampilkan Daftar Buah (Display List of Fruits)
2. Menambah Buah (Add Fruit)
3. Menghapus Buah (Delete Fruit)
4. Membeli Buah (Buy Fruit)
5. Exit Program (Exit Program)'''

#input user
input= (input'masukkan nama buah         :')
input= (input'masukkan stock buah       :')
input= (input'masukkan harga buah        :')

print(tabulate(daftarbuah,
               headers=[index],