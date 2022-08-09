money = 5000
drugs = {'Paracetamol': 50, 'Flagyl': 100,
         'Panadol': 150, 'Piriton': 30, 'Septrin': 200}

print('SIMULATING A PHARMACY EXPERIENCE')
for drug_name in drugs:
    print("""
    -------------------------
        MEDICRIB PHARMACY
    ------------------------- """)
    print('You have ' + str(money) + ' naira in your wallet')
    print('Each ' + drug_name + ' costs ' + str(drugs[drug_name]) + ' naira')

    drug_request = input('How many cards of ' + drug_name + ' do you want ')
    print('You want to get ' + drug_request + ' cards of ' + drug_name)

    count = int(drug_request)
    total_price = count * drugs[drug_name]
    print('The total price will be ' + str(total_price) + ' naira')

    if money >= total_price:
        print('You have bought ' + drug_request + ' cards of ' + drug_name)
        money -= total_price
        if money == 0:
            print('You have exhausted your money')
            break

    else:
        print('You do not have enough money')
        print('You can not buy that many cards of ' + drug_name)

print('YOU HAVE ' + str(money) + ' NAIRA LEFT')
