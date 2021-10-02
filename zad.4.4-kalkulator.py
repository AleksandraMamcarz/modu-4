operation=input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
if operation == '1':
    number=float(input("Składnik 1:"))
    number_1=float(input("Składnik 2:"))
    output=number+number_1
    print("Dodaję %s %s" % (number, number_1))
    
    
elif operation == '2':
    number=float(input("Składnik 1:"))
    number_1=float(input("Składnik 2:"))
    output=number-number_1
    print("Odejmuję %s %s" % (number, number_1))

elif operation == '3':
    number=float(input("Składnik 1:"))
    number_1=float(input("Składnik 2:"))
    output=number*number_1
    print("Mnożę %s %s" % (number, number_1))

elif operation == '4':
    number=float(input("Składnik 1:"))
    number_1=float(input("Składnik 2:"))
    output=number/number_1
    print("Dzielę %s %s" % (number, number_1))

print("Wynik to: %s" % (output))