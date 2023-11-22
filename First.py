
class Asset:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def calculate_depreciation(self):
        raise NotImplementedError("Subclasses must implement calculate_depreciation")


class Stock(Asset):
    def __init__(self, name, value, symbol):
        super().__init__(name, value)
        self.symbol = symbol

    def calculate_depreciation(self):
        return f"Depreciation of {self.name}'s stock is calculated based on market trends."


class RealEstate(Asset):
    def __init__(self, name, value, location):
        super().__init__(name, value)
        self.location = location

    def calculate_depreciation(self):
        return f"Depreciation of {self.name}'s real estate is calculated based on property market conditions."


class BankAccount(Asset):
    def __init__(self, name, value, interest_rate):
        super().__init__(name, value)
        self.interest_rate = interest_rate

    def calculate_depreciation(self):
        return f"Depreciation of {self.name}'s bank account is calculated based on interest rates."


# Example usage:

stock_asset = Stock("TechCorp", 50000, "TCO")
real_estate_asset = RealEstate("City Tower", 800000, "Downtown")
bank_account_asset = BankAccount("Savings", 10000, 0.03)

assets = [stock_asset, real_estate_asset, bank_account_asset]

for asset in assets:
    print(f"{asset.name}: {asset.calculate_depreciation()}")