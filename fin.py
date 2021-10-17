salary = 900045 
budget = 253000

spent = int(input("How much money did you spent this month ? : "))
if spent<budget:
    balance = budget-spent
    print("Yayy !! You can spend" + balance + "more money this month.")

else: 
    print("Oops ! You already spent to the limit. You should not spend moremoney this month.")
