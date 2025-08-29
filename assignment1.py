# Assignment 1: Design Your Own Class 🏗️

# Parent class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"

# Child class (Smartphone inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.storage = storage
        self.battery = battery

    def call(self, contact):
        print(f"📞 Calling {contact} from {self.device_info()}")

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"🔋 Battery charged to {self.battery}%")

    def phone_info(self):
        return f"{self.device_info()} | Storage: {self.storage}GB | Battery: {self.battery}%"


# ----------- TESTING -------------
phone1 = Smartphone("Samsung", "Galaxy S25", 256, 80)
phone2 = Smartphone("Apple", "iPhone 16", 512, 50)

print(phone1.phone_info())
phone1.call("Alice")
phone1.charge(30)

print(phone2.phone_info())
phone2.call("Bob")
