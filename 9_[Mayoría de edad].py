### Mayoría de edad ##

def over_18(age, resting_years):
    if age < 18:
        print("¡Usted es menor, todavía le quedan", (resting_years) ,"años para alcanzar la mayoría de edad!")
        return False
    if age >= 18:
        print("¡Usted es mayor de edad!")
        return True

age = int(-1)
while age < 0:
    try:
        age = int(input("Por favor, introduzca su edad: "))
    except:
        print("¡Solo aceptamos números positivos enteros!")

resting_years = 18 - age

over_18(age, resting_years)