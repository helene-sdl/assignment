"""
PowerOfTen
"""
# Provide your solution here
num = int(input("Please enter a max three-digit number: "))

if num < 0:
    print("number cannot be negative")
elif num >= 1000:
    print("number has more than three digits")
elif 1 <= num <= 10:
    print(f"{num} = {num % 10} * 1")
elif 1 <= num < 100:
    print(f"{num} = {num//10} * 10 + {num % 10} * 1")
else:
    print(f"{num} = {num//100} * 100 + {num//10%10} * 10 + {num % 10} * 1")


"""
Cash Box
"""
# Provide your solution here
while True:
    amount_to_pay = int(input("To pay: "))
    if amount_to_pay < 0:
        print("Negative payment is invalid.")
        continue
    amount_received = int(input("Received: "))
    if amount_received < 0:
        print("Negative received amount is invalid.")
        continue
    if amount_to_pay > amount_received:
        print("You did not pay enough.")
    elif amount_to_pay <= amount_received:
        print("Your change is: " + str(amount_received - amount_to_pay))
        break

