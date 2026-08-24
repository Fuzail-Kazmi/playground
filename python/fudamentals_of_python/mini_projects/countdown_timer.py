# Requirements:

# Input:

# 5

# Output:

# 5
# 4
# 3
# 2
# 1
# Blast Off!

# Rules
# while loop use karna.
# Negative input handle karna.
# Pseudocode pehle.
# Code baad mein.

# while loop lagai ga
# condition check hogi 
# iteration hogi 
# value update hogi 
# jab mera timer 0 kai equivalent hoga
# tab 1 condition true hogi or Blast off! print hoga

timer = int(input("Enter Your Timer: "))

if timer >= 0:
    while timer > 0:
        print(timer)
        timer = timer - 1
    if timer == 0:
        print("Blast Off!")
else:
    print('Please enter a positive number')