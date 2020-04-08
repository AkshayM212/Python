weight = int(input('Enter your weight: '))
weight_type = input('(L)bs or (K)g: ')
weight_type2 = weight_type.capitalize()
if weight_type2 == 'K':
    weight_in_pounds = weight * 2.20462
    print(weight_in_pounds)
elif weight_type2 == 'L':
    weight_in_kg = weight * 0.453592
    print(weight_in_kg)