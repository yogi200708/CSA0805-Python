# TASK 2: OTP Verification with while and for loops
CORRECT_OTP = "2468"

def check_while():
    attempts = 0
    while attempts < 3:
        otp = input("Enter OTP: ")
        if otp.strip() == "":
            print("Blank entry is not counted")
            continue
        if otp == CORRECT_OTP:
            print("Login successful")
            break
        attempts += 1
        print("Wrong OTP")
    else:
        print("Account locked for 30 minutes")

def check_for():
    attempts = 0
    for _ in range(3):
        otp = input("Enter OTP: ")
        if otp.strip() == "":
            print("Blank entry is not counted")
            continue
        if otp == CORRECT_OTP:
            print("Login successful")
            break
        attempts += 1
        print("Wrong OTP")
    else:
        print("Account locked for 30 minutes")

print("Uncomment check_while() or check_for() below to test the interactive program.")
# check_while()
# check_for()
# pass is a no-operation statement; continue skips to the next loop turn.
