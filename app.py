import math

g = 9.81
m1 = float(input("Ingrese la masa 1 en kg: "))
m2 = float(input("Ingrese la masa 2 en kg: "))
dif_m = abs(m1 - m2)

a = g * dif_m / (m1 + m2)
t = 2*m1*m2*g / (m1 + m2)

print("Magnitud de la aceleración: {:.2f} m/s^2".format(a))
print("Tensión en la cuerda sin peso: {:.2f} N".format(t))
