from math import pow

P = 10000
n = 12
r = 0.08
time = int(input("Inserisci il numero di anni: "))
factor = 1 + (r / n)
total_amount = P * pow(factor, n * time)
print("The total amount after " + str(time) + " years is: " + str(total_amount))
