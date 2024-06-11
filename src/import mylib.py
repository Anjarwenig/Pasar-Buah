import mylib

def print_welcome_message():
    print('Selamat datang di Pasar Buah')

def define_stock_and_prices():
    stock = {'Apel': 10, 'Jeruk': 8, 'Anggur': 15}
    prices = {'Apel': 10000, 'Jeruk': 15000, 'Anggur': 20000}
    return stock, prices

def get_fruit_data(stock, prices):
    fruit_data = {}
    for fruit, st in stock.items():
        n, total_price = mylib.inputbuah(nama=fruit, stock=st, harga=prices[fruit])
        fruit_data[fruit] = (n, total_price)
    return fruit_data

def calculate_total(fruit_data):
    return sum(total for _, total in fruit_data.values())

def print_shopping_details(fruit_data, total_belanja):
    print("\nDetail belanja:")
    for fruit, (amount, total_price) in fruit_data.items():
        print(f"{fruit}: {amount} * {prices[fruit]} = {total_price}")
    print(f"Total Belanja: {total_belanja}")

def process_payment(total_belanja):
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

# Main program execution
print_welcome_message()
stock, prices = define_stock_and_prices()
fruit_data = get_fruit_data(stock, prices)
total_belanja = calculate_total(fruit_data)
print_shopping_details(fruit_data, total_belanja)
process_payment(total_belanja)
