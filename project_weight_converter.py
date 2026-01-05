weight = int(input("Kindly insert weight you want to convert: "))
option = input("Press L if this is Lbs or K if it is KG \n")
if option.upper() == "L":
    k = weight * 0.45
    print(f'Conversion is {k} kilos')
elif option.upper() == "K":
    l = weight / 0.45
    print(f'Conversion is {l} lbs')
else:
    print(f'Only K and L is allowed')