print("**********************")
print("*                    *")
print("*    ATM MACHINE     *")
print("*                    *")
print("**********************")
g_pin = int(input("Generate your pin: "))  # generate your new pin.
print("pin generated sucessfully")
pin = int(input("Enter your pin: "))   # pin input.
bal = 10000                                  # balance of the user.
if pin != g_pin:                          # loop for pin and generated pin.
    print("entered pin is wrong")
else:
    choose =("Kindly choose your service")
    A = "press C to check your balance"
    B = "press W to wihdraw your ballance"
    E = "press D to deposite balance to your account"
    F = "press Q to quite"
    print(choose)
    print(A)
    print(B)
    print(E)
    print(F)
    while True:
        usr = input("press to continue: ").upper()  # user input for services .upper is to caps the users input.
        if usr == 'C':
            print("your balance is: " , bal)
        elif usr == 'W':
            print("Your balance is: " , bal)
            w_amt = int(input("Enter your amount to withdraw: "))   #w_amt is withdraw amount.
            bal = bal - w_amt
            print("your available balance is: " , bal)
        elif usr == 'D':
            print("Your balance is: ", bal)
            d_amt = int(input("Enter your amount to withdraw: "))   # d_amt is deposited amount.
            bal = bal + d_amt
            print("Your available balacne is: " , bal)
        elif usr == 'Q':
            print("transaction cancelled")
            break
        else:
            print("invalid input")
