print("-------------------------")
print("--------MINDBREAK--------")
print("-------------------------")
print("-------------------------")
print("-----LISTA-DE-PAÍSES-----")
print("-------------------------")

print("1. Brasil")
print("2. Canadá")
print("3. Japón")
print("4. España")
print("5. Inglaterra")

O = int (input("Digite el código de un país"))

if O == 1:
    R1 = "País: BRASIL"
    R2 = "Capital: Brasilia"
    R3 = "Continente: Sur América"
    R4 = "Idioma: Portugués"
    R5 = "Religión: Cristianismo"
    R6 = "Moneda oficial: Real Brasileño"
elif O ==2:
    R1 = "País: CANADÁ"
    R2 = "Capital: Ottawa"
    R3 = "Continente: Norte América"
    R4 = "Idiomas: Francés, Inglés"
    R5 = "Religión: Cristianismo"
    R6 = "Moneda oficial: Dólar canadiense"
elif O ==3:
    R1 = "País: JAPÓN"
    R2 = "Capital: Tokio"
    R3 = "Continente: Asia"
    R4 = "Idioma: Japonés"
    R5 = "Religión: Sintoísmo"
    R6 = "Moneda oficial: Yen japonés"
elif O ==4:
    R1 = "País: ESPAÑA"
    R2 = "Capital: Madrid"
    R3 = "Continente: Europa"
    R4 = "Idioma: Español"
    R5 = "Religión: Cristianismo"
    R6 = "Moneda oficial: Euro"
elif O ==5:
    R1 = "País: INGLATERRA"
    R2 = "Capital: Londres"
    R3 = "Continente: Europa"
    R4 = "Idioma: Inglés Británico"
    R5 = "Religión: Cristianismo"
    R6 = "Moneda oficial: Libra Esterlina"
else: 
    print("El código del país no es válido")


print("----------------------")
print("-----Datos del país---")
print("Los datos del país elegido son:", R1, R2, R3, R4, R5, R6, sep="\n")