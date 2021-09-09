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
Lagt in om olika mängd dagar men det gäller för användaren att jämföra kostnaden för rätt dag
"""

day_per_month = [10, 15, 20, 28, 30, 31]

while True:
    try:
        current_transport_cost = float(input("Enter the current cost for your transportation: "))
        if current_transport_cost <= 0:
            print("Negativt tal! Försök igen: ")
            print()

        else:
            cost_ticket = 34
            cost_month_card = 795
            for day in day_per_month:
                diff_for_ticket = current_transport_cost - (cost_ticket * day)
                print(f" Du kommer att spara {diff_for_ticket} kronor vid {day} dagars användande vid köp av enkelbiljett")
                diff_for_card = current_transport_cost - cost_month_card
            break

    except ValueError:
        print("Inte nummer! Försök igen! ")

if diff_for_ticket and diff_for_card > 0.0:
    print(f" Du kommer att spara {diff_for_card} kronor vid köp av månadskort")
    print(" Hej Du sparar pengar på att åka Spårvagn.")
    print(" Tänk på vad du kan spara och använda till bra saker!")
    print()
else:
    print()
    print(" Hej!\n Du har redan ett transportsätt som kostar mindre än spårvagn ")
    print(" Tack för att du testade!")
    print(" Du är välkommen att testa att åka spårvagn")
