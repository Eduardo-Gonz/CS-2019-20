print("WELCOME TO MY CALCULATOR")

while True: 
    welcome_input = str(input("TO ENTER PROGRAMMING MODE 1 ENTER P. \nTO ENTER PROGRAMMING MODE 2 ENTER M  \nTO ENTER SCIENTIFIC MODE ENTER S  \nOR press any key TO EXIT:  ").capitalize())

    if (welcome_input == "P"):
        print("You have entered programming mode 1. You can convert from decimal to binary here.")
        # Proramming Mode 1
        input_number = int(input("Enter your number "))
        bits = []

        if input_number < 0:
            print("Number must be greater than zero!")
        else:
            # Running Progamming...
            while input_number != 0:
                bits.append(int(input_number % 2))
                input_number = int(input_number // 2 )

            bits.reverse() 
            print (''.join(map(str, bits)))
            # print(bits)
        # --end Programming mode 1

        # --start Programming mode 2
    elif (welcome_input == "M"):
        print("You have entered programming mode 2. You can convert from binary to decimal here.")

        print("Enter your binary number below: ")
        Digit1 = int(input("Digit 1: "),2)
        Digit2 = int(input("Digit 2: "),2)
        Digit3 = int(input("Digit 3: "),2)
        Digit4 = int(input("Digit 4: "),2)
        Digit5 = int(input("Digit 5: "),2)
        Digit6 = int(input("Digit 6: "),2)
        Digit7 = int(input("Digit 7: "),2)
        Digit8 = int(input("Digit 8: "),2)


        D1 = Digit1 * 2**7
        D2 = Digit2 * 2**6
        D3=  Digit3 * 2**5
        D4 = Digit4 * 2**4
        D5 = Digit5 * 2**3
        D6 = Digit6 * 2**2
        D7 = Digit7 * 2**1
        D8 = Digit8 * 2**0

        print(D1 + D2 + D3 + D4 + D5 + D6 + D7 + D8)
        
        # --end Programming mode 2

        # --start Scientific mode
    elif (welcome_input == "S"):
        print("You have entered scientific mode.")
        num1 = float(input("Enter number:  "))
        oper = input("choose an operand: + - * / **:  ")
        num2 = float(input("Enter number:  "))

        if (oper == "+"):
            print(num1 + num2)
        elif (oper == "-"):
            print(num1 - num2)
        elif (oper == "*"):
            print(num1 * num2)
        elif (oper == "/"):
            print(num1 / num2)
        elif (oper =="**"):
            print(num1 ** num2)
        else:
            print("Invalid selection")
        # --end Scientific mode
    else: 
        print("GOODBYE")
        break