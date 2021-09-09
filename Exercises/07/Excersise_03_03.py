"""
Tram
Kokchun is a clumpsy computer user that doesn't take trams too often.
Write a program to prompt the user for:

number of times he/she wants to take tram in one month
cost for one ticket
cost for monthly card
The program should calculate if it's worth for him to buy monthly card or not.
Make the program user friendly with clear error messages and ask again in case of input errors.
"""

"""
input nuvarande kostnad för vald transport
output kost per biljett
output kost för månadskort

output diff i kostnad vs nuvarande transport +/-

Enkelt gjort med fråga på månad, ej tagit hand om felsvar map månad
"""

def calculate_cost(cost, month):
    cost_ticket = 34
    cost_month_card = 795
    day_per_month = {"jan": 31, "feb": 28, "march": 31, "april": 30, "may": 31, "june": 30, "july": 31, "aug": 31,
                     "sept": 30, "oct": 31, "nov": 30, "dec": 31}
    for key, value in day_per_month.items():
        if month == key:
            diff_for_ticket = cost - (cost_ticket * value)
            diff_for_card = current_transport_cost - cost_month_card
            if diff_for_card and diff_for_ticket > 0.0:
                print()
                print(f" Du kommer att spara {diff_for_ticket} kronor in {key} vid köp av enkelbiljett")
                print(f" Du kommer att spara {diff_for_card} kronor vid köp av månadskort")
                print(" Hej Du sparar pengar på att åka Spårvagn.")
                print(" Tänk på vad du kan spara och använda till bra saker!")
                print()
            else:
                print()
                print(" Hej du har redan ett transportsätt som kostar mindre än spårvagn ")
                print(" Tack för att du testade!")
                print(" Du är välkommen att testa att åka spårvagn")

    #return diff_for_card, diff_for_ticket


while True:
    try:
        current_transport_cost = float(input("Enter the current cost for your transportation: "))
        month = input("Enter the month you want to check: ")
        if current_transport_cost <= 0:
            print("Negativt tal! Försök igen: ")
            print()

        else:
            calculate_cost(current_transport_cost, month)
            break

    except ValueError:
        print("Inte nummer! Försök igen! ")


