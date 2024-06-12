from math import sqrt

pw = float(input("توان را وارد کنید :"))
Density = float(input("چگالی جربان :"))
first_voltage = float(input("ولتاژ اولیه :"))
second_voltage = float(input("ولتاژ ثانویه :"))

Area = round(pw / (Density * second_voltage), 4)

r1 = round(first_voltage / sqrt(2), 4)
r2 = round(second_voltage / sqrt(2), 4)

print(f"مساخت مقطع هسته {Area}")
print(f"دور های پیچش اولیه {r1}")
print(f"دور های پیچش ثانویه {r2}")


with open("4", "w") as file:
    file.write(f"{Area}, {r1}, {r2}\n")
