def startingScreen():
    while True:
        choice = input("Do you want to log in or sign up?: ").lower()
        if choice == "log in":
            logIn()
            break
        elif choice == "sign up":
            registration_list = signUp()
            print("Registration list:", registration_list)
            break
        else:
            print("Please enter a valid input (log in) or (sign up).")


def logIn():
    print("Time to log in!")
    username = input("Enter your username/email: ")
    passcode = input("Enter your passcode: ")

    with open("data.txt", "r") as f:
        all_data = f.read().split("\n")

    for line in all_data:
        info = line.split(";")
        if str(info[0]) == username:
            if str(info[1]) == passcode:
                loggedIn(username)
                return
    print("You did not enter a valid username/passcode.")


def signUp():
    print("Time to sign up!")
    username = input("Enter your username/email: ")
    passcode = input("Enter your passcode: ")
    rpt_passcode = input("Repeat your passcode: ")

    registration_list = []
    while True:
        if passcode == rpt_passcode:
            with open("data.txt", "a") as file:
                file.write(username + ";" + passcode + "\n")
                logIn()
                break
        else:
            print("Your passcodes do not match. Please try again.")
            break
            
    registration_list.append(username)
    registration_list.append(passcode)

    return registration_list

if __name__ == "__main__":
    startingScreen()

def loggedIn(username):
    print("Hello, " + username + ", You are logged in!")



