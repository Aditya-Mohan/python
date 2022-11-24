idcard = input("Do you have the idcard ?: ")
if idcard == "yes" or idcard == "Yes":
    hallticket = input("Do you have the hallticket ?: ")
    if hallticket == "yes" or hallticket == "Yes":
        userid = int(input("Enter your userid: "))
        if userid >= 2000 and userid <= 5500:
            password = input("Enter your password: ")
            if password == "hallticket$%03":

                print("Be ready for your exam")
            else:
                print("Wrong password, Try again!")
        else:
            print("Incorrect userid")
    else:
        print("Missing hallticket")
else:
    print("Missing ID")
