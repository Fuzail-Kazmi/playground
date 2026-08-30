# 1. PARENT CLASS (Inheritance ke liye)
class SmartPhone:
    # 4. __init__ (Auto-run hota hai aur values set karta hai)
    def __init__(self, brand, price):
        self.brand = brand
        # 2. ENCAPSULATION (Double underscore '__' se price ko private kar diya)
        self.__price = price  

    # 3. SELF (Class ke andar current object ko point kar raha hai)
    def show_details(self):
        return f"Brand: {self.brand}, Price: {self.__price}"

    # 5. POLYMORPHISM (Yeh method neeche badal jayega)
    def ringtone(self):
        return "Tring Tring... Basic Ringtone"


# 5. INHERITANCE (Samsung ne SmartPhone ki saari abilities le lein)
class Samsung(SmartPhone):
    def __init__(self, brand, price, camera_pixels):
        # Parent class ke constructor ko call kiya
        super().__init__(brand, price)
        # Child ne apna NAYA FEATURE add kiya
        self.camera = camera_pixels  

    # 5. POLYMORPHISM (Same name ka function lekin behavior alag - Method Overriding)
    def ringtone(self):
        return "Over the Horizon... Samsung Premium Ringtone! 🎶"


# --- Chaliye ab isko run karke check karte hain ---

# Object banaya (__init__ apne aap chal gaya)
my_phone = Samsung("Samsung S26", 150000, "200 MP")

# Inheritance aur Naye Feature ka maza:
print(my_phone.show_details())  # Output: Brand: Samsung S26, Price: 150000
print(f"Camera: {my_phone.camera}")  # Output: Camera: 200 MP

# Polymorphism ka demo (Samsung ne apni alag awaz nikali):
print(my_phone.ringtone())  # Output: Over the Horizon... Samsung Premium Ringtone!

# Encapsulation ka test (Bahar ka banda direct price change nahi kar sakta):
# print(my_phone.__price)  # Agar yeh line chalayein toh ERROR aayega!
