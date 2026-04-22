def validate_email(email):
    if "@" in email and "." in email:
        print("Valid Email")
    else:
        print("Invalid Email")

validate_email("sandeeppettugari@gmail.com")