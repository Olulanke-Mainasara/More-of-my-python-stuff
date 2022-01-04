 #Program to display property taxes

TAX_FACTOR = 0.0065

print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))

while lot != 0:
    # Getting poperty value.
    value = float(input('Enter the property value: '))

    # Calculating the tax of the property
    tax = value * TAX_FACTOR

    # Display the tax.
    print('Property tax: ',tax)

    # Getting the next lot number.
    print('Enter the next lot number or')
    print('enter 0 to end.')
    lot = int(input('Lot number: '))