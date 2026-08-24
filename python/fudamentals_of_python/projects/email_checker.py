# String Project 2 — Email Checker

# Requirements:

# User email enter kare


# Agar:
# .com par end hoti hai


# Print:
# Valid Email


# Else:
# Invalid Email

# Example:

# fuzail@gmail.com

# Output:

# Valid Email

email = input("Enter Your Email: ").lower()
if email.endswith(".com"):
    print(f"{email} Valid Email")
else:
    print(f"{email} Invalid Email")    