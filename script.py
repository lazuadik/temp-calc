temp_is = float(input('Masukkan suhu dalam Celcius (e.g 20, 35): '))
convert_temp = input('Convert dari apa ke apa? (e.g F to C, K to R, C to F): ')

if convert_temp == 'C to F':
    result = float((9* temp_is) / 5 + 32)
    o_convention = 'Fahrenheit'
elif convert_temp == 'C to K':
    result = float((temp_is + 273))
    o_convention = 'Kelvin'
elif convert_temp == 'C to R':
    result = float((4 * temp_is) / 5)
    o_convention = 'Reamur'
elif convert_temp == 'F to C':
    result = float((5* temp_is) /9 - 32)
    o_convention = 'Celcius'
elif convert_temp == 'F to K':
    result = float((5* (temp_is-32)) / 9 + 273)
    o_convention = 'Kelvin'
elif convert_temp == 'F to R':
    result = float((4* temp_is) / 9 -32)
    o_convention = 'Reamur'
elif convert_temp == 'K to C':
    result = float((temp_is - 273))
    o_convention = 'Celcius'
elif convert_temp == 'K to F':
    result = float((9* (temp_is - 273)) / 5 + 32)
    o_convention = 'Fahrenheit'
elif convert_temp == 'K to R':
    result = float((4* temp_is) / 5 - 273)
    o_convention = 'Reamur'
elif convert_temp == 'R to C':
    result = float((5* temp_is) / 4)
    o_convention = 'Celcius'
elif convert_temp == 'R to F':
    result = float((9* temp_is) / 4 + 32)
    o_convention = 'Fahrenheit'
elif convert_temp == 'R to K':
    result = float((5* temp_is) / 4 + 273)
    o_convention = 'Kelvin' 
else:
    print('Yang bener masukinnya!')
    quit()

print("The temperature in", o_convention, "is", result, "degrees.")
