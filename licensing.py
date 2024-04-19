def check_license_eligibility(age):
    if age >= 18:
        print ("congratulations! You are eligible for a driver's license.")
    elif age >= 16:
        print("you are eligible for a learner's permit.")
    else:
        print("sorry, you are not eleigible for a driver's license yet.")



age = int(input("please enter your age:"))

check_license_eligibility(age)