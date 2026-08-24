# Quiz 1

# Output?

# names = ["A", "B", "C"]

# for index, name in enumerate(names):
#     print(index, name)

# 0 A
# 1 B
# 2 C

# Quiz 2

# Output?

# names = ["A", "B", "C"]

# for index, name in enumerate(names, start=1):
#     print(index, name)

# 1 A
# 2 B
# 3 C

# Thinking Question

# Ye dono same kaam kyun karte hain?

# for i in range(len(names)):
#     print(i, names[i])

# aur

# for i, name in enumerate(names):
#     print(i, name)

# range(len(list))
# =
# Index khud manage karo

# for i in range(len(names)):
#     print(i, names[i])

# Yahan:

# len(names) se total items milte hain.
# range() index banata hai.
# names[i] se value nikalte hain.

# Matlab:

# Index khud banana
# Phir us index se value nikalna
# Version 2
# for i, name in enumerate(names):
#     print(i, name)

# Yahan:

# enumerate() khud index + value dono de deta hai

# Isliye:

# names[i]

# likhne ki zarurat nahi.

# enumerate(list)
# =
# Python se index manage karwa lo