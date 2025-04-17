# Virtual ATM Machine in Python

# Sample raw data

accounts = {
    "123456":{
        "pin":"123",
        "account balance":5000
    },
    "789012":{
        "pin":"456",
        "account balance":0
    },
    "3456789":{
        "pin":"999",
        "account balance":1500
    }
}

card_num = input("Please enter your card no. : ")

# Valid card number validation

if card_num not in accounts.keys():
    print("Please enter correct card number!!")

# Valid pin validation

else:
    pin = input("Please enter your atm pin: ")
    ac_data = accounts[card_num]
    if pin != ac_data["pin"]:
        print("Please enter correct pin!!")
    else:
        print("Welcome!!")
        amount = int(input("Please enter amount to withdraw: "))

        if amount <= ac_data["account balance"]:
            # Valid Note Validation
            if amount%500 == 0:
                print(f"withdraw successful of Rs. {amount}")
                print(f"Your updated a/c balance is {ac_data["account balance"]-amount}")
            else:
                print("Please enter amount in the multiple of 500!!")
        else:
            print("insufficient balance!!")

