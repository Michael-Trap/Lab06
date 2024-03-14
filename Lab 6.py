# Michael Trapani - Lab 6

def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

while True:
    menu()
    menu_input = int(input("\nPlease enter an option: "))

    if menu_input == 1:
        password_ = ""
        password = input("Please enter your password to encode: ")
        for x in range(len(password)):
            if int(password[x]) < 7:
                password_ += str(int(password[x]) + 3)
            else:
                password_ += str(int(password[x]) + 3 - 10)
        #print(password_)
        print("Your password has been encoded and stored!\n")

    if menu_input == 2:
        pass

    if menu_input == 3:
        exit()

    else:
        pass

    # if __name__ == '__main__':