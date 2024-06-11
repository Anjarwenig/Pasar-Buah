def buy(database):
    # Show the available fruits
    show(database)

    # Ask the user for the name of the fruit they want to buy
    fruit_name = string_validation('Enter the fruit you want to buy: ')

    # Find the fruit in the database
    for buah in database:
        if fruit_name.lower() == buah[2].lower():  # Assuming the fruit name is stored at index 2
            # Ask how many they want to buy
            nBuah = integer_validation(f'How many kilograms of {buah[2]} do you want to buy? ')

            # Check if the requested amount is available
            if nBuah > buah[1]:  # Assuming the stock is stored at index 1
                print(f'Too many requested. Only {buah[1]} kg available.')
            else:
                # Calculate total cost
                total_cost = nBuah * buah[3]  # Assuming price is stored at index 3
                # Update the stock
                buah[1] -= nBuah
                print(f'You bought {nBuah} kg of {buah[2]}. Total cost: {total_cost}.')

            break
    else:
        print('The fruit you requested is not in our stock.')

    # Show the updated database
    show(database)
