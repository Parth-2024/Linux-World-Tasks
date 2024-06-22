temp=float(input("Enter temperature:"))
print("1.C-Celcius\n2.F-Fahrenheit\n3.K-Kelvin")
unit=input("Enter the unit of the input temperature:")
convert=input("Enter the unit you want to convert your input temperature in:")
final_temp=None
if convert=='F':
    if unit=='C':
        final_temp=temp*(9/5)+32
    elif unit=='K':
        final_temp=(temp-273.15)*(9/5)+32
elif convert=='C':
    if unit=='F':
        final_temp=(temp-32)*(5/9)
    elif unit=='K':
        final_temp=temp-273.15
elif convert=='K':
    if unit=='F':
        final_temp=(temp-32)*(5/9)+273.15
    elif unit=='C':
        final_temp=temp+273.15
if(final_temp!=None):
    print(f"{temp} {unit}={final_temp} {convert}")
else:
    print("Invalid enties")